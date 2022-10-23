from multiprocessing import Process,Queue,freeze_support
from threading import Thread
from datetime import datetime
import os
from time import sleep

class ProcessData():
    DataName:str
    DataCount:int

    def __init__(self):
        self.DataName=""
        self.DataCount=0

def DefaultProcess(MainQueue:Queue,ProcessQueue:Queue):
    while(True):
        if ProcessQueue.empty()==False:
            Data=ProcessQueue.get()
            print("Received data : "+str(os.getpid())+", "+str(Data.DataName))
            ProcessThreadFunctionWithIndex(MainQueue,Data.DataCount)
        else:
            sleep(0.05)

def ProcessThreadFunctionWithIndex(MainQueue:Queue,CalculateCount):
    worker=Thread(target=CalculateWorker,args=(MainQueue,CalculateCount))
    worker.daemon=True
    worker.start()

def CalculateWorker(MainQueue:Queue,CalculateCount):
    Sum=0
    for index in range(int(CalculateCount)):
        Sum+=1
    MainQueue.put(str(os.getpid())+", "+str(Sum))

if __name__=="__main__":
    
    freeze_support()

    TotalCalculateCount=100000000
    IterCount=3 #리스트로 가정하기 위함
    CPUCount=os.cpu_count()
    list_Worker=list()
    list_WorkerQueue=list()
    MainQueue=Queue()

    print(str(datetime.now())+" Process create and calculate test start")

    for index in range(int(CPUCount)):
        print(str(datetime.now())+" Create Process "+str(index)+" start")
        processQueue=Queue()
        list_WorkerQueue.append(processQueue)
        process=Process(name=str(index),target=DefaultProcess,args=(MainQueue,processQueue))
        list_Worker.append(process)
        process.daemon=True
        process.start()

    CalculateCount=int(TotalCalculateCount/len(list_Worker))
    
    print(str(datetime.now())+" Process start done")

    for Iter in range(IterCount):
        for index in range(len(list_Worker)):
            Data=ProcessData()
            Data.DataCount=CalculateCount
            inputindex=int(index%len(list_Worker))
            Data.DataName=str(Iter)+", "+str(inputindex)
            list_WorkerQueue[inputindex].put(Data)
    print(str(datetime.now())+" All Process data input done")

    for index in range(len(list_Worker)):
        print("Process pid : "+str(list_Worker[index].pid)+", index : "+str(index))

    WaitCount=0

    while(WaitCount<len(list_Worker)*IterCount):
        if MainQueue.empty()==False:
            print("Report arrived "+str(MainQueue.get()))
            WaitCount+=1
        else:
            sleep(0.01)

    print(str(datetime.now())+" Process create and calculate test end")