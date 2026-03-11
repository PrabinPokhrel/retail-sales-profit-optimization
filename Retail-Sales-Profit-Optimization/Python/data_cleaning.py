import pandas as pd

# File paths
input_file = r"C:\Users\WELCOME\Desktop\DataAnalysis_Projects\Retail-Sales-Profit-Optimization\Data\Raw_Data\Sample - Superstore.csv"
output_file = r"C:\Users\WELCOME\Desktop\DataAnalysis_Projects\Retail-Sales-Profit-Optimization\Data\Processed_Data\superstore_clean.csv"

# Load dataset
df = pd.read_csv(input_file, encoding="latin1")

print("Original shape:", df.shape)
print("\nColumns in dataset:")
print(df.columns)

# Remove duplicates
df = df.drop_duplicates()

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Remove rows where important values are missing
df = df.dropna(subset=["Order Date", "Sales", "Profit"])

# Feature Engineering
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Month Name"] = df["Order Date"].dt.strftime("%B")
df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

# Profit Margin
df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100
df["Profit Margin"] = df["Profit Margin"].fillna(0)

# Sales Growth by month
monthly_sales = df.groupby("Year-Month")["Sales"].sum().reset_index()
monthly_sales["Sales Growth %"] = monthly_sales["Sales"].pct_change() * 100

# Merge back to main data
df = df.merge(monthly_sales[["Year-Month", "Sales Growth %"]], on="Year-Month", how="left")
df["Sales Growth %"] = df["Sales Growth %"].fillna(0)

# Save cleaned data
df.to_csv(output_file, index=False)

print("\nCleaned data saved successfully")
print("Final shape:", df.shape)
print(f"Saved to: {output_file}")