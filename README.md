This project provides an interactive web application built with Streamlit to analyze and manage customer data. The dashboard allows users to explore customer demographics, purchase behavior, and trends over time. Users can filter and visualize the data in different ways and also download the filtered dataset.

Features
Filter Options: Users can filter the customer data by country and gender.
Visualizations:
Age Distribution: Displays the distribution of customer ages.
Signups Over Time: A line chart showing the signup trend over time.
Purchase Amount by Country: A bar chart showing the total purchase amount per country.
Download Filtered Data: Users can download the filtered dataset in CSV format.

Technologies Used
Python: The programming language used for the backend.
Streamlit: A framework to create the interactive dashboard.
Plotly: Used for creating interactive charts.
Pandas: For data manipulation and analysis.

Installation
To run this project locally, follow these steps:

1. Clone the repository
git clone https://github.com/yourusername/Customer_Dashboard.git
cd Customer_Dashboard

2. Set up a virtual environment
You can create and activate a virtual environment to keep your dependencies isolated:
For Windows:
python -m venv virtual
.\virtual\Scripts\activate
For macOS/Linux:
python3 -m venv virtual
source virtual/bin/activate

3. Run the Streamlit app
To start the application, run:
streamlit run app.py

File Structure
Customer_Dashboard/
│
├── app.py               # Main script for the Streamlit app
├── assets/              # Folder containing images and other assets
├── data/                # Folder containing the 'customers.csv' file
├── virtual/             # Virtual environment folder
├── .gitignore           # Git ignore file

CSV Data Structure
The customers.csv file contains the following columns:
SignupDate: The date the customer signed up.
Country: The country where the customer resides.
Gender: The gender of the customer.
Age: The age of the customer.
PurchaseAmount: The total amount spent by the customer.

Checkout the live app here 
[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)]([https://your-app-url](https://customer-dashboard.streamlit.app/))



