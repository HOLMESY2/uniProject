from sqlite3 import Cursor
from unicodedata import name
import pandas as pd
import json
import matplotlib.pyplot as plt
import pymongo
import mpld3

#converted json file to a dataframe 
with open("Data/2021_NOVEMBER.json") as f:
 data = json.load(f)
 print(type(data))

#test = 'p'
#res = [index for index in data if index[0].lower() == test.lower()]
#print(res)











activityType= data["timelineObjects"][4]["activitySegment"]["activities"][0]["activityType"]
probability = data["timelineObjects"][4]["activitySegment"]["activities"][0]["probability"]
activityType1 = data["timelineObjects"][4]["activitySegment"]["activities"][1]["activityType"]
probability1 = data["timelineObjects"][4]["activitySegment"]["activities"][1]["probability"]
activityType2 = data["timelineObjects"][4]["activitySegment"]["activities"][2]["activityType"]
probability2 = data["timelineObjects"][4]["activitySegment"]["activities"][2]["probability"]
activityType3 = data["timelineObjects"][4]["activitySegment"]["activities"][3]["activityType"]
probability3 = data["timelineObjects"][4]["activitySegment"]["activities"][3]["probability"]
activityType4 = data["timelineObjects"][4]["activitySegment"]["activities"][4]["activityType"]
probability4 = data["timelineObjects"][4]["activitySegment"]["activities"][4]["probability"]
activityType5 = data["timelineObjects"][4]["activitySegment"]["activities"][5]["activityType"]
probability5 = data["timelineObjects"][4]["activitySegment"]["activities"][5]["probability"]
activityType6 = data["timelineObjects"][4]["activitySegment"]["activities"][6]["activityType"]
probability6 = data["timelineObjects"][4]["activitySegment"]["activities"][6]["probability"]
activityType7 = data["timelineObjects"][4]["activitySegment"]["activities"][7]["activityType"]
probability7 = data["timelineObjects"][4]["activitySegment"]["activities"][7]["probability"]
activityType8 = data["timelineObjects"][4]["activitySegment"]["activities"][8]["activityType"]
probability8 = data["timelineObjects"][4]["activitySegment"]["activities"][8]["probability"]
activityType9 = data["timelineObjects"][4]["activitySegment"]["activities"][9]["activityType"]
probability9 = data["timelineObjects"][4]["activitySegment"]["activities"][9]["probability"]
activityType10 = data["timelineObjects"][4]["activitySegment"]["activities"][10]["activityType"]
probability10 = data["timelineObjects"][4]["activitySegment"]["activities"][10]["probability"]
activityType11 = data["timelineObjects"][4]["activitySegment"]["activities"][11]["activityType"]
probability11 = data["timelineObjects"][4]["activitySegment"]["activities"][11]["probability"]
activityType12 = data["timelineObjects"][4]["activitySegment"]["activities"][12]["activityType"]
probability12 = data["timelineObjects"][4]["activitySegment"]["activities"][12]["probability"]
activityType13 = data["timelineObjects"][4]["activitySegment"]["activities"][13]["activityType"]
probability13 = data["timelineObjects"][4]["activitySegment"]["activities"][13]["probability"]
activityType14 = data["timelineObjects"][4]["activitySegment"]["activities"][14]["activityType"]
probability14 = data["timelineObjects"][4]["activitySegment"]["activities"][14]["probability"]




fig = plt.figure(figsize = (5,5))

tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8,activityType9,activityType10,activityType11,activityType12,activityType13,activityType14]
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8,probability9,probability10,probability11,probability12,probability13,probability14]
plt.pie(height)

plt.legend(labels = tick_label, title = "Ativity Type:")

plt.show()

html_str = mpld3.fig_to_html(fig)
Html_file= open("activity_index/index4.html","w")
Html_file.write(html_str)
Html_file.close()





#index 2 in the activity segment 

