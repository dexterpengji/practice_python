import pprint, pickle

data0 = {'a':[1.265, 'test', 5-4j],
         'b':("string_test", 123, u'Unicode string'),
         'c':{456,789,147,'set'},
         'd':{'router':'NetGear','ISP':'Charter'}
         }

data1 = [1]
data2 = [2]
data3 = [3]
data4 = [4]
data5 = [5]

dataA = ['A']
dataB = ['B']
dataC = ['C']
dataD = ['D']

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age  = age
	def showInfo(self):
		print("My name is {}. I am {} years old.".format(self.name,self.age))

pengji = Person('Pengji',27)
pengji.showInfo()

with open('009_pickle_write.pkl','wb') as pkl_file:
	pickle.dump(data1, pkl_file)
	pickle.dump(data2, pkl_file)
	pickle.dump(data3, pkl_file)
	pickle.dump(data4, pkl_file)
	pickle.dump(data5, pkl_file)
	
	pickle.dump(dataA, pkl_file, -1)

	pickle.dump(pengji, pkl_file)
	
print('file closed? - %s' % pkl_file.closed)
