#import datetime format
import datetime

# method to set hours
def setHours(hours):
    return hours

# method to set minutes
def setMinutes(minutes):
    return minutes
    
# method to set seconds
def setSeconds(seconds):
    return seconds
    
# set the time combining hours, minutes and seconds
def setTime():
    current = (datetime.time(hours, minutes, seconds))
    return current

# print the time when method called
def showTime():
    print(current, "(H:M:S)")

# user inputs hours, minutes and seconds
hours = int(input("Enter hours value:"))
minutes = int(input("Enter minutes value:"))
seconds = int(input("Enter seconds value:"))

# set the hours, minutes, seconds
setHours(hours)
setMinutes(minutes)
setSeconds(seconds)
# set the current time in setTime(), using the user's input on hours, minutes and seconds
current = setTime()
# print the current time
showTime()

