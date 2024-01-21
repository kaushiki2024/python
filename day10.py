"""import time
timestamp = time.strftime('%H')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)"""

"""import time
timestamp = time.strftime('%H')
if(timestamp<12):
   print("good morning")
elif(timestamp>12):
   print("good afternooon") 
elif(timestamp>6):
   print("good evening")  
else:
    print('Good night')"""
   
   
# https://docs.python.org/3/library/time.html#time.strftime


import time
currentTime = int(time.strftime('%H'))   

if currentTime < 12 :
     print('Good morning')
if currentTime > 12 :
     print('Good afternoon')
if currentTime > 6 :
     print('Good evening')