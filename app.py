import streamlit as st
import pandas as pd
import plotly.express as px
from src.report import generate_report
from src.rule_checks import (
    check_missing_values,
    check_negative_closing_values,
    check_sudden_spikes,
    check_volume_spikes
)
import base64

# Page config
st.set_page_config(page_title="📊 Index Data Anomaly Detection", layout="wide")

def get_csv_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="final_report.csv">📥 Download Final Report CSV</a>'

def main():
    st.title("📊 Index Data Anomaly Detection Dashboard")

    # Load data
    data_path = "data/sample_index_data.csv"
    try:
        df = pd.read_csv(data_path)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Closing_Value"] = pd.to_numeric(df["Closing_Value"].astype(str).str.replace(",", ""), errors='coerce')
        df["Volume"] = pd.to_numeric(df["Volume"].astype(str).str.replace(",", ""), errors='coerce')
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return

    # Sidebar Filter

    st.sidebar.header("📅 Filter by Date Range")
    min_date = df["Date"].min()
    max_date = df["Date"].max()
    date_range = st.sidebar.date_input("Select date range:", [min_date, max_date])

    if len(date_range) != 2:
        st.warning("⚠️ Please select both a start and an end date to proceed.")
        return
    start_date, end_date = date_range
    filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]


    st.subheader("📈 Raw Index Data (Filtered)")
    st.dataframe(filtered_df)

    # Plotly Charts
    st.subheader("📊 Interactive Charts")
    fig_close = px.line(filtered_df, x="Date", y="Closing_Value", title="Closing Value Over Time", markers=True)
    st.plotly_chart(fig_close, use_container_width=True)

    fig_volume = px.bar(filtered_df, x="Date", y="Volume", title="Volume Traded Over Time")
    st.plotly_chart(fig_volume, use_container_width=True)

    # Anomaly Detections
    st.subheader("🔍 Anomaly Detection Results")
    st.markdown("**1. Missing Values**")
    missing = check_missing_values(filtered_df)
    st.dataframe(missing)

    st.markdown("**2. Negative Closing Values**")
    negative = check_negative_closing_values(filtered_df)
    st.dataframe(negative)

    st.markdown("**3. Sudden Spikes in Closing Values**")
    spikes = check_sudden_spikes(filtered_df)
    st.dataframe(spikes)

    st.markdown("**4. Unusual Volume Spikes**")
    volume_spikes = check_volume_spikes(filtered_df)
    st.dataframe(volume_spikes)

    # Combine results for download
    final_report_df = pd.concat({
        "missing_values": missing,
        "negative_closing": negative,
        "sudden_spikes": spikes,
        "volume_spikes": volume_spikes
    })
    final_report_df.index.names = ['Anomaly_Type', None]  # name index levels
    final_report_df = final_report_df.reset_index()       # flatten into columns
    #st.markdown(get_csv_download_link(final_report_df), unsafe_allow_html=True)
    st.download_button(
    label="📥 Download Final Report CSV",
    data=final_report_df.to_csv(index=False),
    file_name="final_report.csv",
    mime="text/csv",
    key="download_button"
)


    # Footer
    st.markdown("---")
    st.markdown("<div style='text-align: center; font-size: 14px;'>Made with ❤️ by <b>Vaibhav Sharma</b></div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
