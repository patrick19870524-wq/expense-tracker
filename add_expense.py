import csv
import os
from datetime import datetime

FILE = "expenses.csv"
FIELDS = ["date", "amount", "category", "notes"]


def save_expense(date, amount, category, notes=""):
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(FIELDS)
        writer.writerow([date, amount, category, notes])


def ask_date():
    while True:
        text = input("日期 (YYYY-MM-DD，直接按 Enter 用今天): ").strip()
        if text == "":
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("格式錯誤，請輸入 YYYY-MM-DD")


def ask_amount():
    while True:
        try:
            value = float(input("金額: "))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("請輸入大於 0 的數字")


def ask_category():
    while True:
        text = input("類別 (例如 餐飲、交通): ").strip()
        if text:
            return text
        print("類別不能是空的")


def main():
    print("=== 記帳工具 ===")
    while True:
        date = ask_date()
        amount = ask_amount()
        category = ask_category()
        notes = input("備註 (可不填): ").strip()
        save_expense(date, amount, category, notes)
        print("已儲存！\n")
        again = input("繼續新增？(y/n): ").strip().lower()
        if again != "y":
            break
    print("結束，資料存在", FILE)


if __name__ == "__main__":
    main()