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

	pointToLeft = tuple(map(sum, zip(current, (-delta_y, delta_x))))
	if pointToLeft not in visited:
		next = pointToLeft
	else:
		next = tuple(map(sum, zip(current, (delta_x, delta_y))))

	visited[next] = val(next)
	return (current, next, visited[next])

value = 1
while value < 265149:
	t = perform(previous, current)
	previous = t[0]
	current = t[1]
	value = t[2]

print(visited[current])	