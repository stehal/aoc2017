import unittest

def read(fn):
	with open(fn) as f:
		lines = f.readlines()
	return lines	

def perform(line):
	line_ints = list(map(lambda s: int(s), line.split()))
	return (max(line_ints) -  min(line_ints))

def run(fn):
	r = 0
	for line in read(fn):
		r += perform(line)
	print(r)
    
if __name__ == '__main__':
    run("day2.txt")
    