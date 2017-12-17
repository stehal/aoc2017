step = 369
buff = [0]
current_p=0
for i in range(1,2018):
	next_p = ((current_p + step) % i) + 1
	buff.insert(next_p,i)
	current_p= next_p
print(buff[current_p -3: current_p+3] )