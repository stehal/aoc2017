import unittest


class TestAoc(unittest.TestCase):
	def test_x(self):
		#self.assertEqual(len(encode(r'""')), 6)
		self.assertTrue(True)
		
	
def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def parse(line, d):
	a =line.split("<->")
	m = int(a[0])
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




def perform():
	lines = read("day12.txt")
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
	print(count)


	return

def run(fn):
	for line in read(fn):
		perform(line)
    
if __name__ == '__main__':
    #unittest.main()
    perform()
    