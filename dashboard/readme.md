# 🚚 Supply Chain Control Tower (Dashboard)

![Dashboard Preview](./dashboard_preview.png)

> **Interactive Analytics:** A web-based dashboard to visualize logistics performance, delivery times, and revenue trends.
> **Status:** ✅ Active (v1.0)

## 🎯 The Goal
Raw data in CSV files is hard to interpret. This project transforms the cleaned supply chain dataset into an **interactive Streamlit Web Application**.
It empowers logistics managers to answer critical questions in seconds:
* *"How is our revenue developing over time?"*
* *"Which regions have the longest shipping delays?"*
* *"Are we meeting our delivery KPIs?"*

## ⚡ Key Features
* **Real-Time Filtering:** Sidebar controls to slice data by market/region instantly.
* **Smart Caching:** Uses `@st.cache_data` for high-performance data loading.
* **Interactive Visualizations:**
    * 📈 **Revenue Trend:** Zoomable line charts (Plotly) to analyze sales over time.
    * 🚚 **Lead Time Analysis:** Histograms showing the distribution of actual shipping days.
* **KPI "Big Numbers":** Live calculation of Total Sales, Order Count, and Average Lead Time based on active filters.

## 🛠️ Tech Stack
* **Python 3.10+**
* **Streamlit:** For rapid web app development (Frontend + Backend).
* **Plotly Express:** For interactive, responsive charts.
* **Pandas:** For in-memory data manipulation and filtering.

## 🚀 How to Run Locally

1.  Navigate to the dashboard folder:
    ```bash
    cd dashboard
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Launch the application:
    ```bash
    streamlit run app.py
    ```
4.  The dashboard will open automatically in your browser (usually at `http://localhost:8501`).

## 📂 Project Structure
```text
dashboard/
├── app.py                      # Main application logic
├── requirements.txt            # Python dependencies
└── cleaned_supply_chain_data.csv # The dataset (Output from Project B)
