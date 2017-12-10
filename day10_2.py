import unittest
import functools


#elements = list(range(256))
#lengths=(3,4,1,5)
#elements= range(5)

class TestAoc(unittest.TestCase):
	def test_mix(self):
		self.assertEqual(mix([0,1,2,3,4],0,3), [2,1,0,3,4])
		self.assertEqual(mix([2,1,0,3,4],3,4), [4,3,0,1,2])
		self.assertEqual(mix([4,3,0,1,2],2,1), [4,3,0,1,2])
		self.assertEqual(mix([4,3,0,1,2],1,5), [3,4,2,1,0])
		self.assertEqual(mix([4,3,0,1,2],1,0), [4,3,0,1,2])
	
	def test_current(self):
			self.assertEqual(current(0, 3, 0,5), 3)		

	def test_final_elements(self):
		lengths = (3,4,1,5)
		self.assertEqual(final_elements([0,1,2,3,4],lengths,0,0)[0], [3,4,2,1,0])
		self.assertEqual(final_elements([0,1,2,3,4],lengths,0,0)[1], 4)
		self.assertEqual(final_elements([0,1,2,3,4],lengths,0,0)[2], 4)


	def test_ascii_len(self):
		self.assertEqual(ascii_len("1,2,3"), [49,44,50,44,51,17,31,73,47,23])



def mix(elements, current_pos, length):
	if length == 1:
		return elements
	end_select = current_pos + length  
	if end_select> len(elements):
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

def final_elements(elements, lengths, current_pos, skip):
	for length in lengths:
		elements = mix(elements, current_pos, length)
		current_pos = current_pos + length + skip
		if current_pos > len(elements):
			current_pos = current_pos % len(elements)
		skip += 1
	return elements, current_pos, skip



def ascii_len(lens):
	lengths = []
	for c in lens:
		lengths.append(ord(c))
	lengths.extend([17, 31, 73, 47, 23])
	return lengths

def blocks(elements):
	b = [elements[i:i + 16] for i in range(0, len(elements), 16)]
	return b

def run(input):
	skip = 0
	current_pos = 0
	elements = list(range(256))
	#print(elements)
	lens = ascii_len(input)
	for i in range(64):
		print(current_pos, skip)
		r = final_elements(elements, lens, current_pos, skip)
		elements = r[0]
		current_pos = r[1]
		skip = r[2]
	return elements

def xor(block):
	return functools.reduce(lambda i, j: i ^ j, block)

def hex_s(n):
	return format(n,'x').zfill(2)

if __name__ == '__main__':
    #unittest.main()
    elements = run("129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108")
    
    bs = blocks(elements)
    sparse_hash = []
    for block in bs:
    	sparse_hash.append(xor(block))
    h = []
    for n in sparse_hash:
    	h.append(hex_s(n))
    print(''.join(h))
    