import csv 
from matplotlib import pyplot as plt
from datetime import datetime

dv = "Data/death_valley_2014.csv"
with open(dv) as file_object:
    read = csv.reader(file_object)
    heading = next(read)
    
    dates, maximum, minimum = [], [], []
    
    for info in read:
        try:
            current_date = datetime.strptime(info[0], "%Y-%m-%d")
            the_max = int(info[1]) 
            the_min = int(info[3])
        except ValueError:
            print(current_date,"unobtainable!\n".title()) 
        else:
            dates.append(current_date)
            maximum.append(the_max)
            minimum.append(the_min) 

statistic = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, maximum, c="Red", alpha = 0.75) 
plt.plot(dates, minimum, c="Teal", alpha = 0.5)
plt.fill_between(dates, maximum, minimum, facecolor="Black", alpha=0.08)

title = "Daily Maximum and Minimum Temperatures, 2014\nDeath Valley, CA."
plt.title(title, size=24) 
plt.xlabel('', size=12)
statistic.autofmt_xdate()
plt.ylabel("Temperature (Farenheight)", size=12) 
plt.tick_params(axis="both", which="major", labelsize=10)
plt.ylim(ymin=0, ymax=120) 
plt.margins(x=0)

si = "Data/sitka_weather_2014.csv"
with open(si) as file_object:
    read = csv.reader(file_object)
    heading = next(read)
    
    dates, maximum, minimum = [], [], []
    
    for info in read:
        try:
            current_date = datetime.strptime(info[0], "%Y-%m-%d")
            the_max = int(info[1]) 
            the_min = int(info[3])
        except ValueError:
            print(current_date,"unobtainable!\n".title()) 
        else:
            dates.append(current_date)
            maximum.append(the_max)
            minimum.append(the_min) 

statistic = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, maximum, c="Gold", alpha = 0.5) 
plt.plot(dates, minimum, c="Teal", alpha = 0.75)
plt.fill_between(dates, maximum, minimum, facecolor="Black", alpha=0.08)

title = "Daily Maximum and Minimum Temperatures, 2014\nSitka, CA."
plt.title(title, size=24) 
plt.xlabel('', size=12)
statistic.autofmt_xdate()
plt.ylabel("Temperature (Farenheight)", size=12) 
plt.tick_params(axis="both", which="major", labelsize=10) 
plt.ylim(ymin=0,ymax=120)
plt.margins(x=0)

#Test V--------------------------------------
place = "Data/san francisco 2014.csv"
with open(place) as file_object:
    read = csv.reader(file_object)
    heading = next(read)
    
    dates, high, low = [], [], []
    

    for info in read:
        try:
            current_date = datetime.strptime(info[1], "%Y-%m-%d")
            highs = int(info[2]) 
            lows = int(info[3])
        except ValueError:
            pass 
        else:
            dates.append(current_date)
            high.append(highs)
            low.append(lows) 

    
stats = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, high, c="Red", alpha = 0.5) 
plt.plot(dates, low, c="Teal", alpha = 0.5)
plt.fill_between(dates, high, low, facecolor="Gray", alpha=0.08)

title = "Daily Maximum and Minimum Temperatures, 2014\nSan Francisco, CA."
plt.title(title, size=24) 
plt.xlabel('', size=12)
statistic.autofmt_xdate()
plt.ylabel("Temperature (Farenheight)", size=12) 
plt.tick_params(axis="both", which="major", labelsize=10) 
plt.margins(x=0)


place = "Data/chernobyl_2020.csv"
with open(place) as file_object:
    read = csv.reader(file_object)
    heading = next(read)
    
    dates, high, low = [], [], []
    

    for info in read:
        try:
            current_date = datetime.strptime(info[1], "%Y-%m-%d")
            highs = int(info[22]) 
        except ValueError:
            pass 
        else:
            dates.append(current_date)
            high.append(highs)
            

for index in enumerate(heading):
    print(index)
            
    
stats = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, high, c="Blue", alpha = 1) 

title = "Chernobyl's Radiation."
plt.title(title, size=24) 
plt.xlabel('', size=12)
statistic.autofmt_xdate()
plt.ylabel("Radiation Level", size=12) 
plt.tick_params(axis="both", which="major", labelsize=10) 
plt.margins(x=0)

plt.show()
