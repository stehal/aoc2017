step = 369
current_p=0
i = 1
result = 0
while i  < 50000001:
	next_p = ((current_p + step) % i ) + 1
	if next_p ==1:
		result = i
	current_p= next_p
	i += 1

print(result)
