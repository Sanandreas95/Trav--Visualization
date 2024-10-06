import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Key Matrix calculated
# anova_costprice
# anova_sellingprice
# anova_markup



df=pd.read_csv('D:\Project\Project_input\python_test_dataset_flights_6months.csv')
# Identify rows where the booking date is later than the travel date
mask = df['booking_date'] > df['travel_date']

# Swap the dates for these rows
df.loc[mask, ['booking_date', 'travel_date']] = df.loc[mask, ['travel_date', 'booking_date']].values






import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt

# Sample DataFrame (assuming df is your dataset)
# df = pd.read_csv('your_dataset.csv')

# Visualize the distribution of cost_price, markup, and selling_price by journey_type and destination
plt.figure(figsize=(14, 6))

plt.subplot(1, 3, 1)
sns.boxplot(x='journey_type', y='costprice', hue='to_airport', data=df)
plt.title('Cost Price by Journey Type and Destination')

plt.subplot(1, 3, 2)
sns.boxplot(x='journey_type', y='markup', hue='to_airport', data=df)
plt.title('Markup by Journey Type and Destination')

plt.subplot(1, 3, 3)
sns.boxplot(x='journey_type', y='selling_price', hue='to_airport', data=df)
plt.title('Selling Price by Journey Type and Destination')

plt.tight_layout()
plt.show()

# Define the formula for ANOVA
# We'll test if there's a significant effect of journey_type and destination on cost_price, markup, and selling_price

# ANOVA for cost_price
model_cost = ols('costprice ~ C(journey_type) + C(to_airport)', data=df).fit()
anova_cost = sm.stats.anova_lm(model_cost, typ=2)
anova_cost.to_csv(r'D:\Project\Project_output\Anova\ANOVA for cost_price.csv')
print("ANOVA for Cost Price")
print(anova_cost)

# ANOVA for markup
model_markup = ols('markup ~ C(journey_type) + C(to_airport)', data=df).fit()
anova_markup = sm.stats.anova_lm(model_markup, typ=2)
anova_cost.to_csv(r'D:\Project\Project_output\Anova\ANOVA for markup.csv')
print("\nANOVA for Markup")
print(anova_markup)

# ANOVA for selling_price
model_selling = ols('selling_price ~ C(journey_type) + C(to_airport)', data=df).fit()
anova_selling = sm.stats.anova_lm(model_selling, typ=2)
anova_cost.to_csv(r'D:\Project\Project_output\Anova\ANOVA for selling_price.csv')
print("\nANOVA for Selling Price")
print(anova_selling)

