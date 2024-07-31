#Program demonstating Multiple threads enters into same function and avoid Dead Lock/Race Condition
#SyncOOPsEx2.py
import threading,time
class Table:
	
	@classmethod
	def getLock(cls):
		#creating Lock object
		cls.L=threading.Lock() #Step-1--create an object of Lock class--here L is Class Level data Member

	def multable(self,n):
		Table.L.acquire() #Step-2
		if(n<=0):
			print("{}--{} is invalid input".format(threading.current_thread().name,n))
		else:
			print("-"*50)
			print("{}---Multiplication table of {} ".format(threading.current_thread().name,n))
			print("-"*50)
			for i in range(1,11):
				print("\t{} X {} = {}".format(n,i,n*i))
				time.sleep(0.5)
			print("-"*50)
		Table.L.release() #Step-3


#main program

Table.getLock() # Call Class Level Method for initiating Lock Object
#creating multiple sub threads
t1=threading.Thread(target=Table().multable,args=(10,))
t2=threading.Thread(target=Table().multable,args=(-12,))
t3=threading.Thread(target=Table().multable,args=(9,))
t4=threading.Thread(target=Table().multable,args=(19,))
#dispatching the threads
t1.start()
t2.start()
t3.start()
t4.start()