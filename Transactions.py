
import pandas as pd
import matplotlib.pyplot as plt


df=pd.DataFrame(pd.read_csv("Transactions.csv"))


# Display the first few rows of the DataFrame
print(df.head())


# Summary statistics
print(df.describe())



# Total sales per category
category_sales=df.groupby('category')['quantity'].sum()
print(category_sales)


#Total sales per country
country_sales=df.groupby('country')['price'].sum()
print(country_sales)


# Number of unique customers
print("Number of unique customer:", df['customer_id'].nunique())


# Number of unique products
print("Number of unique products:", df['product_id'].nunique())


# Calculate the total revenue
df['revenue']= df['quantity'] * df['price']
total_revenue=df['revenue'].sum()
print("Total Revenue:", total_revenue)


# Find the most popular products
popular_products=df['product_name'].value_counts()
print("Popular products:\n", popular_products)


# Countrey-wise revenue
country_revenue=df.groupby('country')['revenue'].sum()
print("Country-wise Revenue:\n", country_revenue)


# Category-wise analysis
category_revenue=df.groupby('category')['revenue'].sum()
print("Category-wise Revenue:\n", category_revenue)



# Date-wise revenue
date_revenue = df.groupby('transaction_date')['revenue'].sum()
print("Date-wise Revenue:\n", date_revenue)



#Customer-wise analysis
customer_revenue =df.groupby('customer_id')['revenue'].sum()
print("Customer-wise revenue:\n", customer_revenue)

# Average revenue per customer
average_revenue_per_customer= customer_revenue.mean()
print("Average Revenue per customer:", average_revenue_per_customer)

#Customer with the highest total revenue
highest_revenue_customer= customer_revenue.idxmax()
print("Customer with Highest RevenueP:", highest_revenue_customer)


# Calculate the average price per product
average_price_per_product=df.groupby('product_name')['price'].mean()
print("Average Price per Product:\n", average_price_per_product)

# Most expensive product
most_expensive_product=average_price_per_product.idxmax()
print("Most Expensive Product:", most_expensive_product)

# Cheapest product
cheapest_product = average_price_per_product.idxmin()
print("Cheapest Product:", cheapest_product)


# Category-wise revenue by country
category_country_revenue = df.groupby(['category', 'country'])['revenue'].sum()
print("Category-wise Revenue by Country:\n", category_country_revenue)



# Resample data to monthly frequency
monthly_revenue = df.resample('M', on='transaction_date')['revenue'].sum()
print("Monthly Revenue:\n", monthly_revenue)



import matplotlib.pyplot as plt
import seaborn as sns

# Filter data for a specific category
electronics_data = df[df['category'] == 'Electronics']

# Plot a bar chart for product-wise revenue in Electronics category
plt.figure(figsize=(10, 6))
sns.barplot(x='product_name', y='revenue', data=electronics_data)
plt.title("Product-wise Revenue in Electronics Category")
plt.xlabel("Product Name")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()



#Convert the  'transaction_date' column to datetime
df['transaction_date']=pd.to_datetime(df['transaction_date'])



# Set 'transacion_date' as thhe indexx
df.set_index('transaction_date', inplace=True)



# Resample data to monthly frequency and calculate total sales
monthly_sales=df.resample('M')['price'].sum()



#Plot monthly sales over time
plt.figure(figsize=(10, 6))
monthly_sales.plot()
plt.title('Monthly Total Sales')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.show()

