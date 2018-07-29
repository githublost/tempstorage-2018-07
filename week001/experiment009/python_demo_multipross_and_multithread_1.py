#!/usr/bin/env python3

# multi-process
# the 'Proces' class under the 'multiprocessing' encapsulate multi-process operations,
# we can through a program of multi-process version to see it usage:
import os
from multiprocess import Process

def hello(name):
	print('child process: {}'.format(os.getpid()))
	print('Hello ' + name)

def main():
	# notice that: args parameter is passed in as a tuple.
	p = Process(target=hello, args=('multi-process')
	p.start()
	p.join()
	print('parent process: {}'.format(os.getpid()))

if __name__ == '__main__':
	main()
#
# the program above
# first import 'Process' from 'multiprocessing',
# then define a 'hello' function, 
# print 'hello + the value of passed in',
# in 'main' funciton, define a child process by 'Process' class,
# the child process execute 'hello' funciton,
# the passed in parameter is 'multi-process',
# then call 'start()' to start child process,
# at this time, the child process will call 'hello' function,
# and pass in the value 'multi-process' of parameter,
# will back after print current process id and 'hello multi-process'.
# join() method represent that waitting child process finish running,
# then execute continue,
# so program will continue printing parent id after child process return.
# 
# the result:
# child process: 65455  # the number will be random create.
# Hello multi-process
# parent process: 65454  # child pid is closed the parent pid.

# communication between processes
# process have their own independent running space,
# which means that need some sepacial method to 
# implement data exchange between processes.
# 'multiprocessing' module provide 'Pipe' and 'Queue' two methods.
#
# Pipe
# if you think of two processes as sealed boxes, 
# the Pipe is like a Pipe connecting two boxes,
# with this Pipe, can realize simple data exchange between two boxes.
# show the code:
from multiprocessing import Pipe
conn1, conn2 = Pipe()
# Pipe() return a tuple, contains two connections.
# by default, the open pipe is full duplex, 
# meaning you can read and write data in any section,
# write data use send(), read data use recv().
# show example:
from multiprocessing import Process, Pipe
conn1, conn2 = Pipe()

def f1():
	conn1.send('Hello multiprocessing')
def f2():
	data = conn2.recv()
	print(data)
def main():
	Process(target=f1).start()
	Process(target=f2).start()
if __name__ == '__main__':
	main()
# this program started two process, 
# first process write 'hello multiprocessing' to 'pipe' pipeline in f1(),
# second prcess read data from pipe in f2(), and print it.

# Queue
# except Pipe, multiprocessing module also implement a queue structure
# that can be used in mutiple processes.
# the above program is rewirte using Queue.
from multiprocessing import Process, Queue
queue = Queue()
def f1():
	queue.put('Hello multiprocessing')
def f2():
	data = queue.get()
	print(data)
def main():
	Process(target=f1).start()
	Process(target=f2).start()
if __name__ == '__main__':
	main()
# Queue can specify a maximum capactiy at initialization time.
# queue = Queue(maxsize=10)
# in addation, Queue.emtpy() can judge whether queue is empty,
# whether data is readable,
# if return True represent there is no data left.

# process synchronization
# look at this example, have a counter 'i', initial value '0',
# now have ten processes, each process does +1 operation 50 times.
# so the theoretical end result is 500.
#
# this Value object can shared between mutiple processes, 
# and the parameter can be viewed with help(value),
# first parameter is shared data type,
# 'i' refer to ctyps.c_int is integer,
# '0' is the value of Value object shared,
# the share value can through val.value to get in process.
import time
from multiprocessing import Process, Value

def func(val):
	for i in range(50):
		time.sleep(0.01)
		val.value +=1
if __name__ == '__main__':
# multiple processes can't use global variable, multiprocessing provided Value is a broker.
# can implement multiple process share this variable.
	v = Value('i', 0)
	procs = [Process(target=func, args=(v,)) for i in range(10)]
	for p in procs:
		p.start()
	for p in procs:
		p.join()
# since the progression sequence of multiple processes is unpredictable,
# it is possible for several processes to operate +1 for 'i' at the same time,
# however, due to the read and write mechanism of CPU and memory,
# the operation +1 to only one process will be recorded,
# which results in the final result should be less than 500.
# the results of program running 5 times:
# 250
# 269
# 201
# 213
# 
# the correct way is  to do this add a lock for 'i' when the operation +1 every time,
# that is current process operate +1, other processes can't operate it.
# the lock operation from Lock class encapsulated nuder multiprocessing module,
# use acquire() acquire the lock, release() method release the lock.
# the revised code below:
import time
from multiprocessing import Process, Value, Lock
def func(val, lock):
	for i range(50):
		time.sleep(0.01)
		# with lock statement is a shorthand of the following statement
		#
		# lock.acquire()
		# val.value += 1
		# lock.release()
		#
		with lock:
			val.value +=1

if __name__ == '__main__':
	v = value('i', 0)
	# initialize lock
	lock = Lock()
	procs = [Process(target=func, args=(v, lock)) for i in range(10)]
	for p in procs:
		p.start()
	for p in procs:
		p.join()
	print(v.value)
# now the result all 500.

# Pool
# the process pool maintains a fixed number of processes,
# when a tack arrives, a process is taken from the Pool to the process task,
# after processing, the process return to the process Pool.
# 
# a process pool used to print 30 times the number between 0-20.
from multiprocessing import Pool
def f(i):
	print(i, end=' ')
def main():
	# initialize a pool for 3 processes.
	pool = Pool(process=3)
	for i in range(30):
	# call apply() start to processing tack, 
	# pass in the task to handle the function f and parameter i.
		pool.apply(f, (i,))
	pool.close()
	pool.join()
if __name__ == '__main__':
	main()

# multiple threading
# python threading module provide the support for multiple theading,
# it's similar between the interface and multiprocessing provided multi-process interface.
# we can use multi-threading rewrite origin multi-process example below:
import threading
def hello(name):
	# get_ident() function acquire current thread id.
	print('child thread: {}'.format(threading.get_ident()))
def main():
	# initialize a thread, the usage of pass parameter as if using process.
	t = threading.Thread(target=hello, args=('multi-thread'))
	# start thread and wait thread finish, as if Process interface.
	t.start()
	t.join()
	print('main thread: {}'.format(threading.get_ident()))

if __name__ == '__main__':
	main()
