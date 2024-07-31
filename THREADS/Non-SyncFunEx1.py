#Program demonstating Multiple threads enters into same function and raises Dead Lock/Race Condition
#Non-SyncFunEx1.py
import threading,time
def multable(n):
	if(n<=0):
		print("{}--{} is invalid input".format(threading.current_thread().name,n))
	else:
		print("-"*50)
		print("{}---Multiplication table of {} ".format(threading.current_thread().name,n))
		print("-"*50)
		for i in range(1,11):
			print("\t{} X {} = {}".format(n,i,n*i))
			time.sleep(1)
		print("-"*50)


#main program
#creating multiple sub threads
t1=threading.Thread(target=multable,args=(10,))
t2=threading.Thread(target=multable,args=(12,))
t3=threading.Thread(target=multable,args=(9,))
t4=threading.Thread(target=multable,args=(19,))
#dispatching the threads
t1.start()
t2.start()
t3.start()
t4.start()