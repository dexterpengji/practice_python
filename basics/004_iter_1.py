import sys

dic1 = {123:"sdfds", "avba":"avba"}
dic2 = {"sdfds":"sdfds", "bntgr":"bntgr"}
dic1.update(dic2)

it = iter(dic1)

while True:
	try:
		print(next(it))
	except StopIteration:
		sys.exit()
