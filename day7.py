import unittest


class TestAoc(unittest.TestCase):
	def test_x(self):
		self.assertEqual(parse("fwft (72) -> ktlj, cntj, xhth"), ["fwft", [ "ktlj", "cntj", "xhth"]])	
		#self.assertTrue(True)


def parse(line):
	a = line.split("->")
	fr = a[0].split()[0]
	if len(a) < 2:
		return [fr, None] 
	to = list(map(lambda s: s.strip(), a[1].split(",")))

	return [fr, to]
	
def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def perform(fn):
	lines = read(fn)
	to = set()
	fr = set()
	for line in lines:
		a = parse(line)
		fr.add(a[0])
		if a[1]:
			to.update(a[1])
	print(len(fr))
	print(len(to))
	
	print(list(fr.difference(to)))


def run(fn):
	for line in read(fn):
		perform(line)
    
if __name__ == '__main__':
    #unittest.main()
    perform("day7.txt")
    