set1 = set("123456")
set2 = set("456789")

print("set1\t",set1)
print("set2\t",set2)

print("-\t",set1 - set2)
print("|\t",set1 | set2)
print("&\t",set1 & set2)
print("^\t",set1 ^ set2)

a = {x for x in set1 | set2 if x not in ('147')}
print(a)
