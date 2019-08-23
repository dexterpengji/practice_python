with open("007_zip_format.txt","r") as f:
	print(f.readline()[:-1], end='\t-print\n')
	print(f.readline()[:-1], end='\t-print\n')
	print(f.readline()[:-1], end='\t-print\n')

	for line in f:
		print(line[:-1], end='\t-for\n')

print("file closed? - %s" % f.closed)
