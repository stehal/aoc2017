import unittest


class TestAoc(unittest.TestCase):
	def test_x(self):
		self.assertTrue(perform("aa bb cc dd ee"))
		self.assertFalse(perform("aa bb cc dd aa"))
		self.assertTrue(perform("aa bb cc dd aaa"))
			
	
def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def perform(line):
	list_of_words = line.split()
	set_of_words = set(list_of_words)
	return len(list_of_words) == len(set_of_words)

def run(fn):
	r = 0
	for line in read(fn):
		if perform(line):
			r+=1
	print(r)

if __name__ == '__main__':
   #unittest.main()
   run("day4.txt")
    