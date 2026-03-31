import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('cleaned_data.csv')
st.title('Retail Store Sales Analysis')
st.header('Dataset Preview')
st.dataframe(df.head())
st.header('Basic Statistics')
st.write(df.describe())
st.header('Top Selling Products')
top_selling_products = df.groupby('Item')['Quantity'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_selling_products)
st.header('Revenue by Store Location')
revenue_by_store = df.groupby('Location')['Total Spent'].sum().sort_values(ascending=False)
st.bar_chart(revenue_by_store)
st.header('Sales Over Time')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
sales_over_time = df.groupby(df['Transaction Date'].dt.date)['Total Spent'].sum()
st.line_chart(sales_over_time)
st.header('Conclusions')
st.write(''' 
1. The top selling products based on quantity.
2. The store locations contributing the most revenue.
3. The trends in sales over time.
''')