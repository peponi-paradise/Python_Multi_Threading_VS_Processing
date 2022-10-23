from multiprocessing import Process,freeze_support
from threading import Thread
from datetime import datetime

def ProcessThreadFunction():
    print("Process or Thread created")

def ProcessThreadFunctionWithIndex(index):
    print("Process or Thread "+str(index)+" created")

if __name__=="__main__":
    
    freeze_support()

    print("Single worker create test start")

    print(str(datetime.now())+" Create Process start")
    process=Process(target=ProcessThreadFunction)
    process.start()
    process.join()
    print(str(datetime.now())+" Process join done")
    print(str(datetime.now())+" Create Thread start")
    worker=Thread(target=ProcessThreadFunction)
    worker.start()
    worker.join()
    print(str(datetime.now())+" Thread join done")

    print("Single worker create test end")

    print("Multi worker create test start")

    Length_Worker=10
    list_Worker=list()

    print("Process create test start")

    for index in range(Length_Worker):
        print(str(datetime.now())+" Create Process "+str(index)+" start")
        process=Process(target=ProcessThreadFunctionWithIndex,args=(index,))
        list_Worker.append(process)
        process.daemon=True
        process.start()
    
    for index in range(len(list_Worker)):
        list_Worker[index].join()
        print(str(datetime.now())+" Process "+str(index)+" join done")

    print("Process create test end")

    list_Worker.clear()

    print("Thread create test start")

    for index in range(Length_Worker):
        print(str(datetime.now())+" Create Thread "+str(index)+" start")
        worker=Thread(target=ProcessThreadFunctionWithIndex,args=(index,))
        list_Worker.append(worker)
        worker.daemon=True
        worker.start()
    
    for index in range(len(list_Worker)):
        list_Worker[index].join()
        print(str(datetime.now())+" Thread "+str(index)+" join done")

    print("Thread create test end")

    print("Multi worker create test end")