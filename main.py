import threading
from random import randint
import time
import pprint
import collections

def roll_many(n,x):
    with open('randnum.txt', 'a') as f:
      for i in range(x):
          roll = randint(1,6)
          f.write('{:.2f}\n'.format(roll))
          print(f"{roll}") #This is just to display the value to the terminal
roll_many(1,1) #if you wana call roll_many remove this comment argg

for x in range(1000000):
    roll_many(1,1)


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=x)
    t2 = threading.Thread(target=roll_many)
    # starting Threads
    t1.start()
    t2.start()
  
    # wait until all the THREADS are completely executed
    t1.join()
    t2.join()
  
    # both threads completely executed
    print("Done!")
