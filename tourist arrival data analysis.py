import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("tourist_data.csv")
print("Dataset Loaded Successfully\n")
print(df.head())

print("\nDataset Info:")
df.info()

# -----------------------------
# Create Month-Year column (IMPORTANT)
# -----------------------------
df['Month_Year'] = df['Month'] + "-" + df['Year'].astype(str)

# -----------------------------
# BAR CHART
# -----------------------------
plt.figure(figsize=(10,5))
plt.bar(df['Month_Year'], df['Total_Tourists'])
plt.title("Total Tourist Arrivals (Bar Chart)")
plt.xlabel("Month-Year")
plt.ylabel("Number of Tourists")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show(block=True)

# -----------------------------
# LINE CHART
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Month_Year'], df['Total_Tourists'], marker='o')
plt.title("Tourist Arrival Trend (Line Chart)")
plt.xlabel("Month-Year")
plt.ylabel("Number of Tourists")
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show(block=True)
