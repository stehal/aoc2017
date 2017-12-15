	
def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def caught(layers, pause):
	severity = 0
	for depth, rnge in layers.items():
		if (depth + pause) % (2 * (rnge - 1)) == 0:
			return True
	return False

def perform(lines):
		layers = {}
		for line in lines:
			a =line.split(":")
			layers[int(a[0])] = int(a[1])
		c = True
		pause = 0
		while c:
			pause +=2
			c = caught(layers, pause)
		print(pause)	

		
	    

if __name__ == '__main__':
    #unittest.main()
    perform(read("day13.txt"))
    