activityType= data["timelineObjects"][2]["activitySegment"]["activities"][0]["activityType"]
probability = data["timelineObjects"][2]["activitySegment"]["activities"][0]["probability"]
activityType1 = data["timelineObjects"][2]["activitySegment"]["activities"][1]["activityType"]
probability1 = data["timelineObjects"][2]["activitySegment"]["activities"][1]["probability"]
activityType2 = data["timelineObjects"][2]["activitySegment"]["activities"][2]["activityType"]
probability2 = data["timelineObjects"][2]["activitySegment"]["activities"][2]["probability"]
activityType3 = data["timelineObjects"][2]["activitySegment"]["activities"][3]["activityType"]
probability3 = data["timelineObjects"][2]["activitySegment"]["activities"][3]["probability"]
activityType4 = data["timelineObjects"][2]["activitySegment"]["activities"][4]["activityType"]
probability4 = data["timelineObjects"][2]["activitySegment"]["activities"][4]["probability"]
activityType5 = data["timelineObjects"][2]["activitySegment"]["activities"][5]["activityType"]
probability5 = data["timelineObjects"][2]["activitySegment"]["activities"][5]["probability"]
activityType6 = data["timelineObjects"][2]["activitySegment"]["activities"][6]["activityType"]
probability6 = data["timelineObjects"][2]["activitySegment"]["activities"][6]["probability"]
activityType7 = data["timelineObjects"][2]["activitySegment"]["activities"][7]["activityType"]
probability7 = data["timelineObjects"][2]["activitySegment"]["activities"][7]["probability"]
activityType8 = data["timelineObjects"][2]["activitySegment"]["activities"][8]["activityType"]
probability8 = data["timelineObjects"][2]["activitySegment"]["activities"][8]["probability"]
activityType9 = data["timelineObjects"][2]["activitySegment"]["activities"][9]["activityType"]
probability9 = data["timelineObjects"][2]["activitySegment"]["activities"][9]["probability"]
activityType10 = data["timelineObjects"][2]["activitySegment"]["activities"][10]["activityType"]
probability10 = data["timelineObjects"][2]["activitySegment"]["activities"][10]["probability"]
activityType11 = data["timelineObjects"][2]["activitySegment"]["activities"][11]["activityType"]
probability11 = data["timelineObjects"][2]["activitySegment"]["activities"][11]["probability"]
activityType12 = data["timelineObjects"][2]["activitySegment"]["activities"][12]["activityType"]
probability12 = data["timelineObjects"][2]["activitySegment"]["activities"][12]["probability"]
activityType13 = data["timelineObjects"][2]["activitySegment"]["activities"][13]["activityType"]
probability13 = data["timelineObjects"][2]["activitySegment"]["activities"][13]["probability"]
activityType14 = data["timelineObjects"][2]["activitySegment"]["activities"][14]["activityType"]
probability14 = data["timelineObjects"][2]["activitySegment"]["activities"][14]["probability"]




fig = plt.figure(figsize = (5,5))

tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8,activityType9,activityType10,activityType11,activityType12,activityType13,activityType14]
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8,probability9,probability10,probability11,probability12,probability13,probability14]
plt.pie(height)

plt.legend(labels = tick_label, title = "Ativity Type:")

html_str = mpld3.fig_to_html(fig)
Html_file= open("activity_index/index2.html","w")
Html_file.write(html_str)
Html_file.close()


#pie charts 

