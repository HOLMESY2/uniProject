import json
import matplotlib.pyplot as plt
import mpld3

with open("Data/2021_NOVEMBER.json") as f:
 data = json.load(f)


confirmation = data["timelineObjects"][1]["placeVisit"]["editConfirmationStatus"]
name = data["timelineObjects"][1]["placeVisit"]["location"]["name"]
confirmation1 = data["timelineObjects"][3]["placeVisit"]["editConfirmationStatus"]
name1 = data["timelineObjects"][3]["placeVisit"]["location"]["name"]
confirmation2 = data["timelineObjects"][5]["placeVisit"]["editConfirmationStatus"]
name2 = data["timelineObjects"][5]["placeVisit"]["location"]["name"]
confirmation3 = data["timelineObjects"][7]["placeVisit"]["editConfirmationStatus"]
name3 = data["timelineObjects"][7]["placeVisit"]["location"]["name"]
confirmation4 = data["timelineObjects"][9]["placeVisit"]["editConfirmationStatus"]
name4 = data["timelineObjects"][9]["placeVisit"]["location"]["name"]
confirmation5 = data["timelineObjects"][11]["placeVisit"]["editConfirmationStatus"]
name5 = data["timelineObjects"][11]["placeVisit"]["location"]["name"]
confirmation6 = data["timelineObjects"][13]["placeVisit"]["editConfirmationStatus"]
name6 = data["timelineObjects"][13]["placeVisit"]["location"]["name"]
confirmation7 = data["timelineObjects"][15]["placeVisit"]["editConfirmationStatus"]
name7 = data["timelineObjects"][15]["placeVisit"]["location"]["name"]
confirmation8 = data["timelineObjects"][17]["placeVisit"]["editConfirmationStatus"]
name8 = data["timelineObjects"][17]["placeVisit"]["location"]["name"]
confirmation9 = data["timelineObjects"][19]["placeVisit"]["editConfirmationStatus"]
name9 = data["timelineObjects"][19]["placeVisit"]["location"]["name"]

fig = plt.figure(figsize = (15,8))
plt.rc('font', size=12) 
plt.title('User confirmation status of correct location')
plt.xticks(rotation=30, ha ="right")
y = [confirmation,confirmation1,confirmation2,confirmation3,confirmation4,confirmation5,confirmation6,confirmation7,confirmation8,confirmation9]
x = [name,name1,name2,name3,name4,name5,name6,name7,name8,name9]
plt.bar(x, y)
plt.show()


