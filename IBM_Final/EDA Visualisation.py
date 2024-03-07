
# pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
import seaborn as sns
import json5 as js

#from js import fetch
import io
import requests

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"
df=pd.read_csv(URL) #dataset_part_2_csv)
print(df.head(5))
print(df.dtypes)
"""
"""
sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()

sns.catplot(y="LaunchSite", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Launch Site",fontsize=20)
plt.show()

sns.barplot(x='Orbit', y='Class', hue='Orbit', data=df)
plt.xlabel("Targeted Orbit",fontsize=20)
plt.ylabel("Success Rate",fontsize=20)
plt.show()

sns.catplot(y="LaunchSite", x="PayloadMass", hue="Class", data=df, aspect = 5)
plt.xlabel("Launch Site",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()

sns.catplot(y="Orbit", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Orbit",fontsize=20)
plt.show()

sns.catplot(y="Orbit", x="PayloadMass", hue="Class", data=df, aspect = 5)
plt.xlabel("Pay load Mass (kg)",fontsize=20)
plt.ylabel("Orbit",fontsize=20)
plt.show()



year=[]
def Extract_year():
    for i in df["Date"]:
        year.append(i.split("-")[0])
    return year
Extract_year()
df['Date'] = year
#print(df.head())

SuccessRatio = pd.DataFrame()
SuccessRatio['Date'] = (df['Date'].unique())

sRatio = []

def computeSuccessRatio():
    for i in SuccessRatio['Date']:
        #print('Date at work :', i)    
        success = df.loc[df['Date'] == i, 'Class'].sum()
        #print('Success total : ', success)
        total = df.loc[df['Date'] == i, 'Class'].count()
        #print('Number of observations :', total)
        ratio = success / total
        #print('Ratio : ', ratio)
        sRatio.append(ratio)
    return sRatio

SuccessRatio['SRatio'] = computeSuccessRatio()

#print(SuccessRatio)


"""
#  Basic version
sns.catplot(y="Class", x="Date", hue="Class", data=df, aspect = 5)
plt.xlabel("Year",fontsize=20)
plt.ylabel("Success Rate",fontsize=20)
plt.show()

"""
# Sophisticated version
sns.lineplot(y="SRatio", x="Date", data=SuccessRatio)
plt.xlabel("Year",fontsize=20)
plt.ylabel("Success Rate",fontsize=20)
plt.show()

features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()

tempDF = df[['Orbit', 'LaunchSite', 'LandingPad', 'Serial']]
tempDF.head()
features_one_hot = pd.get_dummies(tempDF, prefix=['Orbit', 'LaunchSite', 'LandingPad', 'Serial'])
features_one_hot[['FlightNumber', 'PayloadMass', 'Flights', 'GridFins', 'Reused', 'Legs', 'Block', 'ReusedCount']] = features[['FlightNumber', 'PayloadMass', 'Flights', 'GridFins', 'Reused', 'Legs', 'Block', 'ReusedCount']]

features_one_hot = features_one_hot.astype(float)

features_one_hot.head()

