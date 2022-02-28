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

one = data["timelineObjects"][1]["placeVisit"]["location"]["name"]
three = data["timelineObjects"][3]["placeVisit"]["location"]["name"]
five = data["timelineObjects"][5]["placeVisit"]["location"]["name"]
seven = data["timelineObjects"][7]["placeVisit"]["location"]["name"]
nine= data["timelineObjects"][9]["placeVisit"]["location"]["name"]
eleven = data["timelineObjects"][11]["placeVisit"]["location"]["name"]
thirteen = data["timelineObjects"][13]["placeVisit"]["location"]["name"]
fifthteen = data["timelineObjects"][15]["placeVisit"]["location"]["name"]


one1 =data["timelineObjects"][3]["placeVisit"]["duration"]["startTimestampMs"]
two2 = data["timelineObjects"][5]["placeVisit"]["duration"]["startTimestampMs"]

#working on date and time

##total1 = float(one1)-float(two2)
#import datetime
#millseconds = float(total1)/ 1000.0
#datetime_obj = datetime.datetime.fromtimestamp(millseconds).strftime('%Y-%m-%d %H:%M:%S.%f')
#print(datetime_obj)








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

startlocation = data["timelineObjects"][0]["activitySegment"]["activities"][14]["probability"]



fig = plt.figure(figsize = (6,6))

tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8,activityType9,activityType10,activityType11,activityType12,activityType13,activityType14]
 
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8,probability9,probability10,probability11,probability12,probability13,probability14]
 
# plotting a bar chart
#plt.bar(left, height, tick_label = tick_label,
        #width = 0.5, color = ['red', 'green'])

plt.pie(height )
plt.title('My bar chart!')
plt.legend(labels = tick_label, title = "Ativity Type:")
plt.show()


#saves the chart to a index.html to be dynamically loaded
html_str = mpld3.fig_to_html(fig)
Html_file= open("index.html","w")
Html_file.write(html_str)
Html_file.close()











