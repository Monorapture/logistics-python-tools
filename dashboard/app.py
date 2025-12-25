"""
APPLICATION: Supply Chain Control Tower
TYPE: Streamlit Dashboard
AUTHOR: Kilian Sender

DESCRIPTION:
    Interactive dashboard to visualize logistics performance, 
    shipping times, and revenue trends based on the cleaned dataset.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ==============================================================================
# 1. CONFIGURATION & PATHS
# ==============================================================================
st.set_page_config(
    page_title="Supply Chain Tower",
    page_icon="🚛",
    layout="wide"
)

# Robust path handling: Finds the CSV relative to THIS script file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "cleaned_supply_chain_data.csv")

# ==============================================================================
# 2. DATA LOADING (Cached for Performance)
# ==============================================================================
@st.cache_data
def load_data():
    """Loads and preprocesses the CSV data."""
    if not os.path.exists(DATA_FILE):
        st.error(f"CRITICAL ERROR: Data file not found at {DATA_FILE}")
        st.stop()
        
    df = pd.read_csv(DATA_FILE)
    
    # Convert date columns to datetime objects
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['shipping_date'] = pd.to_datetime(df['shipping_date'])
    
    return df

# Load data initially
try:
    df_raw = load_data()
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()


# ==============================================================================
# 3. SIDEBAR & FILTERS
# ==============================================================================
st.sidebar.header('🔍 Filter Options')

# Filter: Region (Market)
all_markets = sorted(df_raw['market'].unique())
selected_market = st.sidebar.multiselect(
    "Select Market/Region",
    options=all_markets,
    default=all_markets
)

# Apply Filters
if not selected_market:
    st.warning("Please select at least one market to display data.")
    st.stop()

df_filtered = df_raw[df_raw['market'].isin(selected_market)]


# ==============================================================================
# 4. MAIN DASHBOARD LAYOUT
# ==============================================================================
st.title("🚛 Supply Chain Control Tower")
st.markdown("---")

# --- SECTION A: KPI METRICS ---
# Calculate Key Metrics based on filtered data
total_sales = df_filtered['sales'].sum()
total_orders = len(df_filtered)
avg_lead_time = df_filtered['actual_shipping_days'].mean()

col1, col2, col3 = st.columns(3)

col1.metric(
    label="💰 Total Revenue",
    value=f"{total_sales:,.2f} €"
)

col2.metric(
    label="📦 Total Orders",
    value=total_orders
)

col3.metric(
    label="⏱️ Avg. Shipping Days",
    value=f"{avg_lead_time:,.1f} Days",
    help="Target: < 5 Days" # Tooltip for context
)

st.markdown("---")

# --- SECTION B: CHARTS ---
chart_col1, chart_col2 = st.columns(2)

# Chart 1: Revenue over Time (Line Chart)
with chart_col1:
    st.subheader("📈 Revenue Trend")
    # Group by month for cleaner visualization
    sales_over_time = df_filtered.resample('M', on='order_date')['sales'].sum().reset_index()
    
    fig_sales = px.line(
        sales_over_time,
        x='order_date',
        y='sales',
        template='plotly_dark',
        markers=True
    )
    fig_sales.update_layout(xaxis_title="Date", yaxis_title="Revenue (€)")
    st.plotly_chart(fig_sales, use_container_width=True)

# Chart 2: Shipping Days Distribution (Histogram)
with chart_col2:
    st.subheader("🚚 Lead Time Distribution")
    fig_hist = px.histogram(
        df_filtered,
        x="actual_shipping_days",
        nbins=20,
        color_discrete_sequence=['#636EFA'],
        template='plotly_dark'
    )
    fig_hist.update_layout(xaxis_title="Days to Ship", yaxis_title="Count of Orders")
    st.plotly_chart(fig_hist, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.caption(f"Data Source: {os.path.basename(DATA_FILE)} | Records displayed: {len(df_filtered)}")