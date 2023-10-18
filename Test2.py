import pandas as pd

gdp_per_capita_data=pd.read_csv('gdp_per_capita_new.csv', index_col='Country')
gdp_data=pd.read_csv('gdp_new.csv', index_col='Country')
infrastructure_road_data=pd.read_csv('Infrastructure_road_new.csv', index_col='Country')
infrastructure_train_data=pd.read_csv('infrastructure_train_new.csv', index_col='Country')
population_data=pd.read_csv('population_new.csv', index_col='Country')
passenger_data=pd.read_csv('passenger_new.csv', index_col='Country')

infrastructure_road_data.head()
infrastructure_train_data.head()
population_data.head()
passenger_data.head()
gdp_per_capita_data.head()
gdp_data.head()

infrastructure_road_data = infrastructure_road_data.loc[:, '2000':'2020'].mean(axis=1)
infrastructure_road_data = infrastructure_road_data.drop(columns=range(2000, 2021))
infrastructure_road_mean = pd.DataFrame({'Average investments in road infrastructure': infrastructure_road_data})

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
print(infrastructure_road_mean.index)

dataframes_to_be_merged = [gdp_mean, gdp_per_capita_mean, population_mean, passenger_mean, infrastructure_road_mean, infrastructure_train_mean]
descriptive_table = pd.concat(dataframes_to_be_merged, axis=1).reset_index(drop=True)
print(descriptive_table)

#gdp=gdp_mean.append(gdp_per_capita_mean)
#gdp_mean.shape, gdp_per_capita_mean.shape, gdp.shape

#gdp_pop=gdp.append(population_mean)
#gdp.shape, population_mean.shape, gdp_pop.shape

#gdp_pop_pas=gdp_pop.append(passenger_mean)
#gdp_pop.shape, passenger_mean.shape, gdp_pop_pas.shape

#gdp_pop_pas_invr=gdp_pop_pas.append(infrastructure_road_mean)
#gdp_pop_pas.shape, infrastructure_road_mean.shape, gdp_pop_pas_invr.shape

#gdp_pop_pas_invr_invt = gdp_pop_pas_invr.append(infrastructure_train_mean)
#gdp_pop_pas_invr.shape, infrastructure_train_mean.shape, gdp_pop_pas_invr.shape
#print(gdp_pop_pas_invr_invt)

#calculate mean of investments





#GDPInvPop=GDPInv.append(Population)
#GDPInv.shape, Population.shape, GDPInvPop.shape

#GDPInvPopPas = GDPInvPop.append(Passengers)
#GDPInvPop.shape, Passengers.shape, GDPInvPopPas.shape

#print(GDPInvPopPas)