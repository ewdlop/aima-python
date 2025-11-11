"""Deploy the AIMA Online project to a Hugging Face Space via API."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Iterable

from huggingface_hub import HfApi, upload_folder


def _resolve_token(cli_token: str | None) -> str:
    """Return the Hugging Face access token from CLI argument or environment."""
    token = (
        cli_token
        or os.getenv("HF_TOKEN")
        or os.getenv("HUGGINGFACE_TOKEN")
        or os.getenv("MCP_HF_API_TOKEN")
    )
    if not token:
        raise SystemExit(
            "找不到 Hugging Face token，請透過 --token 或環境變數 "
            "HF_TOKEN / HUGGINGFACE_TOKEN / MCP_HF_API_TOKEN 提供。"
        )
    return token


def _resolve_repo_id(cli_repo_id: str | None) -> str:
    """Return target repo id from CLI argument or environment."""
    repo_id = cli_repo_id or os.getenv("MCP_HF_SPACE_REPO")
    if not repo_id:
        raise SystemExit(
            "必須指定 Space repo id，請使用 --repo-id 或設環境變數 MCP_HF_SPACE_REPO。"
        )
    return repo_id


def _normalize_ignore(patterns: Iterable[str] | None) -> list[str]:
    """Return normalized ignore patterns for upload_folder."""
    return [pattern for pattern in (patterns or []) if pattern.strip()]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-id",
        help="Hugging Face Space repo，例如 username/mcp-fastapi。",
    )
    parser.add_argument(
        "--local-dir",
        default=str(Path(__file__).resolve().parents[1]),
        help="要上傳的本地資料夾，預設為專案根目錄。",
    )
    parser.add_argument(
        "--token",
        help="Hugging Face 存取權杖，預設讀取常見環境變數。",
    )
    parser.add_argument(
        "--space-sdk",
        default=os.getenv("MCP_HF_SPACE_SDK", "docker"),
        help="Space SDK 類型（docker、gradio、streamlit...）。",
    )
    parser.add_argument(
        "--space-hardware",
        default=os.getenv("MCP_HF_SPACE_HARDWARE", "cpu-basic"),
        help="Space 硬體選項，例如 cpu-basic、t4-small。",
    )
    parser.add_argument(
        "--update-only",
        action="store_true",
        help="僅更新既有 Space，不會自動建立新的（預設會自動建立或覆寫）。",
    )
    parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="若 Space 不存在則直接建立，不進行互動式確認。",
    )
    parser.add_argument(
        "--private",
        action="store_true",
        help="建立私人 Space。",
    )
    parser.add_argument(
        "--commit-message",
        default="Deploy AIMA Online Space",
        help="上傳時使用的提交訊息。",
    )
    parser.add_argument(
        "--ignore",
        nargs="*",
        default=[".venv*", "__pycache__", "*.pyc", ".git", "tests"],
        help="上傳時忽略的檔案/目錄 pattern。",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    token = _resolve_token(args.token)
    repo_id = _resolve_repo_id(args.repo_id)
    local_dir = Path(args.local_dir).resolve()

    if not local_dir.exists():
        raise SystemExit(f"指定的資料夾不存在：{local_dir}")

    api = HfApi(token=token)
    try:
        api.repo_info(repo_id=repo_id, repo_type="space")
        space_exists = True
    except Exception as exc:  # noqa: BLE001
        response = getattr(exc, "response", None)
        status_code = getattr(response, "status_code", None) if response else None
        if status_code == 404:
            space_exists = False
        else:
            raise

    if space_exists:
        print(f"ℹ️  使用既有 Space：{repo_id}")
        if not args.update_only:
            api.create_repo(
                repo_id=repo_id,
                repo_type="space",
                space_sdk=args.space_sdk,
                space_hardware=args.space_hardware,
                private=args.private,
                exist_ok=True,
            )
    else:
        if args.update_only:
            raise SystemExit(
                f"找不到既有 Space {repo_id}，若要自動建立請移除 --update-only。"
            )
        if not args.yes:
            answer = input(
                (
                    f"找不到 Space {repo_id}。是否要建立新的 Space？ [y/N] "
                )
            ).strip().lower()
            if answer not in {"y", "yes"}:
                raise SystemExit("已取消建立 Space。")

        print(f"➡️  建立 Space：{repo_id}")
        api.create_repo(
            repo_id=repo_id,
            repo_type="space",
            space_sdk=args.space_sdk,
            space_hardware=args.space_hardware,
            private=args.private,
            exist_ok=False,
        )

    print(f"⬆️  上傳資料夾 {local_dir} 至 Space（忽略：{args.ignore}）")
    api.upload_folder(
        repo_id=repo_id,
        repo_type="space",
        folder_path=str(local_dir),
        token=token,
        commit_message=args.commit_message,
        ignore_patterns=_normalize_ignore(args.ignore),
    )
    print("✅ 完成部署。")


if __name__ == "__main__":
    main()

