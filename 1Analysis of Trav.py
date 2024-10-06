import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Key Matrix calculated
# Overall Correlation
# Daily bookings
# Weekly Bookings
# Monthly Bookings






df=pd.read_csv('D:\Project\Project_input\python_test_dataset_flights_6months.csv')


print(df.head())


df['booking_date'] = pd.to_datetime(df['booking_date'], format='%d-%m-%Y')
df['travel_date'] = pd.to_datetime(df['travel_date'], format='%d-%m-%Y')


# Identify rows where the booking date is later than the travel date
mask = df['booking_date'] > df['travel_date']

# Swap the dates for these rows
df.loc[mask, ['booking_date', 'travel_date']] = df.loc[mask, ['travel_date', 'booking_date']].values


df.to_csv(r'D:\Project\Project_output\datecorrecxteddf.csv')




df.set_index('booking_date', inplace=True)

daily_bookings = df.resample('D').size()
daily_bookings.name = 'No. of bookings'
total_sum = daily_bookings.sum()

# Append the sum as a new row
daily_bookings.loc['Total'] = total_sum
print(daily_bookings)
daily_bookings.to_csv(r'D:\Project\Project_output\daily_bookings.csv')





Weekly_bookings = df.resample('W').size()
Weekly_bookings.name = 'No. of bookings'
total_sum = Weekly_bookings.sum()

# Append the sum as a new row
Weekly_bookings.loc['Total'] = total_sum
print(Weekly_bookings)
Weekly_bookings.to_csv(r'D:\Project\Project_output\Weekly_bookings.csv')








Monthly_bookings = df.resample('M').size()
Monthly_bookings.name = 'No. of bookings'
total_sum = Monthly_bookings.sum()

# Append the sum as a new row
Monthly_bookings.loc['Total'] = total_sum
print(Monthly_bookings)
Monthly_bookings.to_csv(r'D:\Project\Project_output\Monthly_bookings.csv')



num_cols = df.select_dtypes(include=['number'])

# Calculate correlation matrix for numerical columns
correlation_matrix = num_cols.corr()
correlation_matrix.to_csv(r'D:\Project\Project_output\correlation_matrix.csv')

print("Correlation matrix:\n", correlation_matrix)





import seaborn as sns
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('correlation_matrix ')
plt.show()





