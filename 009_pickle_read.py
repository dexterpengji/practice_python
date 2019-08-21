import pprint, pickle
from pickle_write import Person

with open('009_pickle_write.pkl','rb') as pkl_file:
	
	for x in range(6):
		data = pickle.load(pkl_file)
		pprint.pprint(data)
	
	pengji = pickle.load(pkl_file)
	
print("file closed? - %s" % pkl_file.closed)
print(pengji)

pengji.name = 'pengji+2'
pengji.age = 29
pengji.showInfo()


