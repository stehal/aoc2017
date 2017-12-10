import unittest

lengths =(129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108)
elements = list(range(256))

class TestAoc(unittest.TestCase):
	def test_mix(self):
		self.assertEqual(mix([0,1,2,3,4],0,3), [2,1,0,3,4])
		self.assertEqual(mix([2,1,0,3,4],3,4), [4,3,0,1,2])
		self.assertEqual(mix([4,3,0,1,2],2,1), [4,3,0,1,2])
		self.assertEqual(mix([4,3,0,1,2],1,5), [3,4,2,1,0])
	def test_current(self):
			self.assertEqual(current(0, 3, 0,5), 3)		

	def test_final_elements(self):
		lengths = (3,4, 1, 5)
		self.assertEqual(final_elements([0,1,2,3,4],lengths), [3,4,2,1,0])

	def test_hash(self):
		self.assertEqual(hash([3,4,2,1,0]), 12)	

def mix(elements, current_pos, length):
	if length == 1:
		return elements
	end_select = current_pos + length  
	if end_select > len(elements):
		select = elements[current_pos:]  
		select.extend(elements[:end_select - len(elements)])
		
		select.reverse()
		append = select[:len(select) - (end_select -len(elements))]
		
		prepend = select[len(append):]
		mid= elements[len(prepend): len(elements) - len(append)]
		prepend.extend(mid)
		prepend.extend(append)
		return prepend
	select =  elements[current_pos: end_select]
	select.reverse()
	r = elements[:current_pos]
	r.extend(select)
	r.extend(elements[current_pos + length:])
	return r


def final_elements(elements, lengths):
	current_pos = 0
	skip = 0
	for length in lengths:
		elements = mix(elements, current_pos, length)
		current_pos = current_pos + length + skip
		if current_pos > len(elements):
			current_pos = current_pos % len(elements)
		skip += 1
	return elements

def hash(elements):
	return elements[0] * elements[1]
	
if __name__ == '__main__':
    #unittest.main()
    print(hash(final_elements(elements, lengths)))
    