activityType= data["timelineObjects"][0]["activitySegment"]["activities"][0]["activityType"]
probability = data["timelineObjects"][0]["activitySegment"]["activities"][0]["probability"]
activityType1 = data["timelineObjects"][0]["activitySegment"]["activities"][1]["activityType"]
probability1 = data["timelineObjects"][0]["activitySegment"]["activities"][1]["probability"]
activityType2 = data["timelineObjects"][0]["activitySegment"]["activities"][2]["activityType"]
probability2 = data["timelineObjects"][0]["activitySegment"]["activities"][2]["probability"]
activityType3 = data["timelineObjects"][0]["activitySegment"]["activities"][3]["activityType"]
probability3 = data["timelineObjects"][0]["activitySegment"]["activities"][3]["probability"]
activityType4 = data["timelineObjects"][0]["activitySegment"]["activities"][4]["activityType"]
probability4 = data["timelineObjects"][0]["activitySegment"]["activities"][4]["probability"]
activityType5 = data["timelineObjects"][0]["activitySegment"]["activities"][5]["activityType"]
probability5 = data["timelineObjects"][0]["activitySegment"]["activities"][5]["probability"]
activityType6 = data["timelineObjects"][0]["activitySegment"]["activities"][6]["activityType"]
probability6 = data["timelineObjects"][0]["activitySegment"]["activities"][6]["probability"]
activityType7 = data["timelineObjects"][0]["activitySegment"]["activities"][7]["activityType"]
probability7 = data["timelineObjects"][0]["activitySegment"]["activities"][7]["probability"]
activityType8 = data["timelineObjects"][0]["activitySegment"]["activities"][8]["activityType"]
probability8 = data["timelineObjects"][0]["activitySegment"]["activities"][8]["probability"]
activityType9 = data["timelineObjects"][0]["activitySegment"]["activities"][9]["activityType"]
probability9 = data["timelineObjects"][0]["activitySegment"]["activities"][9]["probability"]
activityType10 = data["timelineObjects"][0]["activitySegment"]["activities"][10]["activityType"]
probability10 = data["timelineObjects"][0]["activitySegment"]["activities"][10]["probability"]
activityType11 = data["timelineObjects"][0]["activitySegment"]["activities"][11]["activityType"]
probability11 = data["timelineObjects"][0]["activitySegment"]["activities"][11]["probability"]
activityType12 = data["timelineObjects"][0]["activitySegment"]["activities"][12]["activityType"]
probability12 = data["timelineObjects"][0]["activitySegment"]["activities"][12]["probability"]
activityType13 = data["timelineObjects"][0]["activitySegment"]["activities"][13]["activityType"]
probability13 = data["timelineObjects"][0]["activitySegment"]["activities"][13]["probability"]
activityType14 = data["timelineObjects"][0]["activitySegment"]["activities"][14]["activityType"]
probability14 = data["timelineObjects"][0]["activitySegment"]["activities"][14]["probability"]


fig = plt.figure(figsize = (5,5))
tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8,activityType9,activityType10,activityType11,activityType12,activityType13,activityType14]
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8,probability9,probability10,probability11,probability12,probability13,probability14]
plt.pie(height)
plt.legend(labels = tick_label, title = "Activity type:")
html_str = mpld3.fig_to_html(fig)
Html_file= open("activity_index/index0.html","w")
Html_file.write(html_str)
Html_file.close()



#index 6 of json 

