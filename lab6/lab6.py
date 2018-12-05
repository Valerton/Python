import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows',4000)
pd.set_option('display.max_columns',30)
pd.set_option('display.max_colwidth', 10000)
pd.set_option('display.width',None)
plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (15, 5)
data = pd.read_csv('dataset.csv')
def fun1(data):
    return data.sample(10)
def fun2(data):
    return data[['Agency', 'Business Title', 'Work Location 1']][:10]
def fun3(data):   
    print(data[['Agency','# Of Positions']][:10])
    return data[['Agency','# Of Positions']][:10].plot(kind='bar')

def fun4(data):  
    category = data[[u'Job Category']].copy()
    category.loc[:,'Average Salary'] = (data['Salary Range From']+data['Salary Range To'])/2
    print(category[:10])
    category[:10]['Average Salary'].plot(figsize=(15, 5))
def fun5(data):
    location = data[[u'Work Location']].copy()
    location.loc[:,'Average Salary'].mean() = (data['Salary Range From']+data['Salary Range To'])/2
    print(location[:10])
    location[:10]['Average Salary'].plot(figsize=(15, 5))

if (__name__ == "__main__"):
    fun1(data)
    fun2(data)
    fun3(data)
    fun4(data)
    fun5(data)
