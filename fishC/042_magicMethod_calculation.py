# -*- coding: utf-8 -*
class New_int(int):	#inherited from int
	def __add__(self, other):
		return int.__sub__(self, other)
	
	def __sub__(self, other):
		return int.__add__(self, other)

a = New_int(5)
b = New_int(6)

print(a - b)

class Try_int(int):	#wrong
	def __add__(self, other):
		return self + other
		
	def __sub__(self, other):
		return self - other

a = Try_int(5)
b = Try_int(6)
# print(a + b) # unlimited recursives

class Try_new_int(int):
	def __add__(self, other):
		return int(self) + int(other)
		
	def __sub__(self, other):
		return int(self) - int(other)

a = Try_new_int(5)
b = Try_new_int(6)
print(a - b)