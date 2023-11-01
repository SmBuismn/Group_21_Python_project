import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Import data
world_map = gpd.read_file("ne_110m_admin_0_countries.shp")   # world map data
gdp_data = pd.read_csv("gdp_new.csv")   # GDP per capita data
passengers_data = pd.read_csv("passenger_new.csv")
population_data = pd.read_csv("population_new.csv")
infrastructure_data = pd.read_csv("infrastructure_train_new.csv")

# Rename index of countries in world map data
world_map = world_map.rename(columns={"SOV_A3": "Country"})

change_names_dict = {"AU1": "AUS", "GB1": "GBR", "FI1": "FIN", "FR1": "FRA"}

world_map["Country"] = world_map["Country"].replace(change_names_dict)

# Print the updated world_map DataFrame
print(world_map)

# Adding column
world_map['has_value'] = world_map['Country'].isin(gdp_data['Country'])

# Merge data
gdp_world_map = world_map.merge(gdp_data, on="Country")
passenger_world_map = world_map.merge(passengers_data, on="Country")
population_world_map = world_map.merge(population_data, on="Country")
infrastructure_world_map = world_map.merge(infrastructure_data, on="Country")

# First individual plot
fig1, ax1 = plt.subplots(figsize=(6, 4))
world_map[world_map['has_value'] == True].plot(color='green', ax=ax1)
world_map[world_map['has_value'] == False].plot(color='lightgray', ax=ax1)
ax1.set_title('Available countries')
ax1.axis('off')
plt.show()


# 2x2 subplot
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

average_gdp = gdp_world_map.loc[:, '1999':'2019'].mean(axis=1)
average_passenger = passenger_world_map.loc[:, '1999':'2019'].mean(axis=1)
average_population = population_world_map.loc[:, '1999':'2019'].mean(axis=1)
average_infrastructure = infrastructure_world_map.loc[:, '1999':'2019'].mean(axis=1)

gdp_world_map.plot(column=average_gdp, cmap='Greens', linewidth=0.8, ax=ax[0, 0], edgecolor='0.8', legend=True)
world_map[world_map['has_value'] == False].plot(color='lightgray', ax=ax[0, 0])

passenger_world_map.plot(column=average_passenger, cmap='Greens', linewidth=0.8, ax=ax[0, 1], edgecolor='0.8', legend=True)
world_map[world_map['has_value'] == False].plot(color='lightgray', ax=ax[0, 1])

population_world_map.plot(column=average_population, cmap='Greens', linewidth=0.8, ax=ax[1, 0], edgecolor='0.8', legend=True)
world_map[world_map['has_value'] == False].plot(color='lightgray', ax=ax[1, 0])

infrastructure_world_map.plot(column=average_infrastructure, cmap='Greens', linewidth=0.8, ax=ax[1, 1], edgecolor='0.8', legend=True)
world_map[world_map['has_value'] == False].plot(color='lightgray', ax=ax[1, 1])

# Set titles and turn off axis for subplots
ax[0, 0].set_title('GDP')
ax[0, 0].axis('off')

ax[0, 1].set_title('Passenger')
ax[0, 1].axis('off')

ax[1, 0].set_title('Population')
ax[1, 0].axis('off')

ax[1, 1].set_title('Infrastructure')
ax[1, 1].axis('off')

plt.show()

'''


world_map[world_map['has_value'] == True].plot(color='green', ax=ax)
world_map[world_map['has_value'] == False].plot(color='lightgray', ax=ax)

# Plot the figure
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

gdp_world_map.plot(column='2011', cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
world_map[world_map['has_value'] == False].plot(color='lightgray', ax=ax)

passenger_world_map.plot(column='2011', cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
world_map[world_map['has_value'] == False].plot(color='lightgray', ax=ax)

population_world_map.plot(column='2011', cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
world_map[world_map['has_value'] == False].plot(color='lightgray', ax=ax)

infrastructure_world_map.plot(column='2011', cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
world_map[world_map['has_value'] == False].plot(color='lightgray', ax=ax)

ax.set_title('Countries with available data')
ax.axis('off')

plt.show()

'''