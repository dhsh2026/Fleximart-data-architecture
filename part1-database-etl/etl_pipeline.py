import os
import pandas as pd

# -------------------------------
# STEP 1: Resolve paths
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

print("Base directory:", BASE_DIR)
print("Data directory:", DATA_DIR)

# -------------------------------
# STEP 2: File paths
# -------------------------------
customers_path = os.path.join(DATA_DIR, "customers_raw.csv")
products_path = os.path.join(DATA_DIR, "products_raw.csv")
sales_path = os.path.join(DATA_DIR, "sales_raw.csv")

# -------------------------------
# STEP 3: Read CSV files
# -------------------------------
customers_df = pd.read_csv(customers_path)
products_df = pd.read_csv(products_path)
sales_df = pd.read_csv(sales_path)

print("\n✅ All CSV files loaded successfully")

# -------------------------------
# STEP 4: Inspect data
# -------------------------------
print("\n--- CUSTOMERS ---")
print(customers_df.head())
print(customers_df.info())

print("\n--- PRODUCTS ---")
print(products_df.head())
print(products_df.info())

print("\n--- SALES ---")
print(sales_df.head())
print(sales_df.info())
sales_df = pd.read_csv(sales_path)

# -------- TRANSFORMATIONS --------
sales_df["transaction_date"] = pd.to_datetime(
    sales_df["transaction_date"],
    dayfirst=True,
    errors="coerce"
)

print("\n--- SALES ---")
print(sales_df.head())
print(sales_df.info())
# Check missing keys
print(sales_df[sales_df["customer_id"].isna()])
print(sales_df[sales_df["product_id"].isna()])
# Drop rows with missing customer_id or product_id
sales_df_clean = sales_df.dropna(subset=["customer_id", "product_id"])
# Drop duplicates
sales_df = sales_df.drop_duplicates(subset=["transaction_id"])
# Check numeric fields
sales_df = sales_df[sales_df["quantity"] > 0]
sales_df = sales_df[sales_df["unit_price"] > 0]
# Dervied column
sales_df["total_amount"] = sales_df["quantity"] * sales_df["unit_price"]
# ---------------- FINAL SALES CLEANING ----------------

sales_df_final = sales_df.copy()

# Drop missing foreign keys
sales_df_final = sales_df_final.dropna(subset=["customer_id", "product_id"])

# Drop duplicate transactions
sales_df_final = sales_df_final.drop_duplicates(subset=["transaction_id"])

# Drop invalid dates
sales_df_final = sales_df_final.dropna(subset=["transaction_date"])

# Validate numeric fields
sales_df_final = sales_df_final[
    (sales_df_final["quantity"] > 0) &
    (sales_df_final["unit_price"] > 0)
]

# Derived column
sales_df_final["total_amount"] = (
    sales_df_final["quantity"] * sales_df_final["unit_price"]
)

print("\n--- FINAL CLEAN SALES DATA ---")
print(sales_df_final.info())
print(sales_df_final.head())
