from datetime import datetime


TotalCalculateCount=1000000

print(str(datetime.now())+" start")

sum=0
for i in range(TotalCalculateCount):
    sum+=1

print(str(datetime.now())+" end")