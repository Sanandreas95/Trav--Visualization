


import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt

# Key Matrix calculated

# Customer Loyalty
# Avg selling price for loyal vs non Loyal
# Correlation between pricing and repeat business




df=pd.read_csv('D:\Project\Project_input\python_test_dataset_flights_6months.csv')
mask = df['booking_date'] > df['travel_date']
    
    # Swap the dates for these rows
df.loc[mask, ['booking_date', 'travel_date']] = df.loc[mask, ['travel_date', 'booking_date']].values
    
    



output_path = r'D:\Project\Project_output\loyal_customer.csv'

import pandas as pd

# Sample DataFrame (assume df is your dataset)
# df = pd.read_csv('your_data.csv')

# Count the number of bookings per customer
df['BookingCount'] = df.groupby('buyer_id')['buyer_id'].transform('count')


# Define 'loyal customers' as those who have booked more than once
df['LoyalCustomer'] = df['BookingCount'] > 60

# View the updated DataFrame

df.to_csv(r'D:\Project\Project_output\Booking_count.csv')
print(df.head())









# Calculate average selling price for loyal and non-loyal customers
avg_selling_price = df.groupby('LoyalCustomer')['selling_price'].mean()
avg_selling_price.to_csv(r'D:\Project\Project_output\avg_selling_price.csv')
print("Average Selling Price for Loyal vs Non-Loyal Customers:")
print(avg_selling_price)









# Calculate average markup for loyal and non-loyal customers
avg_markup = df.groupby('LoyalCustomer')['markup'].mean()
avg_markup.to_csv(r'D:\Project\Project_output\avg_markup.csv')

print("Average Markup for Loyal vs Non-Loyal Customers:")
print(avg_markup)








# Analyze the correlation between pricing strategies and repeat business
correlation= df[['costprice', 'markup', 'selling_price', 'BookingCount']].corr()
correlation .to_csv(r'D:\Project\Project_output\correlation between pricing strategies and repeat business .csv')

print(" correlation between pricing strategies and repeat business:")
print( correlation)







# Optionally, plot the correlation matrix using Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Between Pricing and Repeat Business')
plt.show()








import statsmodels.api as sm

# Define the independent variables (pricing strategies)
X = df[['costprice', 'markup', 'selling_price']]

# Add a constant to the independent variables
X = sm.add_constant(X)

# Define the dependent variable (repeat business)
y = df['BookingCount']

# Perform the regression analysis
model = sm.OLS(y, X).fit()

# View the regression results
print(model.summary())








plt.figure(figsize=(8,6))
sns.scatterplot(x='selling_price', y='BookingCount', data=df)
plt.title('Selling Price vs Repeat Business')
plt.xlabel('Selling Price')
plt.ylabel('Number of Bookings (Repeat Business)')
plt.show()


plt.figure(figsize=(8,6))
sns.boxplot(x='LoyalCustomer', y='selling_price', data=df)
plt.title('Selling Price for Loyal vs Non-Loyal Customers')
plt.xlabel('Customer Loyalty')
plt.ylabel('Selling Price')
plt.show()




