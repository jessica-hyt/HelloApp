import streamlit as st

st.title("Retail Business Dashboard")

st.header("Manager Input Section")

st.write("Please enter the monthly sales target and select the region.")

sales_target = st.number_input("Enter Monthly Sales Target in (USD):", value = 0.0)
Region = st.selectbox("Select Region", ["North", "East", "South", "West", "Central"])

st.button("Submit")