activityType= data["timelineObjects"][6]["activitySegment"]["activities"][0]["activityType"]
probability = data["timelineObjects"][6]["activitySegment"]["activities"][0]["probability"]
activityType1 = data["timelineObjects"][6]["activitySegment"]["activities"][1]["activityType"]
probability1 = data["timelineObjects"][6]["activitySegment"]["activities"][1]["probability"]
activityType2 = data["timelineObjects"][6]["activitySegment"]["activities"][2]["activityType"]
probability2 = data["timelineObjects"][6]["activitySegment"]["activities"][2]["probability"]
activityType3 = data["timelineObjects"][6]["activitySegment"]["activities"][3]["activityType"]
probability3 = data["timelineObjects"][6]["activitySegment"]["activities"][3]["probability"]
activityType4 = data["timelineObjects"][6]["activitySegment"]["activities"][4]["activityType"]
probability4 = data["timelineObjects"][6]["activitySegment"]["activities"][4]["probability"]
activityType5 = data["timelineObjects"][6]["activitySegment"]["activities"][5]["activityType"]
probability5 = data["timelineObjects"][6]["activitySegment"]["activities"][5]["probability"]
activityType6 = data["timelineObjects"][6]["activitySegment"]["activities"][6]["activityType"]
probability6 = data["timelineObjects"][6]["activitySegment"]["activities"][6]["probability"]
activityType7 = data["timelineObjects"][6]["activitySegment"]["activities"][7]["activityType"]
probability7 = data["timelineObjects"][6]["activitySegment"]["activities"][7]["probability"]
activityType8 = data["timelineObjects"][6]["activitySegment"]["activities"][8]["activityType"]
probability8 = data["timelineObjects"][6]["activitySegment"]["activities"][8]["probability"]
activityType9 = data["timelineObjects"][6]["activitySegment"]["activities"][9]["activityType"]
probability9 = data["timelineObjects"][6]["activitySegment"]["activities"][9]["probability"]
activityType10 = data["timelineObjects"][6]["activitySegment"]["activities"][10]["activityType"]
probability10 = data["timelineObjects"][6]["activitySegment"]["activities"][10]["probability"]
activityType11 = data["timelineObjects"][6]["activitySegment"]["activities"][11]["activityType"]
probability11 = data["timelineObjects"][6]["activitySegment"]["activities"][11]["probability"]
activityType12 = data["timelineObjects"][6]["activitySegment"]["activities"][12]["activityType"]
probability12 = data["timelineObjects"][6]["activitySegment"]["activities"][12]["probability"]
activityType13 = data["timelineObjects"][6]["activitySegment"]["activities"][13]["activityType"]
probability13 = data["timelineObjects"][6]["activitySegment"]["activities"][13]["probability"]
activityType14 = data["timelineObjects"][6]["activitySegment"]["activities"][14]["activityType"]
probability14 = data["timelineObjects"][6]["activitySegment"]["activities"][14]["probability"]


fig = plt.figure(figsize = (5,5))
tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8,activityType9,activityType10,activityType11,activityType12,activityType13,activityType14]
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8,probability9,probability10,probability11,probability12,probability13,probability14]
plt.pie(height)
plt.legend(labels = tick_label, title = "Activity type:")


html_str = mpld3.fig_to_html(fig)
Html_file= open("activity_index/index6.html","w")
Html_file.write(html_str)
Html_file.close()


#index 8 of the json file 
activityType= data["timelineObjects"][8]["activitySegment"]["activities"][0]["activityType"]
probability = data["timelineObjects"][8]["activitySegment"]["activities"][0]["probability"]
activityType1 = data["timelineObjects"][8]["activitySegment"]["activities"][1]["activityType"]
probability1 = data["timelineObjects"][8]["activitySegment"]["activities"][1]["probability"]
activityType2 = data["timelineObjects"][8]["activitySegment"]["activities"][2]["activityType"]
probability2 = data["timelineObjects"][8]["activitySegment"]["activities"][2]["probability"]
activityType3 = data["timelineObjects"][8]["activitySegment"]["activities"][3]["activityType"]
probability3 = data["timelineObjects"][8]["activitySegment"]["activities"][3]["probability"]
activityType4 = data["timelineObjects"][8]["activitySegment"]["activities"][4]["activityType"]
probability4 = data["timelineObjects"][8]["activitySegment"]["activities"][4]["probability"]
activityType5 = data["timelineObjects"][8]["activitySegment"]["activities"][5]["activityType"]
probability5 = data["timelineObjects"][8]["activitySegment"]["activities"][5]["probability"]
activityType6 = data["timelineObjects"][8]["activitySegment"]["activities"][6]["activityType"]
probability6 = data["timelineObjects"][8]["activitySegment"]["activities"][6]["probability"]
activityType7 = data["timelineObjects"][8]["activitySegment"]["activities"][7]["activityType"]
probability7 = data["timelineObjects"][8]["activitySegment"]["activities"][7]["probability"]
activityType8 = data["timelineObjects"][8]["activitySegment"]["activities"][8]["activityType"]
probability8 = data["timelineObjects"][8]["activitySegment"]["activities"][8]["probability"]
activityType9 = data["timelineObjects"][8]["activitySegment"]["activities"][9]["activityType"]
probability9 = data["timelineObjects"][8]["activitySegment"]["activities"][9]["probability"]
activityType10 = data["timelineObjects"][8]["activitySegment"]["activities"][10]["activityType"]
probability10 = data["timelineObjects"][8]["activitySegment"]["activities"][10]["probability"]
activityType11 = data["timelineObjects"][8]["activitySegment"]["activities"][11]["activityType"]
probability11 = data["timelineObjects"][8]["activitySegment"]["activities"][11]["probability"]
activityType12 = data["timelineObjects"][8]["activitySegment"]["activities"][12]["activityType"]
probability12 = data["timelineObjects"][8]["activitySegment"]["activities"][12]["probability"]
activityType13 = data["timelineObjects"][8]["activitySegment"]["activities"][13]["activityType"]
probability13 = data["timelineObjects"][8]["activitySegment"]["activities"][13]["probability"]
activityType14 = data["timelineObjects"][8]["activitySegment"]["activities"][14]["activityType"]
probability14 = data["timelineObjects"][8]["activitySegment"]["activities"][14]["probability"]


