from multiprocessing import Process,freeze_support
from threading import Thread
from datetime import datetime
import os


def ProcessThreadFunctionWithIndex(index,CalculateCount):
    print("Process or Thread "+str(index)+" created")
    Sum=0
    for index in range(int(CalculateCount)):
        Sum+=1

if __name__=="__main__":
    
    freeze_support()

    print("Multi worker create and calculate test start")

    TotalCalculateCount=100000000
    CPUCount=os.cpu_count()
    CalculateCount=TotalCalculateCount/CPUCount
    list_Worker=list()

    print("Process create and calculate test start")

    for index in range(CPUCount):
        print(str(datetime.now())+" Create Process "+str(index)+" start")
        process=Process(target=ProcessThreadFunctionWithIndex,args=(index,CalculateCount))
        list_Worker.append(process)
        process.daemon=True
        process.start()
    
    for index in range(len(list_Worker)):
        list_Worker[index].join()
        print(str(datetime.now())+" Process "+str(index)+" join done")

    print("Process create and calculate test end")

    list_Worker.clear()

    print("Thread create and calculate test start")

    for index in range(CPUCount):
        print(str(datetime.now())+" Create Thread "+str(index)+" start")
        worker=Thread(target=ProcessThreadFunctionWithIndex,args=(index,CalculateCount))
        list_Worker.append(worker)
        worker.daemon=True
        worker.start()
    
    for index in range(len(list_Worker)):
        list_Worker[index].join()
        print(str(datetime.now())+" Thread "+str(index)+" join done")

    print("Thread create and calculate test end")

    print("Multi worker create and calculate test end")