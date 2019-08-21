# -*- coding: utf-8 -*
import pickle
my_list = [123, 3.14, 'pengji', ['another list']]
pickle_file = open('031_mylist.pkl', 'wb') #wb write binnary
pickle.dump(my_list, pickle_file)
pickle_file.close()
