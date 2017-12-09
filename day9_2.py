import unittest

class TestAoc(unittest.TestCase):
	def test_x(self):
		self.assertEqual(count_garbage("<>"), 0)
		self.assertEqual(count_garbage("<random characters>"), 17)
		self.assertEqual(count_garbage("<<<<>"), 3)
		self.assertEqual(count_garbage("<{!>}>"), 2)
		self.assertEqual(count_garbage("<!!>"), 0)
		self.assertEqual(count_garbage("<!!!>>"), 0)
		self.assertEqual(count_garbage('<{o"i!a,<{i<a>'), 10)
			
	
def read(fn):
	with open(fn) as f:	
		text = f.read()
	return text	



def count_garbage(text):
	garbage = False
	count = 0
	cancelled = False
	for i, c in enumerate(text):
		if cancelled:
			cancelled = False
			continue
		if c == "!":
			cancelled = True
			continue
		if c == "<" and not garbage:
			garbage = True
			continue
		if c  == ">":
			garbage = False
			continue
		if garbage:
			count += 1
	return count 	
		
def run(fn):
	text = read(fn)
	return count_garbage(text)
    
if __name__ == '__main__':
    #unittest.main()
    print(run("day9.txt"))