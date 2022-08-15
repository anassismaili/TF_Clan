import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
import random as rd
#Read the data
print("=========== Raw_house Data =========================")
raw_house = pd.read_csv('raw_house_data.csv')
print(raw_house.head(10))
#Columns
print("============ Columns ================")
col_raw = raw_house.columns
#print(col_raw)
#Calculate the missing values
missV = raw_house.isna().sum()
print(missV)
raw_houseHoa = raw_house['HOA']
print(raw_houseHoa)
#describe the records
raw = raw_house.describe()
print(raw)

rsh = raw_house.hist(bins = 60, figsize=(20,10))
#plt.show()
#replace the string None values by None
print("============ Replace string None by None value =============")
raw_house['garage'].replace('None', np.nan, inplace=True)
raw_house['bathrooms'].replace('None', np.nan, inplace=True)
raw_house['sqrt_ft'].replace('None', np.nan, inplace=True)
raw_house['HOA'].replace('None', np.nan, inplace=True)
#print(raw_house)
print("*****************************************************")
print(raw_house['HOA'].sort_values().unique())
print("*****************************************************")

print(len(raw_house['HOA'].sort_values().unique()))
print("*****************************************************")
missV2 = raw_house.isna().sum()
print(missV2)
ty=raw_house.dtypes
print(ty)
raw_house["sqrt_ft"] = raw_house.sqrt_ft.astype(float)
raw_house["bathrooms"] = raw_house.bathrooms.astype(float)
raw_house["garage"] = raw_house.garage.astype(float)
for HOA in raw_house:
  print(raw_house['HOA'].unique())
raw_house['HOA'] = raw_house['HOA'].replace(',','', regex=True)
raw_house['HOA'] = raw_house.HOA.astype(float)
ty1=raw_house.dtypes
print(ty1)
valu_cou = raw_house['HOA'].value_counts()
print(valu_cou)
valu_cou1 = raw_house['sqrt_ft'].value_counts()
print(valu_cou1)
msno.matrix(raw_house)
#plt.show()
raw_house['HOA'] = raw_house['HOA'].replace(np.nan,'Not applicable', regex=True)
print(raw_house['HOA'])
missV2 = raw_house.isna().sum()
print(missV2)
max = raw_house.max(axis = 0)
print(max)

min = raw_house.min(axis = 0)
print(min)
for i in range(10):
    V_lot_acres = rd.uniform(1, 2154)
    raw_house['lot_acres'] = raw_house['lot_acres'].replace(np.nan, V_lot_acres, regex=True)

for i in range(6):
    V_bathrooms = rd.randint(0, 6)
    raw_house['bathrooms'] = raw_house['bathrooms'].replace(np.nan, V_bathrooms, regex=True)

for i in range(56):
    V_sqrt_ft = rd.uniform(1100, 22408)
    raw_house['sqrt_ft'] = raw_house['sqrt_ft'].replace(np.nan, V_sqrt_ft, regex=True)

for i in range(7):
    V_garage = rd.randint(0, 7)
    raw_house['garage'] = raw_house['garage'].replace(np.nan, V_garage, regex=True)

for i in range(25):
    V_fireplaces = rd.uniform(0, 25)
    raw_house['fireplaces'] = raw_house['fireplaces'].replace(np.nan, V_fireplaces, regex=True)

print(raw_house['lot_acres'].head(50))
missV3 = raw_house.isna().sum()
print(missV3)

z_lot= raw_house[raw_house['lot_acres']==0]
print(len(z_lot))