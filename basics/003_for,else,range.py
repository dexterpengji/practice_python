target = input("Type in target number(1-1000): ")
print(target)
ll = range(1,1001)

for x in ll:
	if x == int(target):
		print("target = %d found! BREAK!" % x)
		break
	print(x, end=" - ")
else:
	print("scaned all elements, no target found")
	
