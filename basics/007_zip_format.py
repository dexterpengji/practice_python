list1 = ['nam','sex','age','bir']
list2 = ['Pengji','male  ','27    ','021592']

f = open("007_zip_format.txt","w")
for x in range(int(1)):
	for p,v in zip(list1,list2):
		f.write('What is your {0}? It is {1}. \n'.format(p,v))

	for p,v in zip(list1,list2):
		f.write('What is your %s? It is %s. \n' % (p,v))
		
	print(x)

f.close()
