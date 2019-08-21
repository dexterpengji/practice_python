# -*- coding: utf-8 -*
import random as r

class Fish:
	def __init__(self):
		self.x = 100
		self.y = 100
	
	def move(self):
		self.x += r.randint(-5,5)
		self.y += r.randint(-5,5)
		print("position",self.x,self.y)

class Gold_Fish(Fish):
	def __init__(self):
		#Fish.__init__(self)	# way 1
		super().__init__()		# way 2 - the better one
		self.size = 20
		
	def inflate(self):
		self.size += 10
	
	def shrink(self):
		self.size -= 10

class Carp_Fish(Fish):
	pass

class Salmon_Fish(Fish):
	pass

class Shark_Fish(Fish):
	def __init__(self):
		#Fish.__init__(self)	# way 1
		super().__init__()		# way 2 - the better one
		self.hungry = True
	
	def eat(self):
		if self.hungry:
			print("Hungry...")
			self.hungry = False
		else:
			print("Full...")
		
class Gold_Shark_Fish(Gold_Fish, Shark_Fish):	# 多重继承可能会出现不可预料的bug，尽量不要使用
	pass