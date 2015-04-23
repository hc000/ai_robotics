
#writes array to output.txt
def writeToFile(array):
	f = open('output.txt','w')
	for a in array:
		s=str(a) # converts item to string
		f.write(s+'\n') # python will convert \n to os.linesep
	f.close()

def readFromFile(fname):
	# with open(fname) as fin:
	# 	content = fin.readlines()
	# content = [x.strip('\n') for x in content]
	# print content
	arr =[]
	with open(fname) as fin:
	    for line in fin:
	    	b = line.translate(None, '[,]').rstrip('\n')
	    	c = b.split(' ')
	    	c[1] = c[1].strip()
	    	d = [ int(c[0]), int(c[1])]
	        arr.append(d)
	       
	#print arr

def calculateSpeed(array):
	arr = []

	return  arr


#arr = [[123,123],[123,123],[123,123]]
#writeToFile(arr)

#readFromFile('hexbug-training_video-centroid_data')