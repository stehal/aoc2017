import unittest

class TestAoc(unittest.TestCase):
	def test_parse(self):
		instruct = parse("b inc 5 if a > 1")
		self.assertEqual(instruct, ["b", "inc", 5, "a > 1"])
	def test_eval(self):
		self.assertFalse(eval_comp("a > 0", {}))
		d = {"a": 1}
		self.assertTrue(eval_comp("a > 0", d))
	
	def test_run(self):
		run("day8_tst.txt")
		
def parse(line):
	a = line.split("if")
	comparison = a[1].strip()
	b = a[0].split()
	reg = b[0]
	op = b[1]
	amount = int(b[2])
	return [reg, op, amount, comparison]

def eval_comp(comparison, d):
	a = comparison.split()
	v = d.get(a[0], 0)
	return eval(str(v) + a[1] + a[2])

def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def perform(lines):
	d = {}
	m = []
	for line in lines:
		inst = parse(line)
		if eval_comp(inst[3], d):
			if inst[1] == "inc":
				d[inst[0]] = d.get(inst[0], 0) + inst[2]
			else:
				d[inst[0]] = d.get(inst[0], 0) - inst[2]
		if len(d) > 0:
			m.append(max(d.values()))
	print(max(m))

def run(fn):
	perform(read(fn))
		
if __name__ == '__main__':
    #unittest.main()
    run("day8.txt")
    