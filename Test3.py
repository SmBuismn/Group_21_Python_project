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

#new

infrastructure_train_data = infrastructure_train_data.astype(float)
gdp_data = gdp_data.astype(float)

# Determine percentage of GDP that is invested in railway infrastructure
infrastructure_gdp = infrastructure_train_data / gdp_data*100

passenger_data = passenger_data.astype(float)
population_data = population_data.astype(float)

# Determine amount of kilometers travelled per passenger
# Note that passenger data is the total amount of kilometers travelled in millions
km_per_passenger = passenger_data / population_data*1000000

#investments comparing with passenger transport dataframe making
df1 = pd.DataFrame(infrastructure_gdp)
df2 = pd.DataFrame(km_per_passenger)

print(df1)
print(df2)

years = df2.columns[:]

'''
for year in years:
    plt.figure()
    for country in df1.index:
        plt.scatter(df2.loc[country, year], df1.loc[country, year], label=country)

    plt.legend()
    plt.show()  

'''

data = []
for year in years:
    for country in df1.index:
        data.append({
            'Year': year,
            'Country': country,
            'Investments': df2.loc[country, year],
            'Passengers': df1.loc[country, year]
        })

# Create an animated scatter plot using Plotly Express
fig = px.scatter(data_frame=data, x='Investments', y='Passengers', animation_frame='Year',
                 color='Country', hover_name='Country', range_x=[0, df2.values.max()],
                 range_y=[0, df1.values.max()], labels={'Investments': 'Investments', 'Passengers': 'Passengers'})

# Customize the layout
fig.update_layout(title='Investments vs. Passengers Over the Years',
                  xaxis_title='Investments', yaxis_title='Passengers')

# Show the plot
fig.show()





