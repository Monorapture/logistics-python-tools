# 🚚 Supply Chain Control Tower (Dashboard)

![Dashboard Preview](dashboard_preview.png)

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

## 🚀 How to Run

1.  **Install dependencies:**
    Navigate to the root of the repository:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Launch the application:**
    You can run the dashboard from the root folder:
    ```bash
    streamlit run dashboard/app.py
    ```

3.  **Access:**
    The dashboard will open automatically in your browser (usually at `http://localhost:8501`).