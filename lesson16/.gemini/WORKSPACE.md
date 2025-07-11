### 專案目標 (Project Goal)

我們的目標是建立一個命令列介面（CLI）應用程式，其核心功能如下：

- 讀取指定的 CSV 檔案。
- 根據讀取的資料建立一個樞紐分析表。
- 將產生的樞紐分析表匯出為 Excel 檔案。

---

### 開發流程與規則 (Development Workflow & Rules)

1.  **任務清單 (Todolist)**:

    - 開發將依循 `todolist.md` 檔案中的任務清單進行。
    - 請**依序**完成清單中**未完成**的項目 (`[ ]`)。
    - 已完成的項目 (`[x]`) 不需要再次執行。

2.  **執行回報**:
    - 在開始執行一個新任務前，必須先回報：「現在開始執行任務：<任務說明>」。
    - 每完成一個項目，必須在回覆中更新 `todolist.md` 的內容，將對應的 `[ ]` 修改為 `[x]`。

---

### 技術規格 (Technical Specifications)

1.  **主要語言**: Python

2.  **程式碼註解**:

    - 每個 function、class 和 property 都必須包含簡要的 docstring 說明其用途。

3.  **專案結構**:

    - `app.py`: 主應用程式入口點，用於處理命令列參數和執行核心邏輯。

4.  **預期執行方式**:
    ```bash
    python app.py --csv <輸入 CSV 檔名> --excel <輸出 Excel 檔名>
    ```
    - `--csv`: 指定輸入的 CSV 檔案路徑。
    - `--excel`: 指定輸出的 Excel 檔案路徑。

---

### AI 互動設定 (AI Interaction Settings)

- **工作目錄**: 所有檔案操作皆以 `實際案例4` 資料夾作為根目錄。
- **回覆語言**: 請使用繁體中文進行所有回覆。`檔案名稱`和`程式碼`中的既有英文無需修改。
