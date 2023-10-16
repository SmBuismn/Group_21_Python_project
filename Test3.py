# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

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
infrastructure_gdp = infrastructure_train_data / gdp_data*1000

passenger_data = passenger_data.astype(float)
population_data = population_data.astype(float)

# Determine amount of kilometers travelled per passenger
# Note that passenger data is the total amount of kilometers travelled in millions
km_per_passenger = passenger_data / population_data*1000000

#investments comparing with passenger transport dataframe making
df1 = pd.DataFrame(infrastructure_gdp)
df2 = pd.DataFrame(km_per_passenger)

frames = [df1,df2]
merged_df = df1.merge(df2, left_index=True, right_index=True)

print(merged_df)

# making scatter plot
for col in merged_df.columns:
    plt.scatter(df1[col], df2[col], label=col)
#plt.scatter(merged_df[df1], merged_df[df2])
plt.show()


