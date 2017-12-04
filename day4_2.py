import unittest

class TestAoc(unittest.TestCase):
	def test_x(self):
		self.assertTrue(perform("abcde fghij"))
		self.assertFalse(perform("abcde xyz ecdab"))
		self.assertTrue(perform("a ab abc abd abf abj"))
		self.assertTrue(perform("iiii oiii ooii oooi ooooj"))
		self.assertFalse(perform("oiii ioii iioi iiio"))

def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def perform(line):
	words_list = line.split()
	sorted_words = []
	for word in words_list:
		word_as_chars = []
		for c in word:
			word_as_chars.extend(c)
	
		list.sort(word_as_chars)
		sorted_words.append(tuple(word_as_chars))
	
	return len(words_list) == len(set(sorted_words))

def run(fn):
	r = 0
	for line in read(fn):
		r+= perform(line)
	print(r)

if __name__ == '__main__':
   unittest.main()
   #run("day4.txt")
    