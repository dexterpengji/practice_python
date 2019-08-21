# -*- coding: utf-8 -*
my_list = ['element']

# assert异常处理
try:
	assert len(my_list) > 1	# 断言mylist内元素个数大于1
except AssertionError as reason:
	if str(reason):
		print('Error happens, the reason is ' + str(reason))
	else:
		print('Error happens, none reason')

# OSError异常处理
try:
	f = open('non-existFile.txt')
	print(f.read())
	f.close()
except OSError as reason:
	if str(reason):
		print('Error happens, the reason is ' + str(reason))
	else:
		print('Error happens, none reason')