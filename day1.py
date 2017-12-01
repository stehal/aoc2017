import unittest

class TestAoc(unittest.TestCase):
	def test_x(self):
		self.assertEqual(perform("1212"), 6)
		self.assertEqual(perform("1221"), 0)
		self.assertEqual(perform("123425"), 4)
		self.assertEqual(perform("123123"), 12)
		self.assertEqual(perform("12131415"), 4)
		
	
def read(fn):
	with open(fn) as f:
		lines = f.read()
	return lines	

def perform(s):
	l = len(s)
	jump = l // 2
	r = 0
	for i in range(l):
		r += compare(s, i, jump)
	return r		

def next(i, jump):
	if i >= jump:
		return  i - jump
	return i + jump

def compare(s, i, jump):
	if s[i] == s[next(i,jump)]:
		return int(s[i])
	return 0


if __name__ == '__main__':
    unittest.main()
    #print(perform(read("day1.txt")))
