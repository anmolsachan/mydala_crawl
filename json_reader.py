import json

def reader(filename):
	with open(filename,"r") as fil:
		data=fil.read()
		return(json.loads(data))



#if __name__ == '__main__':
#	filename=""
#	reader(filename)