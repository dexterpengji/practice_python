# -*- coding: utf-8 -*
class Rectangle:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def getPeri(self):
		return (self.x + self.y)*2
	
	def getArea(self):
		return self.x*self.y

rect = Rectangle(3,4)

print(rect.getPeri())
print(rect.getArea())

# __init__ should return and only return none
# The class below is wrong
class Ex:
	def __init__(self):
		return "content of return"
# obj_Ex = Ex()

# __new__方法在这里的目的可以归结为：
# 1.用__new__来进行重写__new__
# 2.预处理实例化对象时传入的参数
class CapStr(str):
	def __new__(cls, string):
		string = string.upper()
		return str.__new__(cls, string)

a = CapStr("I love Amy.")
print(a)

# __del__ 只有在内存回收机制去删除不需要的实例时，该方法会被调用
# 也就是说，del obj_x 是不会调用 obj_x.__del__() 的
class C:
	def __init__(self):
		print("__init__ is running...")

	def __del__(self):
		print("__del__ is running...")

obj_c = C()
print("wait...")