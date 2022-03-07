import json
from mpld3 import save_html
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


plt.rc('font', size=17) 
fig = plt.figure(figsize = (17,8))
x = [name,name1,name2,name3,name4,name5,name6,name7,name8,name9]

y = [datetime_obj,datetime_obj1,datetime_obj2,datetime_obj3,datetime_obj4,datetime_obj5,datetime_obj6,datetime_obj7,datetime_obj8,datetime_obj9]
plt.xticks(rotation='vertical')

plt.scatter(x, y, c ="blue")
plt.title('Scatter Graph showing the arrival time at each location')


plt.ticklabel_format
#plt.plot(x,y)
plt.show()


html_str = mpld3.fig_to_html(fig)
Html_file= open("places_visited_index/PVindex.html","w")
Html_file.write(html_str)
Html_file.close()

fig = plt.figure(figsize = (17,8))
end = data["timelineObjects"][1]["placeVisit"]["duration"]["endTimestampMs"]
end1 = data["timelineObjects"][3]["placeVisit"]["duration"]["endTimestampMs"]
end2 = data["timelineObjects"][5]["placeVisit"]["duration"]["endTimestampMs"]
end3 = data["timelineObjects"][7]["placeVisit"]["duration"]["endTimestampMs"]
end4 = data["timelineObjects"][9]["placeVisit"]["duration"]["endTimestampMs"]
end5 = data["timelineObjects"][11]["placeVisit"]["duration"]["endTimestampMs"]
end6 = data["timelineObjects"][13]["placeVisit"]["duration"]["endTimestampMs"]
end7 = data["timelineObjects"][15]["placeVisit"]["duration"]["endTimestampMs"]
end8 = data["timelineObjects"][17]["placeVisit"]["duration"]["endTimestampMs"]
end9 = data["timelineObjects"][19]["placeVisit"]["duration"]["endTimestampMs"]

end = float(end)/ 1000.0
end = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S.%f')

end1 = float(end1)/ 1000.0
end1 = datetime.datetime.fromtimestamp(end1).strftime('%Y-%m-%d %H:%M:%S.%f')

end2 = float(end2)/ 1000.0
end2 = datetime.datetime.fromtimestamp(end2).strftime('%Y-%m-%d %H:%M:%S.%f')

end3 = float(end3)/ 1000.0
end3 = datetime.datetime.fromtimestamp(end3).strftime('%Y-%m-%d %H:%M:%S.%f')

end4 = float(end4)/ 1000.0
end4 = datetime.datetime.fromtimestamp(end4).strftime('%Y-%m-%d %H:%M:%S.%f')

end5 = float(end5)/ 1000.0
end5 = datetime.datetime.fromtimestamp(end5).strftime('%Y-%m-%d %H:%M:%S.%f')

end6 = float(end6)/ 1000.0
end6 = datetime.datetime.fromtimestamp(end6).strftime('%Y-%m-%d %H:%M:%S.%f')

end7 = float(end7)/ 1000.0
end7 = datetime.datetime.fromtimestamp(end7).strftime('%Y-%m-%d %H:%M:%S.%f')

end8 = float(end8)/ 1000.0
end8 = datetime.datetime.fromtimestamp(end8).strftime('%Y-%m-%d %H:%M:%S.%f')

end9 = float(end9)/ 1000.0
end9 = datetime.datetime.fromtimestamp(end9).strftime('%Y-%m-%d %H:%M:%S.%f')


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



plt.rc('font', size=17) 
x = [name,name1,name2,name3,name4,name5,name6,name7,name8,name9]
y = [end,end1,end2,end3,end4,end5,end6,end7,end8,end9]
plt.xticks(rotation='vertical')
plt.title('Scatter Graph showing the departure time at each location')
plt.scatter(x ,y )

plt.savefig('bank_data.png')

plt.show()

html_str = mpld3.fig_to_html(fig)
Html_file= open("places_visited_index/PVindex1.html","w")
Html_file.write(html_str)
Html_file.close()



activityType= data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][0]["placeId"]
probability = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][0]["placeId"]
activityType1 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][1]["placeId"]
probability1 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][1]["placeId"]
activityType2 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][2]["placeId"]
probability2 =data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][2]["placeId"]
activityType3 =data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][3]["placeId"]
probability3 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][3]["placeId"]
activityType4 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][4]["placeId"]
probability4 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][4]["placeId"]
activityType5 =data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][5]["placeId"]
probability5 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][5]["placeId"]
activityType6 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][6]["placeId"]
probability6 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][6]["placeId"]
activityType7 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][7]["placeId"]
probability7 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][7]["placeId"]
activityType8 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][8]["placeId"]
probability8 = data["timelineObjects"][1]["placeVisit"]["otherCandidateLocations"][8]["placeId"]
fig = plt.figure(figsize = (5,5))



tick_label = [activityType, activityType1, activityType2, activityType3, activityType4, activityType5, activityType6, activityType7, activityType8]
height = [probability, probability1, probability2, probability3, probability4, probability5, probability6,probability7, probability8]
plt.pie(height)

plt.legend(labels = tick_label, title = "Ativity Type:")

plt.show()

html_str = mpld3.fig_to_html(fig)
Html_file= open("activity_index/index4.html","w")
Html_file.write(html_str)
Html_file.close()
