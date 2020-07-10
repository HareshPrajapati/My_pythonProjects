import datetime
import pytz


print("enter youur name :")
name = input()
print("input number for  what you want to update :")
print("1. Office Intime  ")
print("2. Lunch Intime")
print("3. Lunch Outtime")
print("4. Office Outtime")
print("5. Today Task")

var1 = int(input())

if(var1 == 1):
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    print("Your Updated Office Intime is : ",current_time.hour,":",current_time.minute,":",current_time.second)

if(var1 == 2):
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    print("Your Updated Lunch Intime is : ", current_time.hour, ":", current_time.minute, ":", current_time.second)
if(var1 == 3):
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    print("Your Updated Lunch Outtime is : ", current_time.hour, ":", current_time.minute, ":", current_time.second)
if(var1 == 4):
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    print("Your Updated Office Outtime is : ", current_time.hour, ":", current_time.minute, ":", current_time.second)
if(var1 == 5):
    print("Enter Task You Have Done Today")
    var2 = input()
    print("Your Task is :",var2)
    print("Press 1 for Save and Press 2 for Edit")
    var3 = int(input())
    if(var3==1):
        print("Task is Save")
    if(var3 == 2):
        print("Update Your Task :")
        var4 = input()
        print("Your Task is :", var4)









