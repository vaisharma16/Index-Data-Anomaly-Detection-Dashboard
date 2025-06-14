
# 📊 Index Data Anomaly Detection Dashboard

A Streamlit-powered web app for detecting anomalies in financial index data (e.g., Nifty 50). This project identifies missing values, negative closings, sudden price spikes, and abnormal volume patterns in historical stock index data.

---

## 🚀 Features

- 📁 Load index data from CSV (`data/sample_index_data.csv`)
- 🔍 Perform rule-based anomaly detection:
  - Missing values
  - Negative closing prices
  - Sudden spikes in closing values
  - Abnormal volume changes
- 📅 Date range filtering via sidebar
- 📥 Downloadable anomaly report as CSV
- ✅ Clean modular code (rule engine, report generation, and UI separated)

---

## 🛠️ Tech Stack

- Python 3.x  
- Streamlit  
- Pandas  
- Matplotlib / Seaborn (optional for future visualization)

---

## 📂 Project Structure

```

index\_data\_quality\_checker/
│
├── app.py                         # Streamlit dashboard
├── data/
│   └── sample\_index\_data.csv      # Input index data
├── outputs/
│   └── final\_report.csv           # Generated report
├── src/
│   ├── rule\_checks.py             # All anomaly detection rules
│   └── report.py                  # Generates report from rules
└── README.md                      # Project documentation

````

---

## 📸 Sample UI Screenshots

| Raw Data View | Anomaly Report | Final Report Download |
|---------------|----------------|------------------------|
| ✅ Raw CSV Table | ✅ Detected anomalies | ✅ Button to download annotated CSV |

---

## ✅ How to Run

1. **Clone the repository**  
```bash
git clone https://github.com/vaisharma16/index_data_quality_checker.git
cd index_data_quality_checker
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 📈 Sample Data Format

```csv
Date,Index_Name,Closing_Value,Volume
2025-04-16,Nifty 50,21985.08,2877944
2025-04-17,Nifty 50,22465.51,3419138
...
```

---

## 📥 Final Output (`final_report.csv`)

```csv
Anomaly_Type,Date,Index_Name,Closing_Value,Volume
missing_values,2025-05-01,Nifty 50,,2864962
negative_closing,2025-04-26,Nifty 50,-5.0,2974896
sudden_spikes,2025-04-26,Nifty 50,-5.0,2974896
...
```

---

## 📌 Future Improvements

* Allow user to upload their own CSV files
* Add time-series anomaly detection (e.g., Prophet, Isolation Forest)
* Show charts to visualize anomalies
* Deploy on Streamlit Cloud

---

## 🙌 Acknowledgements

Developed by **Vaibhav Sharma**
🔗 [LinkedIn](https://linkedin.com/in/vaibhavsharma16)
---


