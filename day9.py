import unittest
import re

class TestAoc(unittest.TestCase):
	def test_x(self):
		self.assertEqual(remove_garbage("a<>b"), "ab")
		self.assertEqual(remove_garbage("a<xyz>b"), "ab")
		self.assertEqual(remove_garbage("a<<<<>b"), "ab")
		self.assertEqual(remove_garbage("a<{!>}>b"), "ab")
		self.assertEqual(remove_garbage("a<!!>b"), "ab")
		self.assertEqual(remove_garbage("a<!!!>>b"), "ab")
		self.assertEqual(remove_garbage(r'<{o"i!a,<{i<a>'),"")
		
	def test_remove_bang(self):
		self.assertEqual(remove_bang("<!!>"), "<>")
		self.assertEqual(remove_bang("<{!>}>"), "<{}>")
		self.assertEqual(remove_bang("<!!>"), "<>")
	
	def test_count_groups(self):
		self.assertEqual(count_groups("{}"),1)		
		self.assertEqual(count_groups("{{{}}}"), 6)		
		self.assertEqual(count_groups("{{},{}}"), 5)
		self.assertEqual(count_groups("{{{},{},{{}}}}"), 16)
		self.assertEqual(count_groups("{<a>,<a>,<a>,<a>}"), 1)
		self.assertEqual(count_groups("{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)
		self.assertEqual(count_groups("{{<!!>},{<!!>},{<!!>},{<!!>}}"), 9)
		self.assertEqual(count_groups("{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)

def read(fn):
	with open(fn) as f:
		text = f.read()
	return text	

def remove_bang(text):
	return re.sub("!.","", text)

def count_groups(text):
	text = remove_bang(text)
	text = remove_garbage(text)
	count = 0
	depth = 0
	for c in text:
		if c == "{":
			depth += 1
			count +=depth
		if c == "}":
			depth -= 1
		
	return count

def remove_garbage(text):
	clean = []
	text_no_bang = remove_bang(text)
	garbage = False
	for i, c in enumerate(text_no_bang):
		if c == "<":
			garbage = True
		if text_no_bang[i - 1]  == ">" and i > 0:
			garbage = False
		if not garbage:
			clean.append(c)
	return "".join(clean)	
		
def run(fn):
	text = read(fn)
	return count_groups(text)
    
if __name__ == '__main__':
    #unittest.main()
    print(run("day9.txt"))