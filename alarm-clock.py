# inspired by https://www.reddit.com/r/beginnerprojects/comments/4n9hne/project_idea_alarm_clock/
<<<<<<< HEAD
=======
# **********************************************************
#                             (_)(_)
#                             /     \
#                            /       |
#                           /   \  * | - WARNING: MAY RING
#             ________     /    /\__/   LATER THAN EXPECTED
#     _      /        \   /    /
#    / \    /  ____    \_/    /
#   //\ \  /  /    \         /
#   V  \ \/  /      \       /
#       \___/        \_____/
# ************************************************************
>>>>>>> c9eb2dce857aba5faebc69c2e22d73771194c67e
# Version 4.1

from datetime import datetime
import random
import time
import webbrowser

songs = input("Please enter a textfile containing YouTube URLs: ")
ringtones = []
inputF = open(songs, "r")
for line in inputF:
    ringtones.append(line.strip())

yourtime = input("When do you want your alarm to ring? <hr> <min> <am/pm> ")

if int(yourtime.strip().split()[0]) != 12:
    if yourtime.strip().split()[2] == "am":
        yourhour = int(yourtime.strip().split()[0])
    else:
        yourhour = (int(yourtime.strip().split()[0]) + 12) % 24
else:
    if yourtime.strip().split()[2] == "am":
        yourhour = (int(yourtime.strip().split()[0]) + 12) % 24
    else:
        yourhour = int(yourtime.strip().split()[0])

yourmin = int(yourtime.strip().split()[1])

alarm = random.SystemRandom().choice(ringtones)

x = datetime.today()
if yourhour >= x.hour and yourmin > x.minute:
    y = x.replace(day = x.day, hour = yourhour, minute = yourmin)
else:
    y = x.replace(day = x.day + 1, hour = yourhour, minute = yourmin)
delta_t = y - x

secs = delta_t.seconds + 1

print("The current time is " + str(x) + ".")
print("Your alarm will ring in " + str(delta_t) + ".")

def play(url, time):
    time.sleep(time)
    webbrowser.open(url)
    exit(0)

play(alarm, secs)
