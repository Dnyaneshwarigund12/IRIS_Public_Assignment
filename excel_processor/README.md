
# 📊 FastAPI Excel Processor

A FastAPI application that processes Excel sheets and exposes APIs to:
- List sheet names
- Retrieve row names from a sheet
- Compute the sum of numeric values in a specific row

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8+
- pip

### 🧱 Install Dependencies

```bash
pip install -r requirements.txt
````

### ▶️ Run the Server

```bash
uvicorn main:app --reload --port 9090
```

Then visit:
🌐 **[http://localhost:9090/docs](http://localhost:9090/docs)** (OpenAPI)
📄 **[http://localhost:9090/redoc](http://localhost:9090/redoc)** (ReDoc)

> ⚠️ **Make sure the server is running before opening the links above.**

---

## 📁 File Structure

```
excel_processor/
├── main.py
├── routers/
│   └── api.py
├── services/
│   └── excel_service.py
├── utils/
│   └── file_loader.py
├── Data/
│   └── capbudg.xls
├── requirements.txt
└── README.md
```

---

## 🧪 API Endpoints

### 📌 Base URL

```
http://localhost:9090
```

---

### 1. `GET /list_tables`

**Description:** Lists all sheet names in the Excel file.

**Response Example:**

```json
{
  "tables": [
    "CapBudgWS"
  ]
}
```

---

### 2. `GET /get_table_details?table_name=...`

**Query Parameters:**

* `table_name`: Name of the sheet/table.

**Description:** Returns row names (values in first column) for the selected table.

**Example Response:**

```json
{
  "table_name": "CapBudgWS",
  "row_names": [
    "INITIAL INVESTMENT",
    "Initial Investment=",
    "Opportunity cost (if any)=",
    "Lifetime of the investment",
    "Salvage Value at end of project=",
    "Deprec. method(1:St.line;2:DDB)=",
    "Tax Credit (if any )=",
    "Other invest.(non-depreciable)=",
    "WORKING CAPITAL",
    "Initial Investment in Work. Cap=",
    "Working Capital as % of Rev=",
    "Salvageable fraction at end=",
    "GROWTH RATES",
    "Revenues",
    "Fixed Expenses",
    "Default: The fixed expense growth rate is set equal to the growth rate in revenues by default.",
    "INITIAL INVESTMENT",
    "Investment",
    " - Tax Credit",
    "Net Investment",
    " + Working Cap",
    " + Opp. Cost",
    " + Other invest.",
    "Initial Investment",
    "SALVAGE VALUE",
    "Equipment",
    "Working Capital",
    "OPERATING CASHFLOWS",
    "Lifetime Index",
    "Revenues",
    " -Var. Expenses",
    " - Fixed Expenses",
    "EBITDA",
    " - Depreciation",
    "EBIT",
    " -Tax",
    "EBIT(1-t)",
    " + Depreciation",
    " - ∂ Work. Cap",
    "NATCF",
    "Discount Factor",
    "Discounted CF",
    "Book Value (beginning)",
    "Depreciation",
    "BV(ending)"
  ]
}
```

---

### 3. `GET /row_sum?table_name=...&row_name=...`

**Query Parameters:**

* `table_name`: Sheet name
* `row_name`: Specific row (must match a row returned from `/get_table_details`)

**Description:** Computes the sum of numeric values in the selected row.

**Example Response:**

```json
{
  "table_name": "CapBudgWS",
  "row_name": "Fixed Expenses",
  "sum": 0.4
}
```

---

## 🔗 Useful Links

* [OpenAPI Docs](http://localhost:9090/docs) – Swagger UI
* [ReDoc Docs](http://localhost:9090/redoc) – Alternative API view

> ⚠️ **Run the server before opening these links.**

---

## 👨‍💻 Author

* Dnyaneshwari Gund
* GitHub: [github.com/Dnyaneshwarigund12](https://github.com/Dnyaneshwarigund12)

---