fig = plt.figure(figsize = (5,5))
tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8,activityType9,activityType10,activityType11,activityType12,activityType13,activityType14]
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8,probability9,probability10,probability11,probability12,probability13,probability14]
plt.pie(height)
plt.legend(labels = tick_label, title = "Activity type:")

html_str = mpld3.fig_to_html(fig)
Html_file= open("activity_index/index8.html","w")
Html_file.write(html_str)
Html_file.close()


#index 10 of the json file 
activityType= data["timelineObjects"][10]["activitySegment"]["activities"][0]["activityType"]
probability = data["timelineObjects"][10]["activitySegment"]["activities"][0]["probability"]
activityType1 = data["timelineObjects"][10]["activitySegment"]["activities"][1]["activityType"]
probability1 = data["timelineObjects"][10]["activitySegment"]["activities"][1]["probability"]
activityType2 = data["timelineObjects"][10]["activitySegment"]["activities"][2]["activityType"]
probability2 = data["timelineObjects"][10]["activitySegment"]["activities"][2]["probability"]
activityType3 = data["timelineObjects"][10]["activitySegment"]["activities"][3]["activityType"]
probability3 = data["timelineObjects"][10]["activitySegment"]["activities"][3]["probability"]
activityType4 = data["timelineObjects"][10]["activitySegment"]["activities"][4]["activityType"]
probability4 = data["timelineObjects"][10]["activitySegment"]["activities"][4]["probability"]
activityType5 = data["timelineObjects"][10]["activitySegment"]["activities"][5]["activityType"]
probability5 = data["timelineObjects"][10]["activitySegment"]["activities"][5]["probability"]
activityType6 = data["timelineObjects"][10]["activitySegment"]["activities"][6]["activityType"]
probability6 = data["timelineObjects"][10]["activitySegment"]["activities"][6]["probability"]
activityType7 = data["timelineObjects"][10]["activitySegment"]["activities"][7]["activityType"]
probability7 = data["timelineObjects"][10]["activitySegment"]["activities"][7]["probability"]
activityType8 = data["timelineObjects"][10]["activitySegment"]["activities"][8]["activityType"]
probability8 = data["timelineObjects"][10]["activitySegment"]["activities"][8]["probability"]
activityType9 = data["timelineObjects"][10]["activitySegment"]["activities"][9]["activityType"]
probability9 = data["timelineObjects"][10]["activitySegment"]["activities"][9]["probability"]
activityType10 = data["timelineObjects"][10]["activitySegment"]["activities"][10]["activityType"]
probability10 = data["timelineObjects"][10]["activitySegment"]["activities"][10]["probability"]
activityType11 = data["timelineObjects"][10]["activitySegment"]["activities"][11]["activityType"]
probability11 = data["timelineObjects"][10]["activitySegment"]["activities"][11]["probability"]
activityType12 = data["timelineObjects"][10]["activitySegment"]["activities"][12]["activityType"]
probability12 = data["timelineObjects"][10]["activitySegment"]["activities"][12]["probability"]
activityType13 = data["timelineObjects"][10]["activitySegment"]["activities"][13]["activityType"]
probability13 = data["timelineObjects"][10]["activitySegment"]["activities"][13]["probability"]
activityType14 = data["timelineObjects"][10]["activitySegment"]["activities"][14]["activityType"]
probability14 = data["timelineObjects"][10]["activitySegment"]["activities"][14]["probability"]


