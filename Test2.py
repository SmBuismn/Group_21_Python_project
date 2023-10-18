import pandas as pd

#import csv files and store them with a fitting name
gdp_per_capita_data=pd.read_csv('gdp_per_capita_new.csv', index_col='Country')
gdp_data=pd.read_csv('gdp_new.csv', index_col='Country')
infrastructure_train_data=pd.read_csv('infrastructure_train_new.csv', index_col='Country')
population_data=pd.read_csv('population_new.csv', index_col='Country')
passenger_data=pd.read_csv('passenger_new.csv', index_col='Country')

#check if the data is imported correctly
infrastructure_train_data.head()
population_data.head()
passenger_data.head()
gdp_per_capita_data.head()
gdp_data.head()

#Calculate average over the 20 years in a new column, and then drop all original data
#except for the generated column containing the average.
#Also give a fitting name to this new column. This is repeated for all relevant input data.

infrastructure_train_data = infrastructure_train_data.loc[:, '2000':'2020'].mean(axis=1)
infrastructure_train_data = infrastructure_train_data.drop(columns=range(2000, 2021))
infrastructure_train_mean = pd.DataFrame({'Average investments in train infrastructure': infrastructure_train_data})

population_data = population_data.loc[:, '2000':'2020'].mean(axis=1)
population_data = population_data.drop(columns=range(2000, 2021))
population_mean = pd.DataFrame({'Average population': population_data})

passenger_data = passenger_data.loc[:, '2000':'2020'].mean(axis=1)
passenger_data = passenger_data.drop(columns=range(2000, 2021))
passenger_mean = pd.DataFrame({'Average passengers': passenger_data})

gdp_data = gdp_data.loc[:, '2000':'2020'].mean(axis=1)
gdp_data = gdp_data.drop(columns=range(2000, 2021))
gdp_mean = pd.DataFrame({'Average GDP': gdp_data})

gdp_per_capita_data = gdp_per_capita_data.loc[:, '2000':'2020'].mean(axis=1)
gdp_per_capita_data = gdp_per_capita_data.drop(columns=range(2000, 2021))
gdp_per_capita_mean = pd.DataFrame({'Average GDP per capita': gdp_per_capita_data})

#Check if all the dataframes have the same index because
#this is mandatory to be able to perform a concatenation
print(gdp_per_capita_mean.index)
print(gdp_mean.index)
print(passenger_mean.index)
print(population_mean.index)
print(infrastructure_train_mean.index)

#Merge all the dataframes for all the means by first adding them to a list and then concatenating them
dataframes_to_be_merged = [gdp_mean, gdp_per_capita_mean, population_mean, passenger_mean, infrastructure_train_mean]
descriptive_table = pd.concat(dataframes_to_be_merged, axis=1)
descriptive_table = descriptive_table.reset_index()
descriptive_table = descriptive_table.rename(columns={'index': 'Country'})
print(descriptive_table)
