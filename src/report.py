import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from src.rule_checks import (
    check_missing_values,
    check_negative_closing_values,
    check_sudden_spikes,
    check_volume_spikes
)

def generate_report(data_path="data/sample_index_data.csv", output_path="outputs/final_report.csv"):
    try:
        df = pd.read_csv(data_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    results = {
        'missing_values': check_missing_values(df),
        'negative_closing': check_negative_closing_values(df),
        'sudden_spikes': check_sudden_spikes(df),
        'volume_spikes': check_volume_spikes(df)
    }

    combined_report = pd.concat(results.values(), keys=results.keys())
    combined_report.index.names = ['Anomaly_Type', None]
    combined_report = combined_report.reset_index()  # flatten index

    combined_report.to_csv(output_path, index=False)
    print(f"Report generated and saved to {output_path}")
    return combined_report
    

if __name__ == "__main__":
    generate_report()
    
