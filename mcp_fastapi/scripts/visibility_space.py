# """Update a Hugging Face Space visibility (public/private) via CLI."""

# from __future__ import annotations

# import argparse
# import os
# from typing import Optional

# from huggingface_hub import HfApi


# def parse_args() -> argparse.Namespace:
#     parser = argparse.ArgumentParser(description=__doc__)
#     parser.add_argument(
#         "--repo-id",
#         help="完整 Space ID，例如 username/aima_online。也可使用環境變數 MCP_HF_SPACE_REPO。",
#     )
#     parser.add_argument(
#         "--token",
#         help="Hugging Face 存取權杖，預設讀取 MCP_HF_API_TOKEN / HF_TOKEN / HUGGINGFACE_TOKEN。",
#     )
#     visibility = parser.add_mutually_exclusive_group(required=True)
#     visibility.add_argument(
#         "--private",
#         action="store_true",
#         help="將 Space 設為私人。",
#     )
#     visibility.add_argument(
#         "--public",
#         action="store_true",
#         help="將 Space 設為公開。",
#     )
#     return parser.parse_args()


# def resolve_repo_id(cli_repo_id: Optional[str]) -> str:
#     repo_id = cli_repo_id or os.getenv("MCP_HF_SPACE_REPO")
#     if not repo_id:
#         raise SystemExit(
#             "請使用 --repo-id 指定 Space，或設定環境變數 MCP_HF_SPACE_REPO。"
#         )
#     if "/" not in repo_id:
#         raise SystemExit("repo_id 必須使用 username/space-name 格式。")
#     return repo_id


# def resolve_token(cli_token: Optional[str]) -> str:
#     token = (
#         cli_token
#         or os.getenv("MCP_HF_API_TOKEN")
#         or os.getenv("HF_TOKEN")
#         or os.getenv("HUGGINGFACE_TOKEN")
#     )
#     if not token:
#         raise SystemExit(
#             "找不到 Hugging Face token。請使用 --token 或設定 MCP_HF_API_TOKEN / HF_TOKEN / HUGGINGFACE_TOKEN。"
#         )
#     return token


# def main() -> None:
#     args = parse_args()
#     repo_id = resolve_repo_id(args.repo_id)
#     token = resolve_token(args.token)

#     api = HfApi(token=token)
#     target_private = args.private

#     print(f"🔐 更新 Space `{repo_id}` 可見性為 {'private' if target_private else 'public'} ...")
#     api.update_repo_visibility(
#         repo_id=repo_id,
#         repo_type="space",
#         private=target_private,
#     )
#     print("✅ 完成。")


# if __name__ == "__main__":
#     main()

