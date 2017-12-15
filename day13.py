	
def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def caught(layers):
	severity = 0
	for depth, rnge in layers.items():
		if depth % (2*(rnge - 1)) == 0:
			severity += depth * rnge
	return severity	

def perform(lines):
		layers = {}
		for line in lines:
			a =line.split(":")
			layers[int(a[0])] = int(a[1])
		print(layers)
		
		print (caught(layers))
		
	    

if __name__ == '__main__':
    #unittest.main()
    perform(read("day13.txt"))
    