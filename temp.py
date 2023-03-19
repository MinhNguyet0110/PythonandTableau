# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv' , sep=';')

# Sumary of the data
data.info()

data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']
data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']

data['SalesTransaction'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']

#Profit Calculation = sales - cost
data['ProfitPerTransaction']=data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (sales - cost)/ cost
data['Markup']= (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

#Rouding Marking
data['Markup']= round(data['Markup'],2)

#Combining data fields

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
data['My_Date']= day +'-'+data['Month']+'-'+ year

#Using iloc to view specific columns/rows

data.iloc[1]
data.head()

# Split columns
# new_var = column.str.split(',' , expand = true)

split_cols = data['ClientKeywords'].str.split(',' , expand=True)

data['ClientAge']=split_cols[0]
data['ClientType']=split_cols[1]
data['LengthOfContract']=split_cols[2]

#Using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

#Using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

# Merge files
# Bringing in new dataset
seasons = pd.read_csv('value_inc_seasons.csv')
aaa = seasons['Month;Season'].str.split(';' , expand = True)



aaa = seasons['Month;Season'].str.split(';' , expand = True)
seasons['Month'] = aaa[0]
seasons['Seasons'] = aaa[1]
seasons = seasons.drop('Month;Season', axis = 1)


# Merge files
data = pd.merge(data, seasons, on = 'Month')
data = data.drop(['Year','Month','Day'], axis = 1 )
data = data.drop('ClientKeywords', axis = 1 )

# Export to csv

data = data.to_csv('ValueInc_Cleaned.csv', index = False)




















