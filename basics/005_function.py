def printinfo(name = "not spicified", age = "not spicified", sex = "not spicified"):
	print("name: %s" % name, end = "\t")
	print("age: %s" % str(age), end = "\t"*3)
	print("sex: %s" % sex)

printinfo("pengji",27,"male")
printinfo(name = "pengji", age = 27, sex = "male")
printinfo(name = "pengji", age = 27)
printinfo(name = "pengji")

def printinfo( arg1, *vartuple ):
   print ("output: ")
   print (arg1)
   print (vartuple)
   
printinfo("arg1",{516:15616,'asdf':'asdf',156:123})
