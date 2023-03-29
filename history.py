# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Mon Feb  6 19:50:01 2023)---
test_list_tour = [1, 2, 3, 4, 5]
test_dict_tour = {'a': 1, 'b': 2}
runfile('C:/Users/haiye/.spyder-py3/temp.py', wdir='C:/Users/haiye/.spyder-py3')
runcell(0, 'C:/Users/haiye/.spyder-py3/temp.py')
runfile('C:/Users/haiye/.spyder-py3/temp.py', wdir='C:/Users/haiye/.spyder-py3')

## ---(Mon Feb  6 20:05:12 2023)---
runfile('C:/Users/haiye/.spyder-py3/temp.py', wdir='C:/Users/haiye/.spyder-py3')
runcell(0, 'C:/Users/haiye/.spyder-py3/temp.py')
runfile('C:/Users/haiye/.spyder-py3/temp.py', wdir='C:/Users/haiye/.spyder-py3')
runcell(0, 'C:/Users/haiye/.spyder-py3/temp.py')
runfile('C:/Users/haiye/.spyder-py3/temp.py', wdir='C:/Users/haiye/.spyder-py3')
runcell(0, 'C:/Users/haiye/.spyder-py3/temp.py')
runfile('C:/Users/haiye/.spyder-py3/temp.py', wdir='C:/Users/haiye/.spyder-py3')
runcell(0, 'C:/Users/haiye/.spyder-py3/temp.py')
data.info()
data['SalesTransaction'] = data['SailingPricePerItem']*data['NumberOfItemsPurchased']
data['SalesTransaction'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']

## ---(Tue Feb  7 14:19:46 2023)---
runfile('C:/Users/haiye/.spyder-py3/temp.py', wdir='C:/Users/haiye/.spyder-py3')
runcell(0, 'C:/Users/haiye/.spyder-py3/temp.py')
data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemPurchased']
data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemPurchased']

data['SalesTransaction'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']
#Profit Calculation = sales - cost
data['ProfitPerTransaction']=data['SalesPerTransaction'] - data['CostPerTransaction']
data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']
data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']
data['SalesTransaction'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']
data['ProfitPerTransaction']=data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup']= (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']
data['Markup']= round(data['Markup'],2)
data['Day'].astype(str)
data['Year'].astype(str)
Data['My_Date']= data['Day']+'-'+data['Month']+'-'+data['Year']
print(data['Day'].dtype)
data['Year'].astype(str)
data['Day'].astype(str)
print(data['Day'].dtype)
Data['My_Date']= data['Day']+'-'+data['Month']+'-'+data['Year']
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
Data['My_Date']= day +'-'+data['Month']+'-'+ year
data['My_Date']= day +'-'+data['Month']+'-'+ year
data.iloc(0)
data.iloc[1]
data.head()
data.info()
splil_cols = dât['ClientKeywords'].str.split(',' expand = true)
splil_cols = data['ClientKeywords'].str.split(',' expand = true)
splil_cols = data['ClientKeywords'].str.split(',' expand=true)
split_cols = data['ClientKeywords'].str.split(',' expand=true)
split_cols = data['ClientKeywords'].str.split(',' , expand=true)
split_cols = data['ClientKeywords'].str.split(',' , expand=True)
data['ClientAge']=split_cols(0)
data['ClientAge']=split_cols[0]
data['ClientType']=split_cols[1]
data['LengthOfContract']=split_cols[2]
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')
data['ItemDescription'].lower()
data['ItemDescription'] = data['ItemDescription'].str.lower()
seasons = pd.read_csv('value_inc_seasons.csv')
data = pd.merge(data, seasons, on = 'Month')
seasons.info()
seasons(Month;Season).str.split(';' , expand = True)
seasons[Month;Season].str.split(';' , expand = True)
aaa = seasons[Month;Season].str.split(';' , expand = True)
aaa = seasons['Month;Season'].str.split(';' , expand = True)
seasons['Month'] = aaa[0]
seasons['Seasons'] = aaa[1]
seasons = seasons.drop['Month;Season', axis = 1]
seasons = seasons.drop('Month;Season', axis = 1)
data = pd.merge(data, seasons, on = 'Month')
data = data.drop(['Year','Month','Day'], axis = 1 )
data = data.drop('ClientKeywords', axis = 1 )
data = data.to_csv('ValueInc_Cleaned.csv', index = False)
runfile('C:/Users/haiye/.spyder-py3/temp.py', wdir='C:/Users/haiye/.spyder-py3')
data = data.to_csv('ValueInc_Cleaned.csv', index = False)
runfile('C:/Users/haiye/.spyder-py3/temp.py', wdir='C:/Users/haiye/.spyder-py3')

## ---(Thu Feb  9 19:48:43 2023)---
import json
import pandas as pd
json_file = open(loan_data_json.json)
data = pd.json(json_file)
json_file = open('loan_data_json.json')
data = pd.json(json_file)
json_file = open('loan_data_json.json')
data = json.load(json_file)

with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
lists.append('mango')
lists.append['mango']
lists.append('mango')

lists = ['apple','banana','pear','cherry','orange']

# append to a list
lists.append('mango')
ists.insert(2, 'dragon fruit')
lists.insert(2, 'dragon fruit')
lists.remove('apple')
lists.pop()
my_dict = {'Name':'Nguyet','Age':'23','Hometown':'Dong Nai','Major':'Business Administration','hobby':'traveling'}
my_dict['Name']
my_dict['Age']
my_dict.keys()
my_dict.values()
my_dict.items()
my_dict['Gender']='female'
my_dict
loandata = pd.DataFrame(data)
loandata.info()
loandata['purpose'].unique
loandata['purpose'].unique()
loandata.discribe()
loandata.discribe
loandata.describe()
loandata['dti'].describe()
loandata['purpose'].describe()
loandata['fico'].describe()
income = np.exp(loandata['log.annual.inc'])
import numpy as np
income = np.exp(loandata['log.annual.inc'])
loandata['annual_income']= income
arr = np.array(1,2,3,4)
arr = np.array([1,2,3,4])
arr1 = np.array([1,2,3,4],[5,6,7,8],[9,10,11,12])
arr1 = np.array([1,2,3,4],[5,6,7,8])
arr1 = np.array([1, 2, 3, 4],[5, 6, 7, 8])
arr1 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])

