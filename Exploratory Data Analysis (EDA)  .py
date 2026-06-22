import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set global plotting style
sns.set_theme(style="ticks")
plt.rcParams["figure.figsize"] = (10, 6)

# ==========================================
# 1. GENERATE SYNTHETIC REAL ESTATE DATA
# ==========================================
print("--- Step 1: Generating Dataset ---")
np.random.seed(42)
n_houses = 800

# Base features
sqft = np.random.normal(2000, 600, n_houses).astype(int)
sqft = np.clip(sqft, 500, 5000)  # Prevent extreme outliers

neighborhood = np.random.choice(
    ["Downtown", "Suburbs", "Rural", "Waterfront"],
    size=n_houses,
    p=[0.3, 0.4, 0.2, 0.1],
)
bedrooms = np.random.choice([1, 2, 3, 4, 5], size=n_houses, p=[0.1, 0.2, 0.4, 0.2, 0.1])
year_built = np.random.randint(1950, 2025, size=n_houses)

# Base price equation with some random variance
price = (
    (sqft * 150)
    + (bedrooms * 25000)
    + (np.random.normal(50000, 30000, n_houses))
)
# Add premium adjustments based on location
price += np.where(neighborhood == "Waterfront", 150000, 0)
price += np.where(neighborhood == "Downtown", 75000, 0)
price = price.astype(int)

df = pd.DataFrame(
    {
        "House_ID": range(1, n_houses + 1),
        "Square_Feet": sqft,
        "Bedrooms": bedrooms,
        "Neighborhood": neighborhood,
        "Year_Built": year_built,
        "Price_USD": price,
    }
)

print(f"Dataset successfully created with shape: {df.shape}\n")


# ==========================================
# 2. DESCRIPTIVE STATISTICAL ANALYSIS
# ==========================================
print("--- Step 2: Descriptive Summary ---")
print("\n💡 Data Types and Non-Null Counts:")
print(df.info())
