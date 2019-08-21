# -*- coding: utf-8 -*
def hanoi(n,x,y,z):
	global count
	if n == 1:
		print(x, '--->', z)
	else:
		hanoi(n-1, x, z, y) # move the top n-1 layers on x to y
		print(x, '--->', z) # move the bottom layer on x to z
		hanoi(n-1, y, x, z)	# move all layers(n-1) on y to z
	count += 1

count = 0
n = int(input('number of hanoi tower layers:'))
hanoi(n, 'X', 'Y', 'Z')
print('count:%d' % count)