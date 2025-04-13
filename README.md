# Homeworks 3
Homeworks 3 8-4-2025
test use in VS code 12-4-2025 17:31
test save in Vs code syn to github 12-4-2025 17:46
PS : if vs code can't use .venv by any python version, then can input code at Terminal :
python -V , check python Version
which python -> enter , it will show a python link, then copy the link, goback to vs code, at the top 'Enter interpreter path...' paste the link and 'Enter', it will use the follwing python version.
atfer install .venv , but need to input source .venv/bin/activate  , then vs terminal will show (.venv) js@JSdeMacBook-Air XXX , if not, that mean you can't use pip list, pip install fastapi, pip freeze > requirements.txt and pip install -r requirements.txt ... 或用在右下按＋ ZSH
pip install requests ? install at the startup ?
learn how to syn to github, 1, git config --global user.name "Jack So" -> enter 2, git config ==global use.email "oskcaj@gmail.com" -> enter 3, when syn it will non-stop loading, need input a commit.
read other ppl python file, input pip install -r requirements.txt , it will auto to install all you need software

功課。
1， 將第二堂的功課，用SQLMODEL來處理。 
2， 將產品資料放入SQLITE DATABASE內
3， 重寫SHOPPING CART ，要應用 SQLMODEL，要對按DATABASE 應用
4， 全份功課同步到GITHUB

AI REMARK

```markdown
# 🧾 IKEA Furniture Database 功課說明

本專案是 Venturenix LAB 課程中針對 SQLModel、SQLite 資料庫實作與資料操作的練習。透過建立模型、匯入資料、查詢、入庫與購物流程，讓學生理解資料庫操作的全流程。

---

## 📁 專案結構

```
Homeworks3-2/
│
├── ikea_models.py         # 所有商品類別模型定義（使用 SQLModel）
├── main.py                # 初始建立資料庫並匯入樣本資料
├── read_database.py       # 查閱資料庫內容（支援多類別）
├── purchase.py            # 入庫功能（根據 product_id 增加庫存）
├── shopping_cart.py       # 簡易購物車模擬（自動扣庫存、計算總價）
└── ikea.db                # SQLite 資料庫檔案
```

---

## 📦 商品模型設計（ikea_models.py）

建立一個共用父類別 `IkeaFurnitureBase`（不產生資料表 `table=False`），由以下三個子類別繼承並產生對應資料表：

- `Mattress`：床褥
- `BedFrame`：床架
- `Chair`：椅子

每個商品皆包含：

- 共用欄位：`product_id`、`name`、`category`、`price`、`stock` 等
- 專屬欄位（例如床褥的 `firmness`、床架的 `style`、椅子的 `has_wheels`）

---

## 🚀 功能說明

### 1️⃣ 匯入樣本資料（main.py）

```bash
python main.py
```

- 建立 `ikea.db`
- 建立三個資料表：mattress、bedframe、chair
- 匯入每類別各 10 筆測試資料

### 2️⃣ 查詢所有資料（read_database.py）

```bash
python read_database.py
```

- 顯示所有床褥、床架、椅子的完整資料
- 可根據 `product_id` 進行查詢篩選

### 3️⃣ 入庫功能（purchase.py）

```bash
python purchase.py
```

功能說明：

- 輸入 `product_id` 與 `入庫數量`（例如：`BF101 5`）
- 系統自動查找對應商品並增加庫存數量
- 找不到 ID 則提示錯誤

### 4️⃣ 購物車模擬（shopping_cart.py）

```bash
python shopping_cart.py
```

功能流程：

1. 輸入購物清單（格式：`product_id 數量` 多組，例如：`903.195.12 2 BF101 1 CH105 3`）
2. 系統依序處理：
   - 檢查商品是否存在
   - 檢查庫存是否足夠
   - 全部通過才執行扣庫存並顯示總金額
3. 若有任何錯誤（找不到商品 / 庫存不足），整筆訂單不成立，提示錯誤並要求重新輸入

---

## ✅ 完成本功課所學技能

- [x] SQLModel 類別繼承、欄位設計
- [x] SQLite 資料庫操作（create、insert、select、update）
- [x] FastAPI 預備：資料模型與查詢邏輯結構化
- [x] 購物流程資料處理（資料驗證 + 批次處理）
- [x] 使用 Session 進行資料庫連線與交易處理

---

## 📌 學習心得

- 明白了 SQLModel 如何用 `table=False` 定義父類別
- 熟悉 Session 的重要角色（所有 DB 操作都需透過它）
- 購物流程需要考慮資料一致性（任何錯誤就不執行）
- 建立 `.db` 後，只需一次匯入，往後可直接查詢與更新

---

## 🔍 建議後續學習方向

- 分離資料與邏輯（資料讀取使用 JSON 或 CSV）
- 製作 RESTful API（FastAPI + SQLModel）
- 製作網頁前端連接購物功能


