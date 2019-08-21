import os
path = 'V:\\tvshow\\friends'
for dir in os.listdir(path):
	newpath = path+'\\'+dir
	for file in os.listdir(newpath):
		newname=file[:14]+'.mkv'
		os.rename(os.path.join(newpath,file),os.path.join(newpath,newname))
		print ('ok ------ ', newname)