x = 6

if x <= 4:
    print('Kém')
elif x > 4 and x <= 5:
    print('Trung bình')
elif x > 5 and x < 7:
    print('trung bình khá')
elif x >= 7 and x < 8:
    print('Khá')
elif x >=8 and x <9:
    print('giỏi')
else:
    print('Xuất sắc')
x = 9.9

if x <= 4:
    print('Kém')
elif x > 4 and x <= 5:
    print('Trung bình')
elif x > 5 and x < 7:
    print('trung bình khá')
elif x >= 7 and x < 8:
    print('Khá')
elif x >=8 and x <9:
    print('giỏi')
else:
    print('Xuất sắc')
x = 2

if x <= 4:
    print('Kém')
elif x > 4 and x <= 5:
    print('Trung bình')
elif x > 5 and x < 7:
    print('trung bình khá')
elif x >= 7 and x < 8:
    print('Khá')
elif x >=8 and x <9:
    print('giỏi')
else:
    print('Xuất sắc')

fruit = ['Orange','Aplle','Cherry','guava']
for x in fruit:
    print x
fruit = ['Orange','Aplle','Cherry','guava']
for x in fruit:
    print(x)

fruit = ['Orange','Aplle','Cherry','guava']
for x in fruit:
    y = x+' for sales'
    print(x)

fruit = ['Orange','Aplle','Cherry','guava']
for x in fruit:
    y = x+' for sales'
    print(y)
loandata['fico']
len(loandata)
ficocat = []
for x in range(len(loandata)):
    categrory = loandata['fico'][x]
    if categrory >= 300 and < 400:
        cat = 'very poor'
    elif categrory >= 400 and categrory < 600:
        cat = 'poor'
    elif categrory >= 600 and categrory < 600:
        cat = 'fair'
    elif categrory >= 660 and categrory < 700:
        cat = 'good'
    elif categrory >= 700:
        cat = 'excellent'
    else:
        cat = 'unknown'
    ficocat.append(cat)

loandata['fico']
len(loandata)

ficocat = []
for x in range(len(loandata)):
    categrory = loandata['fico'][x]
    if categrory >= 300 and categrory < 400:
        cat = 'very poor'
    elif categrory >= 400 and categrory < 600:
        cat = 'poor'
    elif categrory >= 600 and categrory < 600:
        cat = 'fair'
    elif categrory >= 660 and categrory < 700:
        cat = 'good'
    elif categrory >= 700:
        cat = 'excellent'
    else:
        cat = 'unknown'
    ficocat.append(cat)
np.series(ficocat)
Ficocat = pd.series(ficocat)
Ficocat = pd.Series(ficocat)
loandata['fico.categrory'] = Ficocat

## ---(Mon Feb 20 20:06:43 2023)---

"""
Created on Thu Feb  9 19:49:51 2023

@author: haiye
"""

import json
import pandas as pd
import numpy as np

json_file = open('loan_data_json.json')
data = json.load(json_file)

with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

loandata = pd.DataFrame(data)

#finding unique values
loandata['purpose'].unique()

# discribe the data
loandata.describe()

#describe the specific column
loandata['dti'].describe()
loandata['purpose'].describe()
loandata['fico'].describe()

