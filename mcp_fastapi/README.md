---
title: AIMA Online
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: docker
sdk_version: "1.0"
app_file: app/main.py
pinned: false
license: apache-2.0
---
# AIMA Online

> ⚠️ **人工智慧生成內容聲明**  
> 本 README 部分段落（特別是中文說明與歷史摘要）由人工智慧協助撰寫或潤飾，僅供參考。實際資訊仍以原始資料與官方文件為準，請在引用或修改時自行驗證內容。

這個範例（暫名 **aima-online**）展示如何使用 FastAPI 與 FastMCP 建立 AIMA 演算法示範服務，並提供 Hugging Face Space 的部署流程，同時整合 Gradio 介面與 Hugging Face API 工具。

> ⚠️ **專案聲明**  
> - 此專案為社群示範，不是 AIMA 官方授權或維護版本。  
> - 演算法結果僅供教學與測試，請務必於生產環境自行驗證。  
> - Hugging Face Space 與 GitHub 上請以「aima-online」名稱發佈，可自行依需求調整說明。

## 本地開發

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
uvicorn app.app:app --reload --port 8000
```

-啟動後可透過：

- `GET http://localhost:8000/health` 取得健康檢查
- `POST http://localhost:8000/aima/search/romania` 使用 AIMA 搜尋演算法規劃路線
- `POST http://localhost:8000/aima/csp/nqueens` 求解 N 皇后問題
- `GET http://localhost:8000/gradio` 體驗 Gradio 互動介面
- `GET http://localhost:8000/hf/config` 查看 Hugging Face 設定
- `POST http://localhost:8000/hf/text-generation` 呼叫 Hugging Face Inference API 進行文字生成
- `POST http://localhost:8000/hf/spaces/deploy` 透過 Hugging Face API 建立/更新 Space

### `POST /hf/text-generation` 範例

```json
{
  "prompt": "說明 MCP protocol 的用途。",
  "model": "gpt2",
  "max_new_tokens": 60
}
```

> ⚠️ 呼叫此端點需在環境變數提供 Hugging Face token（`MCP_HF_API_TOKEN`）以及預設模型 ID（`MCP_HF_INFERENCE_MODEL`）或自訂 `model`/`inference_api_url`。

### `POST /aima/search/romania` 範例

```json
{
  "start": "Arad",
  "goal": "Bucharest",
  "algorithm": "uniform_cost"
}
```

回應會包含路徑、動作序列與總成本。

### `POST /aima/csp/nqueens` 範例

```json
{
  "n": 8,
  "algorithm": "backtracking"
}
```

支援 `backtracking` 與 `min_conflicts`。使用 `min_conflicts` 時可額外設定 `max_steps`。

## FastMCP 伺服器

專案同時提供 FastMCP 版本的工具伺服器，繼承既有的 AIMA 搜尋與 CSP 邏輯。

1. 啟動伺服器（預設監聽 `0.0.0.0:3000`）：

   ```bash
   python fastmcp_server.py          # 可透過 MCP_HOST / MCP_PORT 調整
   ```

2. 透過你的 MCP Agent 或 `.mcp.json` 中的 `aima-fastmcp` 服務連線。可用的工具：

   - `romania_route(start: str, goal: str, algorithm: str = "uniform_cost")`  
     `algorithm` 接受 `uniform_cost`、`breadth_first`、`astar`
   - `nqueens(n: int = 8, algorithm: str = "backtracking", max_steps: Optional[int] = 1000)`  
     `algorithm` 接受 `backtracking` 或 `min_conflicts`

3. 工具回傳值會沿用 FastAPI 服務的文字敘述格式，包含路徑、成本或棋盤配置等資訊。

### `.mcp.json` 設定

專案根目錄提供 `.mcp.json` 範例，預設指向本機 `http://127.0.0.1:8000`。若部署到 Hugging Face Space，請將 `base_url`、`docs_url`、`gradio_url` 改成對應的公開網址，並依需求加入認證 header。

## Gradio 互動介面

此專案已將 Gradio 介面掛載於 FastAPI：

- 啟動伺服器後開啟 `http://localhost:8000/gradio` 即可看到兩個分頁：羅馬尼亞搜尋與 N 皇后問題。
- 介面底層直接呼叫與 HTTP/MCP 相同的服務邏輯，保證結果一致。
- 部署到 Hugging Face Space（Docker 模式）後，同樣可以透過 `/gradio` 路徑存取。

## 部署到 Hugging Face Space

1. 保留此資料夾內的 `Dockerfile` 與 `.huggingface/config.json`（SDK 已預設為 `docker`）。
2. 將此資料夾推送到 Git 儲存庫並連結至 Hugging Face Space，或使用下方的部署腳本自動上傳。
3. 在 Space 介面選擇 **Docker** 類型，並設定 `Hardware`（CPU 或 GPU）。
4. 若需要環境變數，可在 Space 的 **Settings → Variables and secrets** 新增（例如 `MCP_HF_API_TOKEN`、`MCP_HF_INFERENCE_MODEL`）。

### 使用部署腳本

`scripts/deploy_space.py` 透過 Hugging Face API 自動建立/更新 Space 並上傳專案檔案。確保已安裝 `huggingface-hub` 並登入或提供 token。

```bash
python scripts/deploy_space.py \
  --repo-id your-username/mcp-fastapi \
  --token hf_xxx \
  --space-sdk docker \
  --space-hardware cpu-basic
```

常用參數：

- `--repo-id`：目標 Space 名稱（也可透過環境變數 `MCP_HF_SPACE_REPO`）。
- `--token`：Hugging Face 存取權杖（也可使用 `HF_TOKEN` / `HUGGINGFACE_TOKEN` / `MCP_HF_API_TOKEN` 環境變數）。
- `--ignore`：客製化上傳時要忽略的檔案/資料夾。
- `--update-only`：僅更新既有 Space，不自動建立新 Space（預設會自動建立或覆寫）。
- `--yes`：建立新 Space 時不再詢問確認，適合自動化流程。

#### 切換 Space 公開/私人

`scripts/visibility_space.py` 可快速更新 Space 的可見性：

```bash
python scripts/visibility_space.py \
  --repo-id ewdlop/aima_space \
  --token hf_xxx \
  --private   # 改為私人；改成 --public 可設回公開
```

若已在環境變數設定 `MCP_HF_SPACE_REPO` / `MCP_HF_API_TOKEN`，對應參數可省略。

### Dockerfile 範例

```dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
```

> Hugging Face Space 預設對外開放的埠為 `7860`，若要修改，需在 Space 設定中同步調整。

## FastMCP 連線測試

本地或 CI 可直接啟動：

```bash
python fastmcp_server.py --host 0.0.0.0 --port 3000
```

- `.mcp.json` 已提供 `aima-fastmcp` 服務設定。啟動你的 MCP Agent 後即可使用 `romania_route`、`nqueens` 工具。
- 在 Hugging Face Space 中執行時，請將 `MCP_PORT` 設為 `7860`（Space 對外開放的唯一埠），例如在 Docker `CMD`／入口腳本中加入：

  ```bash
  MCP_PORT=7860 python fastmcp_server.py
  ```

HTTP 端點（FastAPI）仍可使用 `/aima/*`、`/hf/*` 與 `/gradio` 等路由，與 FastMCP 伺服器互不衝突。


