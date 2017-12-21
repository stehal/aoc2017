import numpy as np

def l2m(line):
	a = line.split("=>")
	return s2m(a[0]),s2m(a[1]) 

def s2m(s):
	c = []
	for d in s.split("/"):
		e = []
		for f in d.strip():
			e.append(f)
		c.append(e)
	return c

def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def b2x2(m, tt):
	n = len(m)//2
	b = []
	for i in range(n):
		c = []
		for j in range(n):
			c.append( transform([[m[2*i][2*j],m[2*i][2*j+1]],[m[2*i+1][2*j],m[2*i+1][2*j+1]]],tt))
		b.append(c)
	d = []
	for i in range(n):
		for k in range(3):	
			e = []
			for j in range(n):
				e.append(b[i][j][k][0])
				e.append(b[i][j][k][1])
				e.append(b[i][j][k][2])
			d.append(e)
	return d

def b3x3(m, tt):
	n = len(m)//3
	b = []
	for i in range(n):
		c = []
		for j in range(n):
			c.append(transform([[m[3*i][3*j],m[3*i][3*j+1],m[3*i][3*j+2]],[m[3*i+1][3*j],m[3*i+1][3*j+1],m[3*i+1][3*j+2]],[m[3*i+2][3*j],m[3*i+2][3*j+1],m[3*i+2][3*j+2]]],tt))
		b.append(c)
	d = []
	for i in range(n):
		for k in range(4):	
			e = []
			for j in range(n):
				e.append(b[i][j][k][0])
				e.append(b[i][j][k][1])
				e.append(b[i][j][k][2])
				e.append(b[i][j][k][3])
			d.append(e)
	return d

def init(tt):
	t_all = {}
	for t in tt:
		m = t[0]
		for j in range(2):
			m = np.fliplr(m)
			for i in range(4):
				m = np.rot90(m) 
				t_all[m2l(m.tolist())] = t[1]
	return t_all
					
def m2l(m):
	r = []
	for a in m:
		r.append("".join(a))
	return "".join(r)

def transform(m, t_all):
	return t_all[m2l(m)]
	
def trans(fn):
	trans =[]
	for line in read(fn):
		trans.append(l2m(line))
	return trans

if __name__ == '__main__':
	tt = init(trans("day21.txt"))
	m = [[".","#","."],[".",".","#"],["#","#","#"]]
	for i in range(18):
		print(i)
		if len(m) % 2 == 0:
			m = b2x2(m,tt)
		else:
			m = b3x3(m,tt)
	count = 0
	for i in range(len(m)):
		for j in range(len(m)):
			if m[i][j] == "#":
				count +=1
	print(count)    