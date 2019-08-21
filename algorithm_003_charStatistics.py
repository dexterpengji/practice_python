str1 = ';lkasjdm;lkjsafkl;jdsal;fjldskajl;kasdf'
print(str1)

seen = []
for cha in str1:
	if cha not in seen:
		seen.append(cha)
		print(cha,str1.count(cha),str1.index(cha))
	else:
		pass
str2 = list(str1)
str2.insert(0,'000')
print(str2)
