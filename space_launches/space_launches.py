import pandas as pd
import numpy as np

# Loading relevant dataframes

df_1 = pd.read_csv('datasets/SO-space.csv')
display(df_1.head(4))
df_2 = pd.read_csv('datasets/company_info.csv')
display(df_2.head(4))
df_3 = pd.read_csv('datasets/JV-space.csv')
display(df_3.head(4))

# Remotion of all companies that don't build rockets
df_2 = df_2[df_2['Tech Type'].str.contains("Rocket")]

# Normalizing df_3 data
df_3=df_3.rename(columns={"Launch Cost":"Launch Cost ($M)","Payload (tons)":"Payload (kg)","Price ($/ton)":"Price ($/kg)"})
df_3['Launch Cost ($M)']=df_3['Launch Cost ($M)'].str.replace(',','').astype(int)
# Dollars to millions of dollars
df_3['Launch Cost ($M)']=df_3['Launch Cost ($M)']/1000000
# Price in $/tons to $/kg
df_3['Price ($/kg)']=df_3['Price ($/kg)']/1000
# Paylod: tons to kg
df_3['Payload (kg)']=df_3['Payload (kg)']*1000

df_new = df_1.append(df_3)

df_new = df_new[df_new['Orbit Altitude'].str.contains("LEO")]

# Merging both dataframes
df = df_new.merge(df_2,left_on='Company ID',right_on='ID',how='inner',validate="m:1")

# Cleaning: removing trailing and leading spaces from Country names
df['Country'].replace(r"^ +| +$", r"", regex=True, inplace=True)

# Cleaning: Normalizing country names
df['Country'] = df['Country'].str.title()
# Cleaning: Passing data to integer and float types
df['Payload (kg)']=df['Payload (kg)'].str.replace(',','')
df['Price ($/kg)']=df['Price ($/kg)'].str.replace(',','')
df['Launch Cost ($M)']=df['Launch Cost ($M)'].str.replace(',','.')
df['Payload (kg)'] = df['Payload (kg)'].astype('float')
df['Price ($/kg)'] = df['Price ($/kg)'].astype('float')
df['Launch Cost ($M)'] = df['Launch Cost ($M)'].astype('float')

# Exclude countries with a launch cost under $10,000,000 in total for all rocket launches across the three classes
# Create list of countries with more than $10M total Launch Cost
list_countries = df.groupby(['Country']).agg('sum')
list_countries = list_countries[list_countries['Launch Cost ($M)']>10].index.values.tolist()

# Select those countries from original dataframe
df = df.loc[df['Country'].isin(list_countries)]

# Exclude companies with QA under 2
df = df[df['QA']>2]

# Classifying payloads
df.loc[df['Payload (kg)'] <= 1000,'Launch Class'] = 'Light'
df.loc[(df['Payload (kg)'] > 1000)&(df['Payload (kg)'] <= 10000),'Launch Class'] = 'Medium'
df.loc[df['Payload (kg)'] > 10000,'Launch Class'] = 'Heavy'

# Selecting only columns that matter
df = df[['Country','Launch Class','Price ($/kg)']]

# Aggregating numeric values into average
df = df.groupby(['Launch Class','Country']).agg('mean')
df.reset_index(inplace=True)

# Selecting the minimum of the average cost for each Launch Class
df= df[df['Price ($/kg)'].isin(df.groupby('Launch Class').min()['Price ($/kg)'].values)]
df=df.rename(columns={"Price ($/kg)":"Average Price"})

# Custom ordering Launch Class
custom_dict = {'Light':0, 'Medium':1, 'Heavy':2}  
df['rank'] = df['Launch Class'].map(custom_dict)
df.sort_values(by=['rank'],inplace=True)
df.drop(columns='rank',inplace=True)

# Selecting only columns that matter
df = df[['Launch Class','Average Price','Country']]
df['Country'] = df['Country'].replace(['Usa'],'USA')
launch_final = df
