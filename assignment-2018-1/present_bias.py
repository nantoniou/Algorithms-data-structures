import sys


def open_file(file_path):
	with open(file_path) as input_file:
		for line in input_file:
			[n1, n2, w] = [x for x in line.split()]
			if n1 not in graph:
				graph[n1] = []
			if n2 not in graph:
				graph[n2] = []
			graph[n1].append(n2)
			weights[(n1, n2)] = int(w)
	return


def all_simple_paths_dfs(s, t):
	visited[s] = True
	path.append(s)
	if s == t:
		paths.append(path[:])
	else:
		for v in graph[s]:
			if not visited[v]:
				all_simple_paths_dfs(v, t)
	path.pop()
	visited[s] = False


def find_path_distance_with_b(path, b):
	distance = 0
	edge = [path[0], path[1]]
	distance += weights[edge[0], edge[1]]
	if len(path) > 2:
		for pos in range(1, len(path) - 1):
			edge = [path[pos], path[pos + 1]]
			distance += weights[edge[0], edge[1]] * b
	return distance


def find_min_distance_with_b(paths, b):
	min_distance_path = []
	min_distance = sys.maxsize
	for currentPath in paths:
		current_distance = find_path_distance_with_b(currentPath, b)
		if current_distance < min_distance:
			min_distance = current_distance
			min_distance_path = currentPath[:]

	if b == 1:
		chosen_path_without_b.extend(min_distance_path)
		return

	next_paths = []
	if len(min_distance_path) == 2:
		chosen_path_with_b.extend([min_distance_path[0], min_distance_path[1]])
		return

	chosen_path_with_b.append(min_distance_path.pop(0))
	for path in paths:
		path.pop(0)
		if path[0] == min_distance_path[0]:
			next_paths.append(path)
	find_min_distance_with_b(next_paths, b)


file_path = sys.argv[1]
b = float(sys.argv[2])
start_node = sys.argv[3]
end_node = sys.argv[4]
graph = {}
weights = {}
open_file(file_path)

visited = {k: False for k in graph.keys()}
paths = []

path = []
all_simple_paths_dfs(start_node, end_node)

chosen_path_without_b = []
chosen_path_with_b = []
chosen_path_without_b = []
chosen_path_with_b = []
find_min_distance_with_b(paths, 1)
find_min_distance_with_b(paths, b)
print(chosen_path_without_b, find_path_distance_with_b(chosen_path_without_b, 1))
print(chosen_path_with_b, find_path_distance_with_b(chosen_path_with_b, 1))
