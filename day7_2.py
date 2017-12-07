import unittest


class TestAoc(unittest.TestCase):
	def test_x(self):
		self.assertEqual(parse("fwft (72) -> ktlj, cntj, xhth"), ["fwft", 72, [ "ktlj", "cntj", "xhth"]])	
		self.assertEqual(parse("fwft (72)"), ["fwft", 72, []])	
		
		#self.assertTrue(True)


def parse(line):
	a = line.split("->")
	fr = a[0].split()[0]
	ws = a[0].split()[1]
	w = int(ws[1:len(ws) - 1])
	if len(a) <2:
		return [fr, w, []] 
	to = list(map(lambda s: s.strip(), a[1].split(",")))

	return [fr, w, to]
	
def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def perform(fn):
	lines = read(fn)

	to = set()
	fr = set()
	tree = {}
	for line in lines:
		a = parse(line)
		fr.add(a[0])
		to.update(a[2])
		tree[a[0]] = (a[1], tuple(a[2]))
	base = list(fr.difference(to))
	weight(base[0], tree)

def weight(base, tree):
	branch_weights = {}
	for branch in tree[base][1]:
		branch_weights[branch] = tree[branch][0] + weight(branch, tree)
	values = list(branch_weights.values())
	if len(set(values)) > 1:
		print(branch_weights)
		for b in branch_weights:
			print(b, tree[b])
		raise Error("XXXX")
	return sum(values)

def run(fn):
	for line in read(fn):
		perform(line)
    
if __name__ == '__main__':
    #unittest.main()
    perform("day7.txt")
