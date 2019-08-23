import sys

range_max = int(input("Type in the max of range: "))

class MyNumbers:
	def __iter__(self):
		self.num = 1
		return self
	
	def __next__(self):
		if self.num <= range_max:
			num_next = self.num
			self.num += 1
			return num_next
		else:
			raise StopIteration

myobj = MyNumbers()
myiter = iter(myobj)

while True:
	try:
		print(next(myiter))
	except StopIteration:
		print("Iteration stopped!")
		sys.exit()

