	
def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def perform(insts):
	i = 0
	steps = 0
	while i >= 0 and i < len(insts):
		start = i
		jump = insts[i]

		i = i + jump
		if jump > 2 :
			insts[start] -=1
		else:
			insts[start] +=1
		steps += 1 
	return steps

def run(fn):
	insts = []
	for line in read(fn):
		insts.append(int(line))
	return perform(insts)

    
if __name__ == '__main__':
    #print(perform([0,3,0,1,-3]))
    print(run("day5.txt"))	
    