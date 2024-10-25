import pandas as pd

# Load each dataset
customer_df = pd.read_csv('dataset/customer_profile_dataset.csv')
product_df = pd.read_csv('dataset/products_dataset.csv')
purchase_df = pd.read_csv('dataset/purchase_history_dataset.csv')

# # Display the first few rows of each dataset
# print("Customer Data:")
# print(customer_df.head())
# print("\nProduct Data:")
# print(product_df.head())
# print("\nPurchase Data:")
# print(purchase_df.head())

# data types
print(customer_df.info())
print(product_df.info())
print(purchase_df.info())

# # find missing data
# print(customer_df.isnull().sum())
# print(product_df.isnull().sum())
# print(purchase_df.isnull().sum())

# # Example: Count unique customers and products
# print("Unique customers:", customer_df['customer_id'].nunique())
# print("Unique products:", product_df['product_id'].nunique())

# Calculate total purchases per product
product_sales = purchase_df.groupby('product_id')['total_amount'].sum().sort_values(ascending=False)
print("Top products by total sales:")
print(product_sales.head())