fig = plt.figure(figsize = (5,5))
tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8,activityType9,activityType10,activityType11,activityType12,activityType13,activityType14]
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8,probability9,probability10,probability11,probability12,probability13,probability14]
plt.pie(height)
plt.legend(labels = tick_label, title = "Activity type:")

html_str = mpld3.fig_to_html(fig)
Html_file= open("activity_index/index10.html","w")
Html_file.write(html_str)
Html_file.close()


#index 12 of the json file 

activityType= data["timelineObjects"][12]["activitySegment"]["activities"][0]["activityType"]
probability = data["timelineObjects"][12]["activitySegment"]["activities"][0]["probability"]
activityType1 = data["timelineObjects"][12]["activitySegment"]["activities"][1]["activityType"]
probability1 = data["timelineObjects"][12]["activitySegment"]["activities"][1]["probability"]
activityType2 = data["timelineObjects"][12]["activitySegment"]["activities"][2]["activityType"]
probability2 = data["timelineObjects"][12]["activitySegment"]["activities"][2]["probability"]
activityType3 = data["timelineObjects"][12]["activitySegment"]["activities"][3]["activityType"]
probability3 = data["timelineObjects"][12]["activitySegment"]["activities"][3]["probability"]
activityType4 = data["timelineObjects"][12]["activitySegment"]["activities"][4]["activityType"]
probability4 = data["timelineObjects"][12]["activitySegment"]["activities"][4]["probability"]
activityType5 = data["timelineObjects"][12]["activitySegment"]["activities"][5]["activityType"]
probability5 = data["timelineObjects"][12]["activitySegment"]["activities"][5]["probability"]
activityType6 = data["timelineObjects"][12]["activitySegment"]["activities"][6]["activityType"]
probability6 = data["timelineObjects"][12]["activitySegment"]["activities"][6]["probability"]
activityType7 = data["timelineObjects"][12]["activitySegment"]["activities"][7]["activityType"]
probability7 = data["timelineObjects"][12]["activitySegment"]["activities"][7]["probability"]
activityType8 = data["timelineObjects"][12]["activitySegment"]["activities"][8]["activityType"]
probability8 = data["timelineObjects"][12]["activitySegment"]["activities"][8]["probability"]
activityType9 = data["timelineObjects"][12]["activitySegment"]["activities"][9]["activityType"]
probability9 = data["timelineObjects"][12]["activitySegment"]["activities"][9]["probability"]
activityType10 = data["timelineObjects"][12]["activitySegment"]["activities"][10]["activityType"]
probability10 = data["timelineObjects"][12]["activitySegment"]["activities"][10]["probability"]
activityType11 = data["timelineObjects"][12]["activitySegment"]["activities"][11]["activityType"]
probability11 = data["timelineObjects"][12]["activitySegment"]["activities"][11]["probability"]
activityType12 = data["timelineObjects"][12]["activitySegment"]["activities"][12]["activityType"]
probability12 = data["timelineObjects"][12]["activitySegment"]["activities"][12]["probability"]
activityType13 = data["timelineObjects"][12]["activitySegment"]["activities"][13]["activityType"]
probability13 = data["timelineObjects"][12]["activitySegment"]["activities"][13]["probability"]
activityType14 = data["timelineObjects"][12]["activitySegment"]["activities"][14]["activityType"]
probability14 = data["timelineObjects"][12]["activitySegment"]["activities"][14]["probability"]


