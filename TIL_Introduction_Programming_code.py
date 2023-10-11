import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

prepare_passenger_data = pd.read_csv("passenger_data.csv")
prepare_infrastructure_data = pd.read_csv("InfrastructureInvestments_data.csv")
gdp_data = pd.read_csv("GDP_data.csv")
gdp_per_capita_data = pd.read_csv("GDP_per_capita_data.csv")

# Choose the timeframe you want to consider
start_timeframe = 2000
end_timeframe = 2020

num_of_countries = gdp_data.shape[0]
num_of_columns = gdp_data.shape[1]


passenger_data = pd.DataFrame(columns=gdp_data.columns)
infrastructure_data = pd.DataFrame(columns=gdp_data.columns)

for i in range(num_of_countries):
    passenger_data.loc[i] = ['..' for _ in range(num_of_columns)]
    infrastructure_data.loc[i] = ['..' for _ in range(num_of_columns)]

for i in range(num_of_countries):
    passenger_data.loc[i, "Country"] = gdp_data.loc[i, "Country"]
    infrastructure_data.loc[i, "Country"] = gdp_data.loc[i, "Country"]



for country in gdp_data["Country"]:
    country_index = gdp_data.loc[gdp_data["Country"] == country].index[0]

    for year in gdp_data.columns[1:]:
        if ((prepare_passenger_data["LOCATION"] == country) & 
                                      (prepare_passenger_data["TIME"] == int(year))).any():
            if np.isnan(prepare_passenger_data["Value"].iloc[prepare_passenger_data.loc[(prepare_passenger_data["LOCATION"] == country) & 
                                      (prepare_passenger_data["TIME"] == int(year))].index[0]]) :
                continue
            else:
                passenger_data.loc[country_index,year] = prepare_passenger_data["Value"].iloc[prepare_passenger_data.loc[(prepare_passenger_data["LOCATION"] == country) & 
                                      (prepare_passenger_data["TIME"] == int(year))].index[0]]
        if ((prepare_infrastructure_data["LOCATION"] == country) & 
                                      (prepare_infrastructure_data["TIME"] == int(year))).any():
            if np.isnan(prepare_infrastructure_data["Value"].iloc[prepare_infrastructure_data.loc[(prepare_infrastructure_data["LOCATION"] == country) & 
                                      (prepare_infrastructure_data["TIME"] == int(year))].index[0]]):
                continue
            else:
                infrastructure_data.loc[country_index,year] = prepare_infrastructure_data["Value"].iloc[prepare_infrastructure_data.loc[(prepare_infrastructure_data["LOCATION"] == country) & 
                                        (prepare_infrastructure_data["TIME"] == int(year))].index[0]]



data_empty = {'Country': [], 'Timeframe passenger': [], 'Timeframe infrastructure': []}
country_timeframe = pd.DataFrame(data_empty)

for country in gdp_data["Country"]:
    country_index = gdp_data.loc[gdp_data["Country"] == country].index[0]

    passenger_start = 0
    passenger_stop = 0
    passenger_count = 0

    infrastructure_start = 0
    infrastructure_stop = 0
    infrastructure_count = 0
    
    for year in gdp_data.columns[1:]:
        if passenger_data.loc[country_index,year] != "..":
            if passenger_start == 0:
                passenger_start = int(year)
            passenger_stop = int(year)
            passenger_count += 1

        if infrastructure_data.loc[country_index,year] != "..":
            if infrastructure_start == 0:
                infrastructure_start = int(year)
            infrastructure_stop = int(year)
            infrastructure_count += 1

    if (passenger_stop - passenger_start + 1 != passenger_count or
        infrastructure_stop - infrastructure_start + 1 != infrastructure_count):
        continue

    else:
        new_row = {'Country': country, 'Timeframe passenger': "{}-{}".format(passenger_start,passenger_stop), 'Timeframe infrastructure': "{}-{}".format(infrastructure_start,infrastructure_stop)}
        country_timeframe = country_timeframe.append(new_row, ignore_index=True)

feasible_countries = []

for country in country_timeframe["Country"]:
    country_index = country_timeframe.loc[country_timeframe["Country"] == country].index[0]

    years_timeframe_passenger = country_timeframe["Timeframe passenger"].iloc[country_index].split('-')
    years_timeframe_infrastructure = country_timeframe["Timeframe infrastructure"].iloc[country_index].split('-')

    start_year_passenger = int(years_timeframe_passenger[0])
    end_year_passenger = int(years_timeframe_passenger[1])

    start_year_infrastructure = int(years_timeframe_infrastructure[0])
    end_year_infrastructure = int(years_timeframe_infrastructure[1])


    if (max(start_year_passenger,start_year_infrastructure) <= start_timeframe) & (min(end_year_passenger,end_year_infrastructure) >= end_timeframe):
        feasible_countries.append(country)


for year in gdp_data.columns[1:]:
    if int(year) < start_timeframe or int(year) > end_timeframe:
        gdp_data = gdp_data.drop(year, axis=1)
        gdp_per_capita_data = gdp_per_capita_data.drop(year, axis=1)
        passenger_data = passenger_data.drop(year, axis=1)
        infrastructure_data = infrastructure_data.drop(year, axis=1)

gdp_data = gdp_data[gdp_data['Country'].isin(feasible_countries)]
gdp_per_capita_data = gdp_per_capita_data[gdp_per_capita_data['Country'].isin(feasible_countries)]
passenger_data = passenger_data[passenger_data['Country'].isin(feasible_countries)]
infrastructure_data = infrastructure_data[infrastructure_data['Country'].isin(feasible_countries)]

gdp_data.set_index('Country', inplace=True)
gdp_data = gdp_data.applymap(lambda x: '{:.0f}'.format(float(x)))  # Convert large numbers (e-powers) to normal numbers
gdp_per_capita_data.set_index('Country', inplace=True)
passenger_data.set_index('Country', inplace=True)
infrastructure_data.set_index('Country', inplace=True)





#Infrastructure / GDP
infrastructure_data = infrastructure_data.astype(float)
gdp_data = gdp_data.astype(float)

infrastructure_gdp = infrastructure_data / gdp_data


plt.figure()
for index, row in infrastructure_gdp.iterrows():
    print(row[1])
    plt.plot(row, marker='o',label=f'{index}')

plt.xlabel('Year')
plt.ylabel('Infrastructure as percentage of GDP')

# Add legend and display the plot
plt.legend()
plt.show()






