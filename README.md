# \# 記帳小工具 Expense Tracker

# 

# 用 Python 做的簡單記帳工具：輸入支出，依類別畫出圓餅圖。

# 

# \## 功能

# \- 新增多筆支出（日期、金額、類別，備註可選），存成 `expenses.csv`

# \- 讀取 `expenses.csv`，產生各類別支出的圓餅圖

# 

# \## 環境需求

# \- Python 3.8 以上

# \- matplotlib

# 

# \## 安裝

# ```bash

# git clone https://github.com/patrick19870524-wq/expense-tracker.git

# cd expense-tracker

# python -m pip install -r requirements.txt

# ```

# 

# \## 執行

# \### 1. 新增支出（輸入模組）

# ```bash

# python add\_expense.py

# ```

# 依提示輸入日期（YYYY-MM-DD，按 Enter 用今天）、金額、類別、備註，輸入 `n` 結束。資料會存進 `expenses.csv`。

# 

# \### 2. 產生圓餅圖（視覺化模組）

# ```bash

# python plot\_pie.py

# ```

# 會跳出圓餅圖視窗，同時存成 `pie\_chart.png`。

# 

# \## 範例圖表

# !\[Sample pie chart](pie\_chart.png)

# 

# \## 檔案說明

# | 檔案 | 說明 |

# |---|---|

# | `add\_expense.py` | 輸入模組 |

# | `plot\_pie.py` | 視覺化模組 |

# | `expenses.csv` | 範例資料 |

# | `requirements.txt` | 套件清單 |

# 

# \## 分支說明

# \- `feature-input`：輸入模組

# \- `feature-piechart`：圓餅圖模組

# \- `integration`：合併以上兩個分支

