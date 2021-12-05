import time
import datetime
print(time.asctime(time.localtime()))
print(time.asctime(time.gmtime()))
temp = datetime.datetime.now()
temp1 = temp.strftime("%H:%M:%S")
print(temp)
print(type(temp1))

while True:
    temp = datetime.datetime.now()
    temp1 = temp.strftime("%H:%M:%S")
    if temp1[3:5] == "39":
        print("yay!")
        break
    else:
        print(temp1)
        continue