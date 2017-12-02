import unittest

class TestAoc(unittest.TestCase):
	def test_x(self):
		self.assertEqual(perform("5 9 2 8"), 4)
		self.assertEqual(perform("9 4 7 3"), 3)
		self.assertEqual(perform("3 8 6 5"), 5)
	
def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def perform(line):
	line_ints = list(map(lambda s: int(s), line.split()))
	line_ints.sort()
	for i in range(len(line_ints)):
		for j in range(i + 1, len(line_ints)):
			if line_ints[j] % line_ints[i] == 0:
				return line_ints[j] / line_ints[i]

def run(fn):
	r = 0
	for line in read(fn):
		r += perform(line)
	print(r)
    
if __name__ == '__main__':
    #unittest.main()
    run("day2.txt")
    