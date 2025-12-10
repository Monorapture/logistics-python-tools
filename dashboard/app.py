import streamlit as st
import pandas as pd
import plotly.express as px

# 1. PAGE CONFIG (Muss immer oben stehen)
st.set_page_config(
    page_title="Supply Chain Tower",
    page_icon="🚛",
    layout="wide"
)

# 2. TITEL & HEADER
st.title("🚛 Supply Chain Control Tower")
st.markdown("---") #Trennlinie

# 3. DATEN LADEN (Cached)
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_supply_chain_data.csv")
    
    # KORREKTUR HIER: Runde Klammern (Funktion) und df[...] (Spalte)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['shipping_date'] = pd.to_datetime(df['shipping_date'])
    return df

df = load_data()

st.sidebar.header('🔍 Filter Options')

# Filter 1: Region (Market)
# Wir holen uns alle einzigartigen Regionen aus der Spalte 'market'
all_markets = sorted(df['market'].unique())
selected_market = st.sidebar.multiselect(
    "Select Market/Region",
    options = all_markets,
    default = all_markets # Standardauswahl (alle)
)

# Filter anwenden: Wir filtern den DataFrame basierend auf der Auswahl
df_filtered = df[df['market'].isin(selected_market)]

# --- KPI SECTION (Die großen Zahlen) ---
# Wir berechnen die Kennzahlen basierend auf den GEFILTERTEN Daten
total_sales = df_filtered['sales'].sum()
total_orders = len(df_filtered)
avg_lead_time = df_filtered['actual_shipping_days'].mean()

# Layout 3: Spalten nebeneinander
kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric(
    label ='💰 Total Revenue',
    value = f'{total_sales:,.2f}€',
    delta = 'Global Sales' # Kleiner Text drunter
    )

kpi2.metric(
    label = "📦 Total Orders",
    value = total_orders
    )

kpi3.metric(
    label = '⏱️ Avg. Shipping Days',
    value = f'{avg_lead_time:,.1f} Days',
    delta_color = 'inverse' # Rot wäre schlecht (hier neutral)
    )

st.markdown('---') # Trennlinie

# Layout 2: Spalten für Grafiken
chart_col1, chart_col2, = st.columns(2)

# Chart 1: Umsatz über Zeit (Line Chart)
# Wir gruppieren nach Datum (Monat)
sales_over_time = df_filtered.resample('M', on='order_date')['sales'].sum().reset_index()

fig_sales = px.line(
    sales_over_time,
    x='order_date',
    y='sales',
    title='📈 Revenue Trend over Time',
    template='plotly_dark' # Dunkles Design
)

chart_col1.plotly_chart(fig_sales, use_container_width=True)

# Chart 2: Lieferzeit Verteilung (Histogram)
fig_days = px.histogram(
    df_filtered,
    x='actual_shipping_days',
    nbins=20,
    title='🚚 Distribution of Shipping Days',
    color_discrete_sequence=['#00CC96'], # Nices Grün
    template='plotly_dark'
) 

chart_col2.plotly_chart(fig_days, use_container_width=True)

# --- Daten Tabelle (Unten zum Aufklappen) ---
with st.expander('📂 View Raw Data'):
    st.dataframe(df_filtered)