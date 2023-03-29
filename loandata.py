# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 19:49:51 2023

@author: haiye
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

loandata.loc[loandata['int.rate'] > 0.12, 'Int.Rate.Type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'Int.Rate.Type'] = 'Low'

caplot = loandata.groupby(['fico.categrory']).size()
caplot.plot.bar(color = 'red')
plt.show()


Purposecount = loandata.groupby(['purpose']).size()
Purposecount.plot.bar(color = 'purple', width = 0.65)
plt.show()

#Scatter Plots
ypoint = loandata['annual_income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color ='pink')
plt.show()

loandata.to_csv('Loandata.Cleaned.csv', index= True)












