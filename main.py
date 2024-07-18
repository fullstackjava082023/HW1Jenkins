from datetime import datetime

# print current time
print("The date today is: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# print day of the week
day = datetime.now().strftime("%A")
print("Today is: ", day)
    
