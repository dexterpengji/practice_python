# -*- coding: utf-8 -*
import random as r

class Fish:
	def __init__(self, n):
		self.num = n
		self.x = 100
		self.y = 100
		print("%d fishes are made." % (self.num))
		
	def move(self):
		self.x += r.randint(-5,5) 
		self.y += r.randint(-5,5) 
		print("fish position is %d %d" % (self.x, self.y))
		
class Turtle:
	def __init__(self, n):
		self.num = n
		print("%d turtles are made." % (self.num))

class Pool:
	def __init__(self, num_fish, num_turtle):
		self.fish = Fish(num_fish)
		self.turtle = Turtle(num_turtle)
	
	def print_num(self):
		print("We have %d turtles and %d fishes in the pool." % (self.fish.num, self.turtle.num))

obj_pool = Pool(15,2)
obj_pool.print_num()

# 与继承不同的是
# 1.组合可以在横向上同时生成多个对象
# 2.这些对象都同属于一个母对象
# 3.各个子对象具有各自的属性与方法互不干扰
obj_pool.fish.move()
obj_pool.fish.move()
obj_pool.fish.move()
obj_pool.fish.move()
obj_pool.fish.move()