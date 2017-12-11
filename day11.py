def read(fn):
	with open(fn) as f:
		lines = f.read()
	return lines	

def dist(dest):
	x = dest[0]
	y = dest[1]
	return max(abs(x), abs(y), abs(y  - x))

def destination(s):
	dir ={"ne":(1,1), "se":(1,0), "s":(0,-1), "sw": (-1,-1), "nw":(-1,0), "n":(0,1)}
	dest=(0,0)
	for d in s.split(","):
		dest= tuple(map(lambda x,y:x+y, dest, dir[d]))
	return dest

s = read("day11.txt")
print(dist(destination(s)))