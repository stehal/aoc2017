import unittest
import math

class TestAoc(unittest.TestCase):
	def test_x(self):
		self.assertEqual(dist( (3,0)), 3)
		self.assertEqual(dist( (0,0)), 0)
		self.assertEqual(dist( (2,-2)), 2)
		self.assertEqual(dist( (-1,-2)), 3)
	def test_dest(self):
		self.assertEqual(destination("ne,ne,ne"), (3,0))
		self.assertEqual(destination("ne,ne,sw,sw"),(0,0))
		self.assertEqual(destination("ne,ne,s,s"), (2,-2))
				
	
def read(fn):
	with open(fn) as f:
		lines = f.read()
	return lines	

def dist( dest):
	x = dest[0]
	y= dest[1]
	return max(abs(x), abs(y), abs(y  - x))
		
dir ={"ne":(1,1), "se":(1,0), "s":(0,-1), "sw": (-1,-1), "nw":(-1,0), "n":(0,1)}

s = read("day11.txt")

def destination(s):
	dest=(0,0)
	distance=[]
	for d in s.split(","):
		dest= tuple(map(lambda x,y:x+y, dest, dir[d]))
		distance.append(dist(dest))
	return max(distance)


print(destination(s))





#if __name__ == '__main__':
    #unittest.main()
    #perform()  