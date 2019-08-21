# -*- coding: utf-8 -*
import time

class Timer():
	def __init__(self, dua = 0):
		self.t_start = 0
		self.t_stop = 0
		self.is_running = False
		self.duaration = dua
		
	def __str__(self):
		if self.is_running == False:
			if self.duaration == 0:
				return "The timer has no record."
			else:
				return "The time has been stopped. It's %d." % (self.duaration)
		else:
			self.duaration = time.time() - self.t_start
			return "The time is running. It's %d now." % (self.duaration)
	
	__repr__ = __str__
	
	def __add__(self, other):
		tempt = float.__add__(self.duaration, other.duaration)
		print("The sum of time is %f." % tempt)
		tempt_obj = Timer(tempt)
		return tempt_obj
		
	def __sub__(self, other):
		tempt = float.__sub__(self.duaration, other.duaration)
		print("The dif of time is %f." % tempt)
		tempt_obj = Timer(tempt)
		return tempt_obj
		
	def start(self):
		if self.is_running == True:
			print("The timer has been started. No need to start it again.")
		else:
			self.t_start = time.time()
			self.is_running = True
			self.duaration = 0
			print("The timer started.")
		
	def stop(self):
		if self.is_running == False:
			print("The timer is NOT running. Please start it first.")
		else:
			self.t_stop = time.time()
			self.is_running = False
			self.duaration = self.t_stop - self.t_start
			print("The timer stopped.")

t1 = Timer()
t1
t1.start()

time.sleep(1)

t2 = Timer()
t2
t2.start()

time.sleep(3)
t1.stop()
t2.stop()

t1
t2

t1+t2
t1-t2
t1+t2+t2
t2+t2+t2+t2+t2+t2+t2+t2+t2+t2