fig = plt.figure(figsize = (5,5))
tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8,activityType9,activityType10,activityType11,activityType12,activityType13,activityType14]
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8,probability9,probability10,probability11,probability12,probability13,probability14]
plt.pie(height)
plt.legend(labels = tick_label, title = "Activity type:")

html_str = mpld3.fig_to_html(fig)
Html_file= open("activity_index/index12.html","w")
Html_file.write(html_str)
Html_file.close()


#index 14 of json file 

activityType= data["timelineObjects"][14]["activitySegment"]["activities"][0]["activityType"]
probability = data["timelineObjects"][14]["activitySegment"]["activities"][0]["probability"]
activityType1 = data["timelineObjects"][14]["activitySegment"]["activities"][1]["activityType"]
probability1 = data["timelineObjects"][14]["activitySegment"]["activities"][1]["probability"]
activityType2 = data["timelineObjects"][14]["activitySegment"]["activities"][2]["activityType"]
probability2 = data["timelineObjects"][14]["activitySegment"]["activities"][2]["probability"]
activityType3 = data["timelineObjects"][14]["activitySegment"]["activities"][3]["activityType"]
probability3 = data["timelineObjects"][14]["activitySegment"]["activities"][3]["probability"]
activityType4 = data["timelineObjects"][14]["activitySegment"]["activities"][4]["activityType"]
probability4 = data["timelineObjects"][14]["activitySegment"]["activities"][4]["probability"]
activityType5 = data["timelineObjects"][14]["activitySegment"]["activities"][5]["activityType"]
probability5 = data["timelineObjects"][14]["activitySegment"]["activities"][5]["probability"]
activityType6 = data["timelineObjects"][14]["activitySegment"]["activities"][6]["activityType"]
probability6 = data["timelineObjects"][14]["activitySegment"]["activities"][6]["probability"]
activityType7 = data["timelineObjects"][14]["activitySegment"]["activities"][7]["activityType"]
probability7 = data["timelineObjects"][14]["activitySegment"]["activities"][7]["probability"]
activityType8 = data["timelineObjects"][14]["activitySegment"]["activities"][8]["activityType"]
probability8 = data["timelineObjects"][14]["activitySegment"]["activities"][8]["probability"]
activityType9 = data["timelineObjects"][14]["activitySegment"]["activities"][9]["activityType"]
probability9 = data["timelineObjects"][14]["activitySegment"]["activities"][9]["probability"]
activityType10 = data["timelineObjects"][14]["activitySegment"]["activities"][10]["activityType"]
probability10 = data["timelineObjects"][14]["activitySegment"]["activities"][10]["probability"]
activityType11 = data["timelineObjects"][14]["activitySegment"]["activities"][11]["activityType"]
probability11 = data["timelineObjects"][14]["activitySegment"]["activities"][11]["probability"]
activityType12 = data["timelineObjects"][14]["activitySegment"]["activities"][12]["activityType"]
probability12 = data["timelineObjects"][14]["activitySegment"]["activities"][12]["probability"]
activityType13 = data["timelineObjects"][14]["activitySegment"]["activities"][13]["activityType"]
probability13 = data["timelineObjects"][14]["activitySegment"]["activities"][13]["probability"]
activityType14 = data["timelineObjects"][14]["activitySegment"]["activities"][14]["activityType"]
probability14 = data["timelineObjects"][14]["activitySegment"]["activities"][14]["probability"]


