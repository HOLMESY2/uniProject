import json
import numpy as np
import matplotlib.pyplot as plt
import pymongo
import mpld3
from prettytable import PrettyTable
import datetime

with open("Data/2021_NOVEMBER.json") as f:
 data = json.load(f)
 print(type(data))


#working on date and time

fig = plt.figure(figsize = (17,8))
address = data["timelineObjects"][1]["placeVisit"]["duration"]["startTimestampMs"]
address1 = data["timelineObjects"][3]["placeVisit"]["duration"]["startTimestampMs"]
address2 = data["timelineObjects"][5]["placeVisit"]["duration"]["startTimestampMs"]
address3 = data["timelineObjects"][7]["placeVisit"]["duration"]["startTimestampMs"]
address4 = data["timelineObjects"][9]["placeVisit"]["duration"]["startTimestampMs"]
address5 = data["timelineObjects"][11]["placeVisit"]["duration"]["startTimestampMs"]
address6 = data["timelineObjects"][13]["placeVisit"]["duration"]["startTimestampMs"]
address7 = data["timelineObjects"][15]["placeVisit"]["duration"]["startTimestampMs"]
address8 = data["timelineObjects"][17]["placeVisit"]["duration"]["startTimestampMs"]
address9 = data["timelineObjects"][19]["placeVisit"]["duration"]["startTimestampMs"]

address = float(address)/ 1000.0
datetime_obj = datetime.datetime.fromtimestamp(address).strftime('%Y-%m-%d %H:%M:%S.%f')

address1 = float(address1)/ 1000.0
datetime_obj1 = datetime.datetime.fromtimestamp(address1).strftime('%Y-%m-%d %H:%M:%S.%f')

address2 = float(address2)/ 1000.0
datetime_obj2 = datetime.datetime.fromtimestamp(address2).strftime('%Y-%m-%d %H:%M:%S.%f')

address3 = float(address3)/ 1000.0
datetime_obj3 = datetime.datetime.fromtimestamp(address3).strftime('%Y-%m-%d %H:%M:%S.%f')

address4 = float(address4)/ 1000.0
datetime_obj4 = datetime.datetime.fromtimestamp(address4).strftime('%Y-%m-%d %H:%M:%S.%f')

address5 = float(address5)/ 1000.0
datetime_obj5 = datetime.datetime.fromtimestamp(address5).strftime('%Y-%m-%d %H:%M:%S.%f')

address6 = float(address6)/ 1000.0
datetime_obj6 = datetime.datetime.fromtimestamp(address6).strftime('%Y-%m-%d %H:%M:%S.%f')

address7 = float(address7)/ 1000.0
datetime_obj7 = datetime.datetime.fromtimestamp(address7).strftime('%Y-%m-%d %H:%M:%S.%f')

address8 = float(address8)/ 1000.0
datetime_obj8 = datetime.datetime.fromtimestamp(address8).strftime('%Y-%m-%d %H:%M:%S.%f')

address9 = float(address9)/ 1000.0
datetime_obj9 = datetime.datetime.fromtimestamp(address9).strftime('%Y-%m-%d %H:%M:%S.%f')



name = data["timelineObjects"][1]["placeVisit"]["location"]["name"]
name1 = data["timelineObjects"][3]["placeVisit"]["location"]["name"]
name2 = data["timelineObjects"][5]["placeVisit"]["location"]["name"]
name3 = data["timelineObjects"][7]["placeVisit"]["location"]["name"]
name4 = data["timelineObjects"][9]["placeVisit"]["location"]["name"]
name5 = data["timelineObjects"][11]["placeVisit"]["location"]["name"]
name6 = data["timelineObjects"][13]["placeVisit"]["location"]["name"]
name7 = data["timelineObjects"][15]["placeVisit"]["location"]["name"]
name8 = data["timelineObjects"][17]["placeVisit"]["location"]["name"]
name9 = data["timelineObjects"][19]["placeVisit"]["location"]["name"]




x = [name,name1,name2,name3,name4,name5,name6,name7,name8,name9]
y = [datetime_obj,datetime_obj1,datetime_obj2,datetime_obj3,datetime_obj4,datetime_obj5,datetime_obj6,datetime_obj7,datetime_obj8,datetime_obj9]
plt.xticks(rotation='vertical')
plt.title('Scatter Graph showing the arrival time at each location')
plt.scatter(x ,y )
#plt.plot(x,y)
plt.show()

html_str = mpld3.fig_to_html(fig)
Html_file= open("places_visited_index/PVindex.html","w")
Html_file.write(html_str)
Html_file.close()
