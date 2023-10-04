import pandas as pd
import numpy as np

prepare_passenger_data = pd.read_csv("passenger_data.csv")
prepare_infrastructure_data = pd.read_csv("InfrastructureInvestments_data.csv")
gdp_data = pd.read_csv("GDP_data.csv")
gdp_per_capita_data = pd.read_csv("GDP_per_capita_data.csv")

#print(passenger_data)
#print(infrastructure_data)
print(gdp_data)
#print(gdp_per_capita_data)

passenger_data = pd.DataFrame(columns=gdp_data.columns)
infrastructure_data = pd.DataFrame(columns=gdp_data)


