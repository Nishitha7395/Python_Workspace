#Program for generating 1-n Numbers after each and every second
#NumGenOOPEx4.py
import threading,time
class Number:
	def __init__(self,n):
		self.n=n

	def generate(self):
		print("Name of Sub Thread in generate()=",threading.current_thread().name)
		if(self.n<=0):
			print("Invalid Input")
		else:
			print("-"*50)
			print("Numbers within : {}".format(self.n))
			print("-"*50)
			for i in range(1,self.n+1):
				print("\tValue of i={}".format(i))
				time.sleep(1)
			print("-"*50)

#main program
n=int(input("Enter How many numbers you want to generate? :"))
t1=threading.Thread(target=Number(n).generate)
t1.start()