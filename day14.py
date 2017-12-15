import functools

def mix(elements, current_pos, length):
	if length == 1:
		return elements
	end_select = current_pos + length  
	if end_select> len(elements):
		select = elements[current_pos:]  
		select.extend(elements[:end_select - len(elements)])
		
		select.reverse()
		append = select[:len(select) - (end_select -len(elements))]
		
		prepend = select[len(append):]
		mid= elements[len(prepend): len(elements) - len(append)]
		prepend.extend(mid)
		prepend.extend(append)
		return prepend
	select =  elements[current_pos: end_select]
	select.reverse()
	r = elements[:current_pos]
	r.extend(select)
	r.extend(elements[current_pos + length:])
	return r

def final_elements(elements, lengths, current_pos, skip):
	for length in lengths:
		elements = mix(elements, current_pos, length)
		current_pos = current_pos + length + skip
		if current_pos > len(elements):
			current_pos = current_pos % len(elements)
		skip += 1
	return elements, current_pos, skip

def ascii_len(lens):
	lengths = []
	for c in lens:
		lengths.append(ord(c))
	lengths.extend([17, 31, 73, 47, 23])
	return lengths

def blocks(elements):
	b = [elements[i:i + 16] for i in range(0, len(elements), 16)]
	return b

def run(input):
	skip = 0
	current_pos = 0
	elements = list(range(256))
	lens = ascii_len(input)
	for i in range(64):
		r = final_elements(elements, lens, current_pos, skip)
		elements = r[0]
		current_pos = r[1]
		skip = r[2]
	return elements

def xor(block):
	return functools.reduce(lambda i, j: i ^ j, block)

def hex_s(n):
	return format(n,'x').zfill(2)

def inputs():
	p = "stpzcrnm"
	inp = []
	for i in range(128):
		inp.append(p + "-" + str(i))
	return inp

def hex_to_bin(c):
	return bin(int(c, 16))[2:].zfill(4)

def adj_to(s, bs):
	adj = []
	
	if s[0] < 127:
		if bs[s[0] + 1][s[1]] == "1":
			adj.append(str(s[0] + 1).zfill(3) + str(s[1]).zfill(3) )
	if s[1] < 127:
		if bs[s[0]][s[1] + 1] == "1":
			adj.append(str(s[0]).zfill(3)+ str(s[1] + 1).zfill(3))
	if s[0] > 0:
		if bs[s[0] - 1] [s[1]] == "1":
			adj.append(str(s[0] - 1).zfill(3) + str(s[1]).zfill(3) )
	if s[1] > 0:
		if bs[s[0]] [s[1] -1] == "1":
			adj.append(str(s[0]).zfill(3) + str(s[1] - 1 ).zfill(3))
	return adj

def parse(line, d):
	a =line.split("<->")
	m = int(a[0])
	if a[1].strip() == '':
		d[m] = set()
		return d
	for b in a[1].split(","):
		n = int(b)
		c = d.get(n, set())
		c.add(m)
		d[n] = c

		c = d.get(m, set())
		c.add(n)
		d[m] = c
	return d

def walk(q, d, s):
	if q in s:
		return s
	s.add(q)
	for p in d[q]:
		walk(p, d, s)

def perform(lines):
	in_groups = set()
	d = {}
	for line in lines:
		d = parse(line,d)
	count = 0
	for q in d:
		s = set()
		if q not in in_groups:
			count += 1
			walk(q, d, s)
			for t in s:
				in_groups.add(t)
	return count

if __name__ == '__main__':
	hshs = []
	for s in inputs():
		elements = run(s)
		bs = blocks(elements)
		sparse_hash = []
		for block in bs:
			sparse_hash.append(xor(block))
		h = []
		for n in sparse_hash:
			h.append(hex_s(n))
		hshs.append(''.join(h))
  
	bs = []
	for h in hshs:
		b = []
		for c in h:
			for i in str(hex_to_bin(c)):
				b.append(i)
		bs.append(b)
	lines = []

	for i in range(128):
		for j in range(128):
			if bs[i][j] == "1":
				line = str(i).zfill(3)+str(j).zfill(3)+" <-> "+','.join(adj_to((i,j), bs))
				lines.append(line)
	print(perform(lines))
