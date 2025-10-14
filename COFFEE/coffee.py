import pandas as pd

df = pd.read_csv("C:\\Users\\apues\\Downloads\\archive (25)\\Coffe_sales.csv")

#Data Cleaning
df = df.dropna()
df['Date'] = pd.to_datetime(df['Date'])
df = df.rename(columns={'Cash Type': 'cash_type'})

#Data Analysis
#value = df['coffee_name'].value_counts()
#print(value)

#val = df['cash_type'].value_counts()
#print(val)

#total_sum = df.groupby('coffee_name', as_index=True)['money'].sum()
#print(total_sum)

#total_date = df.groupby('Date', as_index=False)['money'].sum()
#print(total_date)

top_5 = df.groupby('coffee_name', as_index=False)['money'].sum().sort_values(by='money', ascending=False).head(5)
print("\n--- Top 5 Best-Selling Coffees ---")
print(top_5)

total_revenue = df['money'].sum()
print("\n--- Total Revenue ---")
print("₱{:.2f}".format(total_revenue))