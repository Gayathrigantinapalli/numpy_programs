# def my_add(x):
#     return x+100
# def my_sub(x):
#     return x-100
# if __name__=="__main__":
#     print("task started")
#     y=my_sub(20)
#     print(y)
#     print("task completed")




# import multiprocessing as mp
# from multiprocessing import Process
# def my_add(x):
#     print (x+100)
# def my_sub(x):
#     print (x-100)
# if __name__=="__main__":
#     print("task started")
#     y1=Process(target=my_sub,args=(20,))
#     y2=Process(target=my_add,args=(30,))
#     y1.start()
#     y2.start()
#     y1.join()
#     y2.join()
#     print("task completed")








# import threading
# def my_add(x):
#     print (x+100)
# if __name__=="__main__":
#     print("task started")
#     y1=threading.Thread(target=my_add,args=(20,))
#     y2=threading.Thread(target=my_add,args=(30,))
#     y1.start()
#     y2.start()
#     y1.join()
#     y2.join()
#     print("task completed")







# import multiprocessing
# import time
# def my_sum(a,b):
#     c=a+b
#     print(c)
# if __name__=="__main__":
#     y1=multiprocessing.Process(target=my_sum,args=("a","b"))
#     y1.start()
#     y1.join()
    
#     print("task completed")



