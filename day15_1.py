import struct

def to16b(n):
	return str(bin(n)).split('b')[1].zfill(16)[-16:]

def nextA(n):
	return n * 16807 % 2147483647

def nextB(n):
	return n * 48271 % 2147483647

a = 883
b = 879
count = 0
for i in range(40000000):
	a = nextA(a)
	b= nextB(b)
	if to16b(a) == to16b(b):
		count +=1
		print(i, count)
	
print(count)	

