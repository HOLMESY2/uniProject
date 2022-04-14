
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

modified_time = os.path.getmtime(r'uploads/newUpload.json')
convert_time = time.ctime(modified_time)


cursor.execute("""INSERT INTO Time (Date_and_time)VALUES(?)""",[convert_time])
connection.commit()  
query = cursor.execute('SELECT * from Time ORDER BY Date_and_time DESC LIMIT 1, 1')

query = cursor.fetchone()[0]

if query == convert_time:
    print('this is the same file')
    cursor.execute('DROP TABLE IF EXISTS activity')
    cursor.execute('DROP TABLE IF EXISTS places')
    connection.commit()
else:
    print('different files code need to run')
    cursor.execute('DROP TABLE IF EXISTS activity')
    cursor.execute('DROP TABLE IF EXISTS places')
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
   Start Time VARCHAR(20),
   End Time VARCHAR(20)
  );
""")



for d in data["timelineObjects"]:
    #  print(d) d is all the place visits and the actvity segments in the file 
    for line in d:
        if "activitySegment" in line:
         segment = line
         x = d.get("activitySegment")
    #  print(x) x is the first activity segment 
         Y = x.get("activities")
         for mylist in Y:
       
          activitytype = mylist.get('activityType')
          probability = mylist.get('probability')
          probability = int(probability)
          cursor.execute("""
          INSERT INTO activity (Activity,Probability,ActivityId)VALUES(?,?,?)""",[activitytype,probability,segment])
          connection.commit() 
    for  line in d : 
        
        if "placeVisit" in line:
         place = line
         print(place) 
         x = d.get("placeVisit")
         Y = x.get("location")
         name = Y.get('name')
         cursor.execute("""
         INSERT INTO places (Name,Placeid)VALUES(?,?)""",[name,place])
         connection.commit() 
         
         


























#         maxid =cursor.execute("select  _rowid_ from  activity order by _rowid_ desc ")
#         maxid = cursor.fetchone()[0]
                  


#         list = []
#         list1 = []


 


 
#         activity =cursor.execute("select * from activity WHERE Activity = 'IN_PASSENGER_VEHICLE'")
#         activity = cursor.fetchone()[0]
#         list.append(activity)
#         activity =cursor.execute("select * from activity WHERE Activity = 'IN_BUS'")
#         activity = cursor.fetchone()[0]
#         list.append(activity)
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

