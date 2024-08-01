import The_Alarm


try:
    set_minutes = int(input("how many (minutes) until the alarm goes off??? "))
except:
    set_minutes = int(input("please enter a number or the program will crash!! "))

try:
    set_seconds = int(input("how many (seconds) until the alarm goes off??? "))
except:
    set_seconds = int(input("please enter a number or the program will crash!! "))

total_seconds = (set_minutes * 60) + set_seconds

The_Alarm.alarm(total_seconds)