# using exp to get the anual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual_income']= income

#working with array
arr = np.array([1,2,3,4])
arr1 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])

x = 2

if x <= 4:
    print('Kém')
elif x > 4 and x <= 5:
    print('Trung bình')
elif x > 5 and x < 7:
    print('trung bình khá')
elif x >= 7 and x < 8:
    print('Khá')
elif x >=8 and x <9:
    print('giỏi')
else:
    print('Xuất sắc')

# For loop
fruit = ['Orange','Aplle','Cherry','guava']
for x in fruit:
    y = x+' for sales'
    print(y)

# applying loop in loandata
loandata['fico']
len(loandata)

ficocat = []
for x in range(len(loandata)):
    categrory = loandata['fico'][x]
    if categrory >= 300 and categrory < 400:
        cat = 'very poor'
    elif categrory >= 400 and categrory < 600:
        cat = 'poor'
    elif categrory >= 600 and categrory < 600:
        cat = 'fair'
    elif categrory >= 660 and categrory < 700:
        cat = 'good'
    elif categrory >= 700:
        cat = 'excellent'
    else:
        cat = 'unknown'
    ficocat.append(cat)

Ficocat = pd.Series(ficocat)
loandata['fico.categrory'] = Ficocat
import json
import pandas as pd
import numpy as np
json_file = open('loan_data_json.json')
data = json.load(json_file)
loandata.info()
loandata = pd.DataFrame(data)
loandata['fico']
len(loandata)

ficocat = []
for x in range(len(loandata)):
    categrory = loandata['fico'][x]
    if categrory >= 300 and categrory < 400:
        cat = 'very poor'
    elif categrory >= 400 and categrory < 600:
        cat = 'poor'
    elif categrory >= 600 and categrory < 600:
        cat = 'fair'
    elif categrory >= 660 and categrory < 700:
        cat = 'good'
    elif categrory >= 700:
        cat = 'excellent'
    else:
        cat = 'unknown'
    ficocat.append(cat)

Ficocat = pd.Series(ficocat)
loandata['fico.categrory'] = Ficocat
loandata.info()
loandata.loc[loandata[int.rate] > 0.12, 'Int.Rate.Type'] = 'High'
loandata.loc[loandata[interest.rate] > 0.12, 'Int.Rate.Type'] = 'High'
loandata.loc[loandata['int.rate'] > 0.12, 'Int.Rate.Type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'Int.Rate.Type'] = 'Low'
import matplotlib.pyplot as plt
caplot = loandata.groupby([fico.categrory]).size()
caplot = loandata.groupby(['fico.categrory']).size()
caplot = loandata.groupby(['fico.categrory']).size()
caplot.plot.bar()
plt.show()
caplot = loandata.groupby(['fico.categrory']).size()
caplot.plot.bar()
caplot = loandata.groupby(['fico.categrory']).size()
caplot.plot.bar(color = 'red')
plt.show()

Purposecount = loandata.groupby(['purpose']).size()
Purposecount.plot.bar(color = 'purple')
plt.show()
Purposecount = loandata.groupby(['purpose']).size()
Purposecount.plot.bar(color = 'purple', width = 1)
plt.show()
Purposecount = loandata.groupby(['purpose']).size()
Purposecount.plot.bar(color = 'purple', width = 0.5)
plt.show()
Purposecount = loandata.groupby(['purpose']).size()
Purposecount.plot.bar(color = 'purple', width = 0.65)
plt.show()

ypoint = loandata['log.annual.inc']
xpoint = loandata['pti']
plt.scatter(xpoint, ypoint)
plt.show()

ypoint = loandata['log.annual.inc']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()
xpoint = loandata['log.annual.inc']
ypoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()
income = np.exp(loandata['log.annual.inc'])
loandata['annual_income']= income
loandata.info()

xpoint = loandata['annual_income']
ypoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()
ypoint = loandata['annual_income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

ypoint = loandata['annual_income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color ='green')
plt.show()

ypoint = loandata['annual_income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color ='lightgreen')
plt.show()

ypoint = loandata['annual_income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color ='pink')
plt.show()
loandata.to_csv('Loandata.Cleaned.csv', index= True)
data = pd.read_xlsx('articles.xlsx')
import pandas as pd

data = pd.read_xlsx('articles.xlsx')
runfile('C:/Users/haiye/.spyder-py3/Blogme.py', wdir='C:/Users/haiye/.spyder-py3')
import pandas as pd

data = pd.read_excel('articles.xlsx')
data.info()
data.groupby(['source_id'])['article_id'].count()
data.groupby(['source_id'])['engagement_reaction_count'].sum()
data.drop('engagement_comment_plugin_count')

data.drop('engagement_comment_plugin_count', axis = 1)