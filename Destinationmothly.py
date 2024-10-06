import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt


# Key Matrix Calculated
# Destination count season wise/month wise



df=pd.read_csv('D:\Project\Project_input\python_test_dataset_flights_6months.csv')


df['booking_date'] = pd.to_datetime(df['booking_date'], format='%d-%m-%Y')
df['travel_date'] = pd.to_datetime(df['travel_date'], format='%d-%m-%Y')

mask = df['booking_date'] > df['travel_date']

# Swap the dates for these rows
df.loc[mask, ['booking_date', 'travel_date']] = df.loc[mask, ['travel_date', 'booking_date']].values

df.set_index('travel_date', inplace=True)

df = df[df['booking_status'] == 'confirmed']




# Count the number of travels to each airport
airport_counts = df['to_airport'].value_counts()
airport_counts.to_csv(r'D:\Project\Project_output\airport_counts.csv')









# Identify the top 10 airports
top_airports = airport_counts.nlargest(10).index


destination_counts = df['to_airport'].value_counts()

# Plot top 10 most popular destinations
destination_counts.head(10).plot(kind='bar', title='Top 10 Most Popular Destinations')
plt.ylabel('Number of Bookings')
plt.show()







# Filter the DataFrame to include only top 10 airports
top_df = df[df['to_airport'].isin(top_airports)]

# Aggregate weekly and monthly data
weekly_counts = top_df.groupby('to_airport').resample('W').size().unstack(level=0)
weekly_counts.to_csv(r'D:\Project\Project_output\weekly_counts.csv')
monthly_counts = top_df.groupby('to_airport').resample('M').size().unstack(level=0)
monthly_counts.to_csv(r'D:\Project\Project_output\monthly_counts.csv')




plt.figure(figsize=(14, 7))

# Weekly counts plot
plt.subplot(1, 2, 1)
weekly_counts.plot(ax=plt.gca())  # Using `gca` to specify the current axes
plt.title('Weekly Travel Counts for Top 10 Airports')
plt.ylabel('Number of Travels')
plt.xlabel('Date')
plt.legend(title='Airports', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# Monthly counts plot
plt.subplot(1, 2, 2)
monthly_counts.plot(ax=plt.gca())
plt.title('Monthly Travel Counts for Top 10 Airports')
plt.ylabel('Number of Travels')
plt.xlabel('Date')
plt.legend().set_visible(False)  # Hide legend here as it's the same as the left plot
plt.grid(True)

plt.tight_layout()
plt.show()
