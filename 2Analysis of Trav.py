import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Key Matrix calculated
# Destination counts and Popular destinations
# Monthly Travels




df=pd.read_csv('D:\Project\Project_input\python_test_dataset_flights_6months.csv')


print(df.head())


df['booking_date'] = pd.to_datetime(df['booking_date'], format='%d-%m-%Y')
df['travel_date'] = pd.to_datetime(df['travel_date'], format='%d-%m-%Y')

# Identify rows where the booking date is later than the travel date
mask = df['booking_date'] > df['travel_date']

# Swap the dates for these rows
df.loc[mask, ['booking_date', 'travel_date']] = df.loc[mask, ['travel_date', 'booking_date']].values







df.set_index('booking_date', inplace=True)

daily_bookings = df.resample('D').size()
total_sum = daily_bookings.sum()

# Append the sum as a new row
daily_bookings.loc['Total'] = total_sum
print(daily_bookings)



Monthly_bookings = df.resample('M').size()
total_sum = Monthly_bookings.sum()

# Append the sum as a new row
Monthly_bookings.loc['Total'] = total_sum
print(Monthly_bookings)



num_cols = df.select_dtypes(include=['number'])

# Calculate correlation matrix for numerical columns
correlation_matrix = num_cols.corr()


print("Correlation matrix:\n", correlation_matrix)


destination_counts = df['to_airport'].value_counts()

# Plot top 10 most popular destinations
destination_counts.head(10).plot(kind='bar', title='Top 10 Most Popular Destinations')
plt.ylabel('Number of Bookings')
plt.show()






# # Resample data to analyze monthly revenue
# monthly_revenue = df.resample('M')['Price'].sum()

# # Plot monthly revenue
# plt.figure(figsize=(10,6))
# monthly_revenue.plot()
# plt.title('Monthly Revenue Trend')
# plt.ylabel('Total Revenue')
# plt.show()










# grpedit=df.groupby(['to_airport','payment_method','channel_of_booking'])['travel_date'].sum
# print(grpedit)


# destin=df.groupby("to_airport").count()
# print(destin)




grpedit=df.groupby(['to_airport','payment_method','channel_of_booking','travel_date'])

# webbooking=grpedit.get_group('Web','')
# print(webbooking)







df.set_index('travel_date', inplace=True)

Monthly_travel = df.resample('M').size()
total_sum = Monthly_travel.sum()

# Append the sum as a new row
Monthly_travel.loc['Total'] = total_sum
print(Monthly_travel)





# # Get cancellations over time
# cancellations = df[df['Cancellation'] == True].resample('M').size()

# # Plot the cancellations trend
# cancellations.plot(title='Monthly Cancellations')
# plt.ylabel('Number of Cancellations')
# plt.show()