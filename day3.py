visited = {(0,0):1, (1,0):1}
previous = (0,0)
current = (1,0)

def adjacent(p):
	adj = set()
	adj.add((p[0], p[1] + 1))
	adj.add((p[0] + 1, p[1]))
	adj.add((p[0] + 1, p[1] + 1))
	adj.add((p[0] + 1, p[1] - 1))
	adj.add((p[0] - 1 , p[1] + 1))
	adj.add((p[0] - 1, p[1] - 1))
	adj.add((p[0], p[1] - 1))
	adj.add((p[0] - 1, p[1]))
	return adj

def val(next):
	r = 0
	for  p in adjacent(next):
		r += visited.get(p, 0)
	return r
	
def perform(previous, current) :
	delta_x = current[0] - previous[0]
	delta_y = current[1] - previous[1]
	
	if delta_x != 0:
		if (current[0], current[1] + delta_x) not in visited:
			next =  (current[0], current[1] + delta_x)
		else:
			next =  (current[0] + delta_x, current[1])

	if delta_y != 0:
		if (current[0]  - delta_y, current[1]) not in visited:
			next =  (current[0] - delta_y, current[1] )
		else:
			next =  (current[0], current[1] + delta_y)

	visited[next] = val(next)
	return (current, next, visited[next])

value = 1
while value < 265149:
	t = perform(previous, current)
	previous = t[0]
	current = t[1]
	value = t[2]

print(visited[current])	