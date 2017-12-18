import string
from queue import Queue
from threading import Thread


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
	reg0 = {"p":0}
	pos0 = 0
	reg1 = {"p":1}
	pos1 = 0
	
	send_to_1 = Queue()
	send_to_0 = Queue()
	
	t0 = Thread(target=duet, args=(0,insts, reg0,pos0,send_to_1, send_to_0,))
	t1 = Thread(target=duet, args=(1,insts, reg1, pos1, send_to_0, send_to_1,))
	t0.start()
	t1.start()



def duet(id, insts, reg, pos, snd_q, rcv_q):
	count = 0
	while True:
		inst = insts[pos].split()
		cmd = inst[0]
		x = inst[1]
		
		if cmd == "set":
			reg[x] = c2i(inst[2],reg)
			pos +=1
		elif cmd == "snd":
			snd_q.put(c2i(x,reg))
			count +=1
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
			try:
				reg[x] = rcv_q.get(True, 0.1)
			except:
				print("id", id ,  count)
				return
			pos +=1
		elif cmd == "jgz":
			if c2i(x,reg) > 0:
				pos += c2i(inst[2],reg)
			else:
				pos +=1

def run(fn):
	return perform(read(fn))
    
if __name__ == '__main__':
    print(run("day18.txt"))
    
    