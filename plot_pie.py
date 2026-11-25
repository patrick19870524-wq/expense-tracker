import csv
import sys
from collections import defaultdict

import matplotlib.pyplot as plt

FILE = "expenses.csv"
OUTPUT = "pie_chart.png"

# 讓圖表能顯示中文（Windows 用微軟正黑體）
plt.rcParams["font.sans-serif"] = [
    "Microsoft JhengHei", "PingFang TC", "Noto Sans CJK TC", "Arial Unicode MS",
]
plt.rcParams["axes.unicode_minus"] = False


def load_totals(path=FILE):
    """讀取 CSV，回傳 {類別: 總金額}"""
    totals = defaultdict(float)
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            totals[row["category"]] += float(row["amount"])
    return totals


def draw_pie(totals, output=OUTPUT):
    labels = list(totals.keys())
    values = list(totals.values())
    total = sum(values)

    def show_label(pct):
        return f"{pct:.1f}%\n${pct * total / 100:,.0f}"

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(
        values,
        labels=labels,
        autopct=show_label,
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 2},
        textprops={"fontsize": 12},
    )
    ax.set_title(f"各類別支出比例（總計 ${total:,.0f}）", fontsize=16)
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print("圖表已存成", output)
    plt.show()


def main():
    try:
        totals = load_totals()
    except FileNotFoundError:
        print(f"找不到 {FILE}，請先執行 add_expense.py 新增資料")
        sys.exit(1)
    if not totals:
        print("沒有任何支出資料")
        sys.exit(1)
    draw_pie(totals)


if __name__ == "__main__":
    main()