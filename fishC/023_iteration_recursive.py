# -*- coding: utf-8 -*
def fab_1(n): # 迭代 iteration
	n1 = 1
	n2 = 1
	n3 = 1
	
	if n < 1:
		print('wrong input')
		
	while n > 2:
		n3 = n2 + n1
		n1 = n2
		n2 = n3
		n -= 1
	
	return n3

def fab_2(n): # 递归 recursive
	if n < 1:
		print('wrong input')
	
	if n == 1 or n == 2:
		return 1
	else:
		return fab_2(n - 1) + fab_2(n - 2)
		
result1 = fab_1(20)
if result1 != -1:
	print('%d pairs of rabbits were born! # iteration' % result1)
	
result2 = fab_2(20)
if result2 != -1:
	print('%d pairs of rabbits were born! # recursive' % result2)