fig = plt.figure(figsize = (5,5))
tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8,activityType9,activityType10,activityType11,activityType12,activityType13,activityType14]
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8,probability9,probability10,probability11,probability12,probability13,probability14]
plt.pie(height)
plt.legend(labels = tick_label, title = "Activity type:")


html_str = mpld3.fig_to_html(fig)
Html_file= open("activity_index/index14.html","w")
Html_file.write(html_str)
Html_file.close()


#index 16 of json file 

activityType= data["timelineObjects"][16]["activitySegment"]["activities"][0]["activityType"]
probability = data["timelineObjects"][16]["activitySegment"]["activities"][0]["probability"]
activityType1 = data["timelineObjects"][16]["activitySegment"]["activities"][1]["activityType"]
probability1 = data["timelineObjects"][16]["activitySegment"]["activities"][1]["probability"]
activityType2 = data["timelineObjects"][16]["activitySegment"]["activities"][2]["activityType"]
probability2 = data["timelineObjects"][16]["activitySegment"]["activities"][2]["probability"]
activityType3 = data["timelineObjects"][16]["activitySegment"]["activities"][3]["activityType"]
probability3 = data["timelineObjects"][16]["activitySegment"]["activities"][3]["probability"]
activityType4 = data["timelineObjects"][16]["activitySegment"]["activities"][4]["activityType"]
probability4 = data["timelineObjects"][16]["activitySegment"]["activities"][4]["probability"]
activityType5 = data["timelineObjects"][16]["activitySegment"]["activities"][5]["activityType"]
probability5 = data["timelineObjects"][16]["activitySegment"]["activities"][5]["probability"]
activityType6 = data["timelineObjects"][16]["activitySegment"]["activities"][6]["activityType"]
probability6 = data["timelineObjects"][16]["activitySegment"]["activities"][6]["probability"]
activityType7 = data["timelineObjects"][16]["activitySegment"]["activities"][7]["activityType"]
probability7 = data["timelineObjects"][16]["activitySegment"]["activities"][7]["probability"]
activityType8 = data["timelineObjects"][16]["activitySegment"]["activities"][8]["activityType"]
probability8 = data["timelineObjects"][16]["activitySegment"]["activities"][8]["probability"]
activityType9 = data["timelineObjects"][16]["activitySegment"]["activities"][9]["activityType"]
probability9 = data["timelineObjects"][16]["activitySegment"]["activities"][9]["probability"]
activityType10 = data["timelineObjects"][16]["activitySegment"]["activities"][10]["activityType"]
probability10 = data["timelineObjects"][16]["activitySegment"]["activities"][10]["probability"]
activityType11 = data["timelineObjects"][16]["activitySegment"]["activities"][11]["activityType"]
probability11 = data["timelineObjects"][16]["activitySegment"]["activities"][11]["probability"]
activityType12 = data["timelineObjects"][16]["activitySegment"]["activities"][12]["activityType"]
probability12 = data["timelineObjects"][16]["activitySegment"]["activities"][12]["probability"]
activityType13 = data["timelineObjects"][16]["activitySegment"]["activities"][13]["activityType"]
probability13 = data["timelineObjects"][16]["activitySegment"]["activities"][13]["probability"]
activityType14 = data["timelineObjects"][16]["activitySegment"]["activities"][14]["activityType"]
probability14 = data["timelineObjects"][16]["activitySegment"]["activities"][14]["probability"]


fig = plt.figure(figsize = (5,5))
tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8,activityType9,activityType10,activityType11,activityType12,activityType13,activityType14]
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8,probability9,probability10,probability11,probability12,probability13,probability14]
plt.pie(height)
plt.legend(labels = tick_label, title = "Activity type:")

 


html_str = mpld3.fig_to_html(fig)
Html_file= open("activity_index/index16.html","w")
Html_file.write(html_str)
Html_file.close()

































#show the bar charts all at once 


































