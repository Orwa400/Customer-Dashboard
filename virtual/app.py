import streanlit as st # Create web app with python
import pandas as pd # For data manipulation and analysis
import plotly.express as px # Create interactive visualizations

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
filtered_data = data.copy() # Start with the copy of the original dataset
if selected_country:
    filtered_data = filtered_data[filtered_data["Country"].isin(selected_country)]
if selected_gender:
    filtered_data = filtered_data[filtered_data["Gender"].isin(selected_gender)]

#Display filtered Data
st.subheader("filtered Data") # This section creates a subheader for filtered data and displays the `filtered_data` DataFrame as an interactive table in the Streamlit app.
st.subheader("Filtered Data")  
st.dataframe(filtered_data)

# Age Distribution
# This section generates a histogram to visualize the distribution of customer ages in the filtered dataset.
st.markdown("### Age distribution")
fig_age = px.histogram(filtered_data, x="Age", nbins=10, title="Age Distribution")
st.plotly_chart(fig_age)  # Display the Plotly chart in the Streamlit app.

# Purchase amount by country
# This section generates a bar chart to show the total purchase amount for each country in the filtered dataset.
st.markdown("### Purchsse Amount by Country")
fig_purchase = px.bar(
    filtered_data.groupby("Country")["PurchaseAmount"].sum().reset_index(name="Signups"),
    x="Country", y="Total Purchase Amount", title="Purchase Amount by Country"
)
st.plotly_chart(fig_purchase) # Display the Plotly bar chart in the Streamlit app.

# Sign up trend over time
# Display a line chart showing the trend of customer signups over time, grouped by month
# The data is resampled to aggregate the number of signups monthly, and the result is visualized
st.markdown("### SIgnup Trend")
fig_signup = px.line(
    filtered_data.resample("M", on="SignupDate").size().reset_index(name="Signups"),
    x="SignupDate", y=Signups, title="Signups Over Time"
)
st.plotly_chart(fig_signup)  # Render the line chart in the Streamlit app

# Download filtered data
st.subheader("Download Filtered Data")
csv = filtered_data.to_csv(index=False) # Convert the filtered data to a CSV format string without including the index
st.download_button(
    label="Download CSV",
    data= csv,
    file_name="filtered_customer.csv",
    mime="text/csv",
)

    