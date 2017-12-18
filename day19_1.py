import string

def c2i(s, reg):
	try: 
		int(s)
		return int(s)
	except ValueError:
		return reg[s]
	
def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def perform(insts):
	reg = {}
	pos = 0
	last_freq = 0
		
	while True:
		inst = insts[pos].split()
		cmd = inst[0]
		x = inst[1]
		
		if cmd == "set":
			reg[x] = c2i(inst[2],reg)
			pos +=1
		elif cmd == "snd":
			last_freq = c2i(x,reg)
			pos +=1

		elif cmd == "add":
			reg[x] = reg.get(x, 0) + c2i(inst[2],reg)
			pos +=1

		elif cmd == "mul":
			reg[x] = reg.get(x, 0) * c2i(inst[2],reg)
			pos +=1

		elif cmd == "mod":
			reg[x] = reg.get(x, 0) % c2i(inst[2],reg)
			pos +=1

		elif cmd == "rcv":
			if c2i(x,reg) > 0:
				return last_freq
			pos +=1
		elif cmd == "jgz":
			if c2i(x,reg) > 0:
				pos += c2i(inst[2],reg)
			else:
				pos +=1

def run(fn):
	return perform(read(fn))
    
if __name__ == '__main__':
    print(run("day19.txt"))