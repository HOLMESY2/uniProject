
from select import select
from sqlite3 import Cursor
import sqlite3
from unicodedata import name
import pandas as pd
import json
import matplotlib.pyplot as plt
import os
import time
import sys
import mpld3

from numpy import True_
import os.path

#loads up file as a dictionary
with open("uploads/newUpload.json") as f:
    data=json.load(f)
connection = sqlite3.connect('activity1.db')
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Time(
   Date_and_time varchar(50)
  );
""")

modified_time = os.path.getmtime('uploads/newUpload.json')
convert_time = time.ctime(modified_time)


cursor.execute("""INSERT INTO Time (Date_and_time)VALUES(?)""",[convert_time])
connection.commit()  
query = cursor.execute('SELECT * from Time ORDER BY Date_and_time DESC LIMIT 1, 1')

query = cursor.fetchone()[0]

if query == convert_time:
   
    cursor.execute('DROP TABLE IF EXISTS activity')
    cursor.execute('DROP TABLE IF EXISTS places')
    cursor.execute('DROP TABLE IF EXISTS otherlocation')
    connection.commit()
else:
   
    cursor.execute('DROP TABLE IF EXISTS activity')
    cursor.execute('DROP TABLE IF EXISTS places')
    cursor.execute('DROP TABLE IF EXISTS otherlocation')
    connection.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS activity(
   ActivityId TEXT (30),
   Activity TEXT(200),
   Probability VARCHAR(20)
  );
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS places(
   
   Placeid TEXT (20),
   Name TEXT(200),
   Start_Time VARCHAR(20),
   End_Time VARCHAR(20),
   Location_confidence VARCHAR(100)
  


  );
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS otherlocation(
   
   Name TEXT(200),
   other_location VARCHAR(100),
   otherLprobability VARCHAR(100)

  );
""")



for d in data["timelineObjects"]:
    #  print(d) d is all the place visits and the actvity segments in the file 
    for line in d:
        segment = line
        if "activitySegment" in line:
         cursor.execute("""
         INSERT INTO activity (ActivityId)VALUES(?)""",[segment])
         connection.commit()
         x = d.get("activitySegment")
    #  print(x) x is the first activity segment 
         Y = x.get("activities")
         for mylist in Y:
       
          activitytype = mylist.get('activityType')
          probability = mylist.get('probability')
          probability = int(probability)
          cursor.execute("""
          INSERT INTO activity (Activity,Probability)VALUES(?,?)""",[activitytype,probability])
          connection.commit() 
    for  line in d : 
        place = line

        if "placeVisit" in line:
         cursor.execute("""
         INSERT INTO places (Placeid)VALUES(?)""",[place])
         connection.commit()
         placevisit = d.get("placeVisit")
         
         location = placevisit.get("location")
         duration = placevisit.get("duration")
         other_location = placevisit.get("otherCandidateLocations")
         for mylist in location:
          name = location.get('name')
          locationConf = location.get('locationConfidence')
         
         for mylist in duration:
          starttime = duration.get('startTimestamp') 
          endtime = duration.get('endTimestamp')


         cursor.execute("""
         INSERT INTO places (Name,Start_Time,End_Time,Location_confidence)VALUES(?,?,?,?)""",[name,starttime,endtime,locationConf])
       
         connection.commit() 
         

for d in data["timelineObjects"]:
    for line in d:
        if "placeVisit" in line:
             x = d.get("placeVisit")
        
             other_location = x.get("otherCandidateLocations")
             location = x.get("location")
             name = location.get('name')
             cursor.execute("""
             INSERT INTO otherlocation (Name)VALUES(?)""",[name])
             connection.commit()
             for mylist in other_location:
              Other_location = mylist.get('name') 
              locationConfidence = mylist.get('locationConfidence')
              cursor.execute("""
              INSERT INTO otherlocation (other_location,otherLprobability)VALUES(?,?)""",[Other_location,locationConfidence])
             
              connection.commit() 

             
       
             
             
         
         
        
         
        
        
         
         


























#         maxid =cursor.execute("select  _rowid_ from  activity order by _rowid_ desc ")
#         maxid = cursor.fetchone()[0]
                  


#         list = []
#         list1 = []


 


 

# activity =cursor.execute("select Activity from activity WHERE ActivityId = 'activitySegment'")
# activity = cursor.fetchone()[0]
# print(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'MOTORCYCLING'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'STILL'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'WALKING'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'CYCLING'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'IN_TRAIN'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'IN_SUBWAY'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'FLYING'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'RUNNING'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'IN_FERRY'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'IN_TRAM'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'SKIING'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'SAILING'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)
# #  activity =cursor.execute("select * from activity WHERE Activity = 'IN_VEHICLE'")
# #  activity = cursor.fetchone()[0]
# #  list.append(activity)


 
#         # activity =cursor.execute("select probability from activity WHERE Activity = 'IN_PASSENGER_VEHICLE'")
#         # activity = cursor.fetchone()[0]
#         # list1.append(activity)
#         # activity =cursor.execute("select probability from activity WHERE Activity = 'IN_BUS'")
#         # activity = cursor.fetchone()[0]
#         # list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'MOTORCYCLING'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'STILL'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'WALKING'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'CYCLING'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'IN_TRAIN'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'IN_SUBWAY'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'FLYING'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'RUNNING'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'IN_FERRY'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'IN_TRAM'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'SKIING'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'SAILING'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
# #  activity =cursor.execute("select probability from activity WHERE Activity = 'IN_VEHICLE'")
# #  activity = cursor.fetchone()[0]
# #  list1.append(activity)
#         # fig = plt.figure(figsize = (5,5))

# #  tick_label = [list]
# #  height = [list1]


#         # plt.plot(list1, list)
       


# #  plt.legend( labels =list1, title = "Ativity Type:")

#         # plt.show()

# # html_str = mpld3.fig_to_html(fig)
# # Html_file= open("activity_index_upload/index4.html","w")
# # Html_file.write(html_str)
# # Html_file.close()

 


 

# print(list)
# # print(list1)


       
connection.close

