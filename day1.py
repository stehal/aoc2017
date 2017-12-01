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
		if i >= jump:
			next =  i - jump
		else:
			next = i + jump
		if s[i] == s[next]:
			r += int(s[i])
	return r		

if __name__ == '__main__':
    #unittest.main()
    print(perform(read("day1.txt")))
