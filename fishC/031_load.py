# -*- coding: utf-8 -*
import pickle
pickle_file = open('031_mylist.pkl', 'rb')  #rb read binnary
my_list = pickle.load(pickle_file)
print(my_list)