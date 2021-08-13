import pandas as pd
import matplotlib.pyplot as plt
import os

#path=os.path("C:\Users\Chint\Downloads\data.csv")
data = pd.read_csv("C:/Users/Chint/Downloads/data.csv",skiprows=4)
print(data.head())
"""
filteredData = data[data.Edition == 2008]
print(filteredData)


#SPORT
fig = plt.subplots(figsize=(10,6))
filteredData.Sport.value_counts().plot()

plt.show()

fig = plt.subplots(figsize=(10,6))
filteredData.Sport.value_counts().plot(kind = 'barh')
plt.show()


#MEDAL
fig = plt.subplots(figsize=(10,6))
filteredData.Medal.value_counts().plot(kind = 'pie',startangle=75,explode=(0,0.1,0),autopct="%1.2f%%")
plt.show()

fig = plt.subplots(figsize=(10,6))
filteredData.Event_gender.value_counts().plot(kind = 'bar')
plt.xlabel("GENDER")
plt.ylabel("TOTAL MEDALS")
plt.legend()

plt.show()
"""
filteredData1 = data[data.Edition == 1992]
print(filteredData1)

fig = plt.subplots(figsize=(11,5))
filteredData1.Sport.value_counts().plot(kind = 'bar',color = 'orange')
plt.xlabel=("Sports")
plt.ylabel("Total Participants")
plt.legend()
plt.show()