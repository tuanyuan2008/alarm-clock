# inspired by https://www.reddit.com/r/beginnerprojects/comments/4n9hne/project_idea_alarm_clock/
# Version 4.1

from datetime import datetime
import random
import time
import webbrowser
import os


songs = input("Please enter a textfile containing YouTube URLs: ")
ringtones = []
inputF = open(songs, "r")
for line in inputF:
    ringtones.append(line.strip())
alarm = random.SystemRandom().choice(ringtones)


yourtime = input("When do you want your alarm to ring? <hr> <min> <am/pm> ")
now = datetime.now()
hour = yourtime.strip().split()[0]
minute = yourtime.strip().split()[1]
ampm = yourtime.strip().split()[2]


ringTime = str(now.strftime("%B")[0:3]) + " " + str(now.day) + " " + str(now.year) + " " + str(hour) + ":" + str(minute) + str(ampm).upper()
ringTimeDatetime = datetime.strptime(ringTime, '%b %d %Y %I:%M%p')
timeDifference = ringTimeDatetime - now


print("The current time is " + str(now) + ".")
print("Your alarm will ring at " + hour + ":" + minute + " " + ampm + ".")
time.sleep(timeDifference.total_seconds())
print("Your alarm rang at " + str(datetime.now()))
webbrowser.open(alarm)