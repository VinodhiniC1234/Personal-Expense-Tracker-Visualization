# =====================================================
# PERSONAL EXPENSE TRACKER WITH DATA VISUALIZATION
# =====================================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime

# =====================================================
# STYLE SETTINGS
# =====================================================

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

# =====================================================
# CREATE SYNTHETIC DATA
# =====================================================

print("Creating Expense Dataset...")

categories = [
    'Food',
    'Transport',
    'Shopping',
    'Bills',
    'Entertainment',
    'Healthcare',
    'Education'
]

payment_methods = [
    'Cash',
    'UPI',
    'Credit Card',
    'Debit Card'
]

records = []

# Generate 180 days of expenses
for i in range(180):

    record = {
        'Date': pd.date_range(start='2026-01-01', periods=180)[i],
        'Category': random.choice(categories),
        'Amount': random.randint(100, 6000),
        'Payment_Method': random.choice(payment_methods),
        'Description': f'Expense Record {i+1}'
    }

    records.append(record)

# Create DataFrame
expense_df = pd.DataFrame(records)

# Save CSV
expense_df.to_csv('data/expense_data.csv', index=False)

print("Dataset Created Successfully!")

# =====================================================
# LOAD DATA
# =====================================================

expense_df = pd.read_csv('data/expense_data.csv')

print("\nExpense Dataset Preview:\n")
print(expense_df.head())
# =====================================================
# DATA CLEANING
# =====================================================

expense_df.drop_duplicates(inplace=True)
expense_df.dropna(inplace=True)

expense_df['Date'] = pd.to_datetime(expense_df['Date'])
expense_df['Month'] = expense_df['Date'].dt.strftime('%B')
expense_df['Day'] = expense_df['Date'].dt.day_name()

print("\nData Cleaning Completed!")

# =====================================================
# ANALYSIS
# =====================================================

# Category Analysis
category_expense = expense_df.groupby('Category')['Amount'].sum().sort_values(ascending=False)

# Monthly Analysis
monthly_expense = expense_df.groupby('Month')['Amount'].sum()

# Payment Analysis
payment_analysis = expense_df.groupby('Payment_Method')['Amount'].sum()

# Daily Spending
daily_spending = expense_df.groupby('Date')['Amount'].sum()

# Highest Category
highest_category = category_expense.idxmax()

# Total Spending
total_spending = expense_df['Amount'].sum()

# Average Daily Spending
average_daily = daily_spending.mean()

# =====================================================
# PRINT INSIGHTS
# =====================================================

print("\n================ FINANCIAL INSIGHTS ================")

print(f"\nTotal Spending: ₹{total_spending:,.2f}")

print(f"Average Daily Spending: ₹{average_daily:,.2f}")

print(f"Highest Spending Category: {highest_category}")

print("\nCategory-wise Spending:\n")
print(category_expense)

# =====================================================
# VISUALIZATION SECTION
# =====================================================

print("\nGenerating Professional Charts...")

# -----------------------------------------------------
# CATEGORY-WISE BAR CHART
# -----------------------------------------------------

plt.figure(figsize=(12, 6))

bars = plt.bar(
    category_expense.index,
    category_expense.values,
    edgecolor='black'
)

plt.title('Category-wise Expense Analysis', fontweight='bold')
plt.xlabel('Expense Category')
plt.ylabel('Amount Spent')
plt.xticks(rotation=15)

# Add values above bars
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + 1000,
        f'₹{int(yval)}',
        ha='center',
        fontsize=10
    )

plt.tight_layout()
plt.savefig('images/category_spending.png', dpi=300)
plt.close()

# -----------------------------------------------------
# MONTHLY TREND LINE CHART
# -----------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_expense.index,
    monthly_expense.values,
    marker='o',
    linewidth=3,
    markersize=10
)

plt.title('Monthly Expense Trend', fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Spending')
plt.grid(True)

for x, y in zip(monthly_expense.index, monthly_expense.values):
    plt.text(x, y, f'₹{int(y)}', fontsize=9)

plt.tight_layout()
plt.savefig('images/monthly_trend.png', dpi=300)
plt.close()

# -----------------------------------------------------
# PAYMENT METHOD PIE CHART
# -----------------------------------------------------
plt.figure(figsize=(8, 8))

payment_analysis.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    shadow=True
)

plt.title('Payment Method Usage', fontweight='bold')
plt.ylabel('')

plt.tight_layout()
plt.savefig('images/payment_method.png', dpi=300)
plt.close()
# -----------------------------------------------------
# DAILY SPENDING TREND
# -----------------------------------------------------

plt.figure(figsize=(14, 6))

plt.plot(
    daily_spending.index,
    daily_spending.values,
    linewidth=2
)

plt.title('Daily Spending Trend', fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Daily Spending')
plt.grid(True)

plt.tight_layout()
plt.savefig('images/daily_spending.png', dpi=300)
plt.close()
# -----------------------------------------------------
# TOP 5 EXPENSE CATEGORIES
# -----------------------------------------------------

top_categories = category_expense.head(5)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=top_categories.index,
    y=top_categories.values
)

plt.title('Top 5 Expense Categories', fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Spending')

plt.tight_layout()
plt.savefig('images/top_categories.png', dpi=300)
plt.close()

print("Professional Charts Generated Successfully!")
# =====================================================
# REPORT GENERATION
# =====================================================

summary_report = {
    'Total Spending': [total_spending],
    'Average Daily Spending': [average_daily],
    'Highest Spending Category': [highest_category]
}

report_df = pd.DataFrame(summary_report)

report_df.to_csv('reports/final_report.csv', index=False)

# Save category report
category_expense.to_csv('reports/category_report.csv')

# Save monthly report
monthly_expense.to_csv('reports/monthly_report.csv')

print("\nReports Generated Successfully!")
# =====================================================
# FINAL MESSAGE
# =====================================================

print("\n================================================")
print(" PERSONAL EXPENSE TRACKER COMPLETED SUCCESSFULLY ")
print("================================================")

print("\nGenerated Outputs:")

print("1. data/expense_data.csv")
print("2. images/category_spending.png")
print("3. images/monthly_trend.png")
print("4. images/payment_method.png")
print("5. images/daily_spending.png")
print("6. images/top_categories.png")
print("7. reports/final_report.csv")
print("8. reports/category_report.csv")
print("9. reports/monthly_report.csv")