a, b = 0, 1
print(a)

while b < 10:
	print(b)
	a, b = b, a + b
'''
pb	a	b
0	0	1
1	1	1
1	1	2
2	2	3
3	3	5
5	5	8
8	8	13
'''


############################################
a, b = 0, 1
print(0,a)

for x in range(99):
	print(x+1,b)
	a, b = b, a + b
	
	
############################################
a, b = 0, 1
print([0,a], end=",")

for x in range(99):
	print([x+1,b], end=",")
	a, b = b, a + b
