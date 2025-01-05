import streanlit as st
import pandas as pd
import plotly.express as px

# load data
@st.cache
def load_data():
    return pd.read_csv("data/customers.csv", parse_dates=["SignupDate"])

data = load_data()

#Title and description
st.title("Customer Data Management Dashboard")
st.markdown("Analyze and manage customer data with interactive visualizations")

# Sidebar filters
st.sidebar.header("Filter Options")
selected_country = st.sidebar.multiselect("Country", data["Country"].unique())
selected_gender = st.sidebar.multiselect("Gender", data["Gender"].unique())

# Apply Filters
filtered_data = data.copy()
if selected_country:
    filtered_data = filtered_data[filtered_data["Country"].isin(selected_country)]
if selected_gender:
    filtered_data = filtered_data[filtered_data["Gender"].isin(selected_gender)]

