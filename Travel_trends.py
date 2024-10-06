import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt



# # Key Matrix calculated
# Daily Travel
# Weekly Travel
# Monthly Travel



df=pd.read_csv('D:\Project\Project_input\python_test_dataset_flights_6months.csv')


df['booking_date'] = pd.to_datetime(df['booking_date'], format='%d-%m-%Y')
df['travel_date'] = pd.to_datetime(df['travel_date'], format='%d-%m-%Y')

mask = df['booking_date'] > df['travel_date']

# Swap the dates for these rows
df.loc[mask, ['booking_date', 'travel_date']] = df.loc[mask, ['travel_date', 'booking_date']].values



df = df[df['booking_status'] == 'confirmed']



# Count daily travels
daily_Travel = df.resample('D', on='travel_date').size()
daily_Travel.name = 'No. of Travels'
daily_Travel.to_csv(r'D:\Project\Project_output\daily_Travel.csv')



# Plot daily travels
plt.figure(figsize=(12, 6))
daily_Travel.plot(title='Daily Travel Trend')
plt.xlabel('Date')
plt.ylabel('Number of Travels')
plt.show()






# Travel by Week
Weekly_travel = df.resample('W', on='travel_date').size()
Weekly_travel.name = 'No. of bookings'
Weekly_travel.to_csv(r'D:\Project\Project_output\Weekly_travel.csv')

# Travel by month
monthly_travel = df.resample('M', on='travel_date').size()
monthly_travel.name = 'No. of bookings'
monthly_travel.to_csv(r'D:\Project\Project_output\monthly_travel.csv')


# Plot weekly and monthly travel trends
plt.figure(figsize=(12, 6))
Weekly_travel.plot(label='Weekly Travel Trend')
monthly_travel.plot(label='Monthly Travel Trend')
plt.title('Weekly and Monthly travel Trends')
plt.xlabel('Date')
plt.ylabel('Number of Travels')
plt.legend(loc = 'right')
plt.show()







# Step 5: Deep Dive into Specific Categories

# Group by journey type and plot monthly trends
journey_type_monthly = df.groupby(['journey_type']).resample('M', on='travel_date').size().unstack(0)
journey_type_monthly.to_csv(r'D:\Project\Project_output\journey_type_monthlytravel.csv')
# Plotting
journey_type_monthly.plot(kind='line', figsize=(12, 6), title='Monthly Travel by Journey Type')
plt.xlabel('Month')
plt.ylabel('Number of Travels')
plt.legend()
plt.show()




