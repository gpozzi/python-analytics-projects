import pandas as pd

df_1 = pd.read_csv('datasets/wastestats.csv')
df_2 = pd.read_csv('datasets/2018_2019_waste.csv')
df_3 = pd.read_csv('datasets/energy_saved.csv',skiprows=2)

display(df_1.head(5))
display(df_2.head(5))
display(df_3.head(5))

# Transpose dataframe
df_3 = pd.read_csv('datasets/energy_saved.csv',skiprows=2).T

# Set column names, remove first row
df_3.columns = df_3.iloc[0]
df_3 = df_3.iloc[1:,].reset_index(drop=True)

# Normalize materials column name
df_3 = df_3.rename(columns={"material":"waste_type"})

# Drop "crude_oil saved" column since we don't need this data right now
df_3 = df_3.drop(columns='crude_oil saved')

# Remove " kwh" from "energy_saved
df_3.energy_saved = df_3.energy_saved.str.replace("( ).*","")
df_3


df_2 = pd.read_csv('datasets/2018_2019_waste.csv')
# Renaming columns, standardizing to match df_1 ones, and making them `snake_case` for easier usability
df_2 = df_2.rename(columns={"Waste Type":"waste_type","Total Generated ('000 tonnes)": "total_waste_generated","Total Recycled ('000 tonnes)" : 'total_waste_recycled_tonne',"Year":"year"})

df_2 = df_2.drop(columns=['total_waste_generated'])


df_2['total_waste_recycled_tonne'] = df_2['total_waste_recycled_tonne']*1000
df_2.head(4)

df_1 = pd.read_csv('datasets/wastestats.csv')

# Drop "waste_disposed_of_tonne" and "total_waste_recycled_tonne" columns since we don't need them
df_1 = df_1.drop(columns=['waste_disposed_of_tonne','recycling_rate','total_waste_generated_tonne'])

display(df_1[df_1['year']==2015])

df_new = pd.concat([df_1,df_2])
display(df_new.shape)
df_new.head(5)
list_types = df_new['waste_type'].unique().tolist()

# Create list of relevant materials
list_materials = df_3['waste_type'].unique().tolist()
list_materials.remove('Paper')

# Normalize names
df_new.replace("Plastics", "Plastic",inplace=True)
df_new.replace(['Ferrous metal','Ferrous Metals'], "Ferrous Metal",inplace=True)
df_new.replace(["Non-ferrous Metals",'Non-ferrous metal','Non-ferrous metals'], "Non-Ferrous Metal",inplace=True)

# Select material types that are "glass, plastic, ferrous and non-ferrous metals"
df_new = df_new[df_new['waste_type'].isin(list_materials)]

df_new_final = df_new.merge(df_3,on='waste_type')

annual_energy_savings = df_new_final.set_index('year')
annual_energy_savings.total_waste_recycled_tonne = annual_energy_savings.total_waste_recycled_tonne.astype('int')
annual_energy_savings.energy_saved = annual_energy_savings.energy_saved.astype('int')

annual_energy_savings['total_energy_saved'] = annual_energy_savings['total_waste_recycled_tonne'] * annual_energy_savings['energy_saved']
display(annual_energy_savings.loc[2019])
annual_energy_savings = annual_energy_savings.drop(columns=['total_waste_recycled_tonne','waste_type','energy_saved'])
annual_energy_savings = annual_energy_savings.groupby(['year']).sum()
annual_energy_savings = annual_energy_savings.loc[2015:2019]
annual_energy_savings
