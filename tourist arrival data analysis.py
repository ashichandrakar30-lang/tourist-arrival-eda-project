import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("tourist_data.csv")

print("Data loaded successfully\n")
print(df.head())
print("\nColumns:\n", df.columns)

# -------------------------------
# Basic Info
# -------------------------------
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# -------------------------------
# Target Variable Analysis (y)
# -------------------------------
plt.figure()
plt.plot(df.index, df["y"])
plt.xlabel("Year / Index")
plt.ylabel("Total Number of Tourists")
plt.title("Tourist Arrivals Over Time")
plt.show()

# -------------------------------
# Histogram of Tourist Arrivals
# -------------------------------
plt.figure()
plt.hist(df["y"], bins=10)
plt.xlabel("Total Tourists")
plt.ylabel("Frequency")
plt.title("Distribution of Tourist Arrivals")
plt.show()

# -------------------------------
# Correlation with Target (y)
# -------------------------------
corr = df.corr()["y"].sort_values(ascending=False)
print("\nCorrelation with y:\n")
print(corr)

# -------------------------------
# Top 5 Features vs y
# -------------------------------
top_features = corr.index[1:6]  # skip y itself

for col in top_features:
    plt.figure()
    plt.scatter(df[col], df["y"])
    plt.xlabel(col)
    plt.ylabel("Total Tourists")
    plt.title(f"{col} vs Tourist Arrivals")
    plt.show()

# -------------------------------
# Average of Monthly Features
# -------------------------------
feature_cols = [col for col in df.columns if col.startswith("f")]

monthly_avg = df[feature_cols].mean()

plt.figure(figsize=(10,5))
plt.plot(monthly_avg.values)
plt.xlabel("Feature Index (f1–f41)")
plt.ylabel("Average Value")
plt.title("Average Trend of f1–f41")
plt.show()
