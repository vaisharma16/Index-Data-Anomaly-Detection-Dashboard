import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Config
output_path = "data/sample_index_data.csv"
num_days = 60  # past 60 days

# Generate Dates
dates = [datetime.today() - timedelta(days=i) for i in range(num_days)][::-1]
index_name = "Nifty 50"

# Simulate Closing Values & Volume with some anomalies
closing_values = np.random.normal(loc=22000, scale=300, size=num_days).round(2)
volumes = np.random.randint(2800000, 3500000, size=num_days)

# Add anomalies manually
closing_values[10] = -5                  # Negative value
closing_values[15] = np.nan              # Missing value
closing_values[25] = closing_values[24] * 1.8  # Sudden spike

# Create DataFrame
df = pd.DataFrame({
    "Date": [d.strftime("%Y-%m-%d") for d in dates],
    "Index_Name": index_name,
    "Closing_Value": closing_values,
    "Volume": volumes
})

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Save to CSV
df.to_csv(output_path, index=False)
print(f"✅ Sample index data written to {output_path}")
