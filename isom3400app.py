# business_app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Business Data Dashboard")

# Introduction text
st.write("This dashboard helps visualize sales data over time.")


# Sample data
date_rng = pd.date_range(start='1/1/2023', end='12/31/2023', freq='ME')
df = pd.DataFrame(date_rng, columns=['date'])
df['sales'] = np.random.randint(100, 500, size=(len(date_rng)))

# Data visualization with Streamlit
st.subheader("Monthly Sales Data")
st.line_chart(df.set_index('date'))

# Adding a slider for user input
sales_threshold = st.slider("Sales threshold", 100, 500, 300)

# Filtering and displaying data based on user input
filtered_data = df[df['sales'] >= sales_threshold]
st.write(f"Months with sales above {sales_threshold}")
st.write(filtered_data)

import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration & Title
st.set_page_config(page_title="Simple Data App", layout="centered")
st.title("📊 Interactive Sales Dashboard")
st.write("Adjust the controls in the sidebar to update the chart and data.")

# 2. Sidebar Inputs
st.sidebar.header("Filter Options")
num_days = st.sidebar.slider("Number of days", min_value=7, max_value=90, value=30)
category = st.sidebar.selectbox("Product Category", ["Electronics", "Clothing", "Home Goods"])

# 3. Generate Sample Data
np.random.seed(42)
dates = pd.date_range(end=pd.Timestamp.today(), periods=num_days)
sales = np.random.randint(100, 500, size=num_days)
df = pd.DataFrame({"Date": dates, "Sales ($)": sales, "Category": category})

# 4. Display Key Metrics
col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${df['Sales ($)'].sum():,}")
col2.metric("Average Daily Sales", f"${df['Sales ($)'].mean():.2f}")

# 5. Interactive Chart & Data Table
st.subheader(f"{category} Sales Trend")
st.line_chart(df.set_index("Date")["Sales ($)"])

if st.checkbox("Show raw data table"):
    st.dataframe(df, use_container_width=True)
