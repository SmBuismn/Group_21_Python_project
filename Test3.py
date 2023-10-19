# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import seaborn as sns
from matplotlib.animation import FuncAnimation
import plotly.express as px

# Import data
passenger_data = pd.read_csv("passenger_new.csv", index_col='Country')
infrastructure_road_data = pd.read_csv("infrastructure_road_new.csv", index_col='Country')
infrastructure_train_data = pd.read_csv("infrastructure_train_new.csv", index_col='Country')
population_data = pd.read_csv("population_new.csv", index_col='Country')
gdp_data = pd.read_csv("gdp_new.csv", index_col='Country')
gdp_per_capita_data = pd.read_csv("GDP_per_capita_new.csv", index_col='Country')

#Setting data right
infrastructure_train_data = infrastructure_train_data.astype(float)
gdp_data = gdp_data.astype(float)
passenger_data = passenger_data.astype(float)
population_data = population_data.astype(float)

# Determine percentage of GDP that is invested in railway infrastructure and km travelled per passenger
infrastructure_gdp = infrastructure_train_data / gdp_data*100
km_per_passenger = passenger_data / population_data*1000000

# Calculate rolling average for each year based on the past 5 years
investments_over_years = infrastructure_gdp.shift(axis=1).rolling(window=5,axis=1, min_periods=1).mean()
passenger_growth = km_per_passenger.pct_change(periods=5, axis=1)*100

# Since the rolling average starts from the fifth year, remove the first 4 years 
for years in investments_over_years.columns[:5]:
    investments_over_years = investments_over_years.drop(years, axis=1)

for years in passenger_growth.columns[:5]:
    passenger_growth = passenger_growth.drop(years, axis=1)

#make new dataframes
df1 = pd.DataFrame(investments_over_years)
df2 = pd.DataFrame(passenger_growth)

years = df2.columns[:]

data = []
for year in years:
    for country in df1.index:
        data.append({
            'Year': year,
            'Country': country,
            'Investments': df1.loc[country, year],
            'Passengers': df2.loc[country, year]
        })


# Scatter plot
fig = px.scatter(data_frame=data, x='Investments', y='Passengers', animation_frame='Year', size='Investments',
                 color='Country', hover_name='Country', range_x=[0, df1.values.max()],
                 range_y=[df2.values.min(), df2.values.max()], labels={'Investments': 'Investments', 'Passengers': 'Passengers'},)

# Layout
fig.update_layout(title='Investments vs. Passengers Over the Years',
                  xaxis_title='Investments in railway infrastructure corrected by GDP ', yaxis_title='Kilometers traveled per passengers')

# Show the plot
fig.show()


#The figure above shows the relation of investments in railway infrastructure (corrected by GDP) and the amount of kilometers travelled per passenger. 
#Every year from 2005 onwards, we look at the investments made in the 5 years before and look at what the impact has been on the travelled kilometers, for each country. 
#In this way, we want to analyze if the investments in railway lead to more train passengers. 
#As we look at the outcome of the graphs, we see that it not shows what we expected, meaning that the investments in the long term do not seem to increase over a long period. 
#This can have different reasons, for instance in this graph we do not look at the investments in other segments like air transportation and road transportation.
