#Program for generating 1-n Numbers after each and every second
#EvenOddGenFunEx1.py
import threading,time
def even(n):
	print("Name of Sub Thread in even()=",threading.current_thread().name)
	if(n<=0):
		print("Invalid Input")
	else:
		for i in range(1,n+1):
			if(i%2==0):
				print("\tEven Number={}".format(i))
				time.sleep(1)

def odd(n):
	print("Name of Sub Thread in odd()=",threading.current_thread().name)
	if(n<=0):
		print("Invalid Input")
	else:
		for i in range(1,n+1):
			if(i%2!=0):
				print("\tOdd Number={}".format(i))
				time.sleep(1)

#main program
n=int(input("Enter the Number under which you want to generate even/odd numbers? :"))
print("-"*50)
print("Even & Odd Numbers within : {}".format(n))
print("-"*50)
t1=threading.Thread(target=even,args=(n,))
t2=threading.Thread(target=odd,args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()
print("-"*50)
