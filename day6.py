import unittest

data = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"

#data = "0 2 7 0"		

def next_j(i, blocks):
	if i == len(blocks) - 1:
		return 0
	return i + 1	

	

def perform(blocks):
	all_variants = set()
	all_variants.add(tuple(blocks))	
	while True:
		for i in range(len(blocks)):
			if blocks[i] == max(blocks):
				break
		amount = blocks[i]
		blocks[i] = 0
		j = next_j(i, blocks)
		while amount > 0:
			blocks[j] += 1
			amount -= 1
			j = next_j(j, blocks)
		if  tuple(blocks) in all_variants:
			break
		all_variants.add(tuple(blocks))	
	print(len(all_variants))
	return blocks

blocks = []
for n in data.split():
		blocks.append(int(n))
	
blocks = perform(blocks)
perform(blocks)