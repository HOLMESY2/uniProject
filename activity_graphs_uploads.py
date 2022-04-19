
from re import X
from select import select
from sqlite3 import Cursor
import sqlite3
from unicodedata import name
from matplotlib import axes
import pandas as pd
import json
import matplotlib.pyplot as plt
import os
import time
import sys
import mpld3
import numpy as np
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

             
       
             
             
         
         
        
         
        
        
         
         
















def graph_data():
    cursor.execute("SELECT Activity, Probability FROM activity WHERE Activity = 'IN_PASSENGER_VEHICLE'  ")
    x = []
    y = []
    for row in cursor.fetchall():
        x.append(row[0])
        y.append(row[1])
        
    fig = plt.figure(figsize =(7, 7))
    plt.pie(y,labels =  y,startangle = 90)
    plt.title("IN_PASSENGER_VEHICLE")
    plt.axis('equal')
   
    html_str = mpld3.fig_to_html(fig)
    Html_file= open("activity_index_upload/index1.html","w")
    Html_file.write(html_str)
    Html_file.close()
graph_data()
 

def graph_data():
    cursor.execute("SELECT Activity, Probability FROM activity WHERE Activity = 'IN_BUS'  ")
    x = []
    y = []
    for row in cursor.fetchall():
        x.append(row[0])
        y.append(row[1])
        
    fig = plt.figure(figsize =(7, 7))
    plt.pie(y,labels =  y,startangle = 90, 
        wedgeprops = {"edgecolor" : "black",
                      'linewidth': 0.5,
                      'antialiased': True})
    plt.title("IN_BUS")
    plt.axis('equal')

    html_str = mpld3.fig_to_html(fig)
    Html_file= open("activity_index_upload/index2.html","w")
    Html_file.write(html_str)
    Html_file.close()
graph_data()
def graph_data():
    cursor.execute("SELECT Activity, Probability FROM activity WHERE Activity = 'MOTORCYCLING'  ")
    x = []
    y = []
    for row in cursor.fetchall():
        x.append(row[0])
        y.append(row[1])
        
    fig = plt.figure(figsize =(7, 7))
    plt.pie(y,labels =  y,startangle = 90, 
        wedgeprops = {"edgecolor" : "black",
                      'linewidth': 0.5,
                      'antialiased': True})
    plt.title("MOTORCYCLING")
    plt.axis('equal')

    html_str = mpld3.fig_to_html(fig)
    Html_file= open("activity_index_upload/index3.html","w")
    Html_file.write(html_str)
    Html_file.close()
graph_data()
def graph_data():
    cursor.execute("SELECT Activity, Probability FROM activity WHERE Activity = 'STILL'  ")
    x = []
    y = []
    for row in cursor.fetchall():
        x.append(row[0])
        y.append(row[1])
        
    fig = plt.figure(figsize =(7, 7))
    plt.pie(y,labels =  y,startangle = 90, 
        wedgeprops = {"edgecolor" : "black",
                      'linewidth': 0.5,
                      'antialiased': True})
    plt.title("STILL")
    plt.axis('equal')
 
    html_str = mpld3.fig_to_html(fig)
    Html_file= open("activity_index_upload/index4.html","w")
    Html_file.write(html_str)
    Html_file.close()
graph_data()
def graph_data():
    cursor.execute("SELECT Activity, Probability FROM activity WHERE Activity = 'WALKING'  ")
    x = []
    y = []
    for row in cursor.fetchall():
        x.append(row[0])
        y.append(row[1])
        
    fig = plt.figure(figsize =(7, 7))
    plt.pie(y,labels =  y,startangle = 90, 
        wedgeprops = {"edgecolor" : "black",
                      'linewidth': 0.5,
                      'antialiased': True})
    plt.title("WALKING")
    plt.axis('equal')
    
    html_str = mpld3.fig_to_html(fig)
    Html_file= open("activity_index_upload/index5.html","w")
    Html_file.write(html_str)
    Html_file.close()
graph_data()
def graph_data():
    cursor.execute("SELECT Activity, Probability FROM activity WHERE Activity = 'CYCLING'  ")
    x = []
    y = []
    for row in cursor.fetchall():
        x.append(row[0])
        y.append(row[1])
        
    fig = plt.figure(figsize =(7, 7))
    plt.pie(y,labels =  y,startangle = 90, 
        wedgeprops = {"edgecolor" : "black",
                      'linewidth': 0.5,
                      'antialiased': True})
    plt.title("CYCLING")
    plt.axis('equal')
   
    html_str = mpld3.fig_to_html(fig)
    Html_file= open("activity_index_upload/index6.html","w")
    Html_file.write(html_str)
    Html_file.close()
graph_data()

def graph_data():
    cursor.execute("SELECT Name, Start_Time FROM places  ")
    x = []
    y = []
    for row in cursor.fetchall():
        x.append(row[0])
        y.append(row[1])
        
    fig = plt.figure(figsize =(18, 12))
    plt.scatter(y,x)
    plt.title("The time the user started at each location")
    plt.xticks(rotation=90, ha ="right")
    plt.xticks(y)
    spacing = 0.300
    fig.subplots_adjust(bottom=spacing)
   
    fig.savefig("activity_index_upload/index7.png")
graph_data()
def graph_data():
    cursor.execute("SELECT Name, End_Time FROM places  ")
    x = []
    y = []
    for row in cursor.fetchall():
        x.append(row[0])
        y.append(row[1])
        
    fig = plt.figure(figsize =(18, 12))
    plt.scatter(y,x)
    plt.title("The time the user finished at each location ")
    plt.xticks(rotation=90, ha ="right")
    plt.xticks(y)
    spacing = 0.300
    fig.subplots_adjust(bottom=spacing)
   
   
    fig.savefig("activity_index_upload/index8.png")
graph_data()

def graph_data():
    cursor.execute("SELECT Name, Location_confidence FROM places  ")
    x = []
    y = []
    for row in cursor.fetchall():
        x.append(row[0])
        y.append(row[1])
        
    fig = plt.figure(figsize =(18, 8))
    plt.scatter(y,x)
    plt.title("The location confidence taken from each loation the user has visited ")
    plt.xticks(rotation=90, ha ="right")
    
    fig.savefig("activity_index_upload/index10.png")
    
graph_data()






 



       
connection.close

