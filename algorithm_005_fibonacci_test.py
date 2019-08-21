a, b = 0, 1

for x in range(100):
	a, b = b, a+b
	print(x," ",a)
