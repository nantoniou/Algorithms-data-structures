import sys

def create_square(numbers):
	square = [[0 for y in range(4)] for x in range(4)]
	for x in numbers:
		square[keys_10[x % 4]][keys_10[x // 4]] = 1
	return square


def already_used(group, groups):
	checking_values = []
	for key in list(groups.keys()):
		if key >= len(group):
			checking_values.append(key)
	already_used_sum = 0
	for z in group:
		for x in checking_values:
			for y in groups[x]:				
				if z in y:
					already_used_sum += 1
					if already_used_sum == len(group):
						return True
	return False


def find_groups():
	groups = {x:[] for x in [1, 2, 4, 8]}
	for case, sq in enumerate([square, square_zipped]): #finding groups of 8
		group_8 = []
		for x in keys_10:
			if sum(sq[x]) + sum(sq[(x + 1) % 4]) == 8:
				if case == 0:
					for z in range(2):
						[group_8.append(keys[y] + keys[(x + z) % 4]) for y in range(4)]
				else:
					for z in range(2):
						[group_8.append(keys[(x + z) % 4] + keys[y]) for y in range(4)]
		if group_8:
			groups[8].append(group_8[:])

	combinations = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]
	combo_cases = []
	for combo in combinations:
		combo_case = []
		for element in combo:
			if element == 1: #finding groups of 4 (2x2 square)
				for row in keys_10:
					for col in keys_10:
						group_4 = [[row, col], [(row + 1) % 4, col], 
						[row, (col + 1) % 4], [(row + 1) % 4, (col + 1) % 4]]
						if (sum([square[x[0]][x[1]] for x in group_4]) == 4 and not 
						already_used([(keys[x[1]] + keys[x[0]]) for x in group_4], groups)):
							groups[4].append([(keys[x[1]] + keys[x[0]]) for x in group_4])
							combo_case.append([(keys[x[1]] + keys[x[0]]) for x in group_4])
			elif element == 2:  #finding groups of 4 (row)
				sq = square
				for row in keys_10:
					group_4_keys = [(keys[x] + keys[row]) for x in keys_10]
					if sum(sq[row]) == 4 and not already_used(group_4_keys, groups):
						groups[4].append(group_4_keys)
						combo_case.append(group_4_keys)
			else:  #finding groups of 4 (column)
				sq = square_zipped
				for row in keys_10:
					group_4_keys_sq_zipped = [(keys[row] + keys[x]) for x in keys_10]
					if sum(sq[row]) == 4 and not already_used(group_4_keys_sq_zipped, groups):
						groups[4].append(group_4_keys_sq_zipped)
						combo_case.append(group_4_keys_sq_zipped)
		groups[4] = []
		combo_cases.append(combo_case)
	groups[4].extend(min(combo_cases, key = len))

	combinations = [[1,2], [2,1]]
	combo_cases = []
	for combo in combinations: #finding groups of 2
		combo_case = []
		for element in combo:
			for row in keys_10:
				for col in keys_10:
					group_2 = [[row, col], [row, (col + 1) % 4]]
					if element == 1:
						sq = square
						group_2_keys = [(keys[x[1]] + keys[x[0]]) for x in group_2]
						if (sum([sq[x[0]][x[1]] for x in group_2]) == 2 and not 
						already_used(group_2_keys, groups)):
							groups[2].append(group_2_keys)
							combo_case.append(group_2_keys)
					else:
						sq = square_zipped
						group_2_keys_sq_zipped = [(keys[x[0]] + keys[x[1]]) for x in group_2]
						if (sum([sq[x[0]][x[1]] for x in group_2]) == 2 and not 
						already_used(group_2_keys_sq_zipped, groups)):
							groups[2].append(group_2_keys_sq_zipped)
							combo_case.append(group_2_keys_sq_zipped)
		groups[2] = []
		combo_cases.append(combo_case)
	groups[2].extend(min(combo_cases, key = len))

	for row in keys_10: #finding groups of 1
		for col in keys_10:
			group_1 = [row, col]
			if (square[group_1[0]][group_1[1]] == 1 and not already_used([keys[group_1[1]] + keys[group_1[0]]], groups)):
				groups[1].append([keys[group_1[1]] + keys[group_1[0]]])
	return groups
				

def find_same_values():
	final_values = []
	for set_of_groups in groups.values():
		if set_of_groups:
			for group in set_of_groups:
				sum_of_values = [0, 0, 0, 0]
				for x in group:
					for position, value in enumerate(x):
						sum_of_values[position] += int(value)
				final_group_values = []
				for pos, sum_of_value in enumerate(sum_of_values):
					if sum_of_value == 0:
						final_group_values.append((pos, 0))
					elif sum_of_value == len(group):
						final_group_values.append((pos, 1))
				final_values.append(final_group_values)
	return final_values


def print_values(final_values):
	final_values = sorted(final_values, 
		key = lambda x: [(len(x), x[y][0], -x[y][1]) for y in range(len(x))])
	numeric_to_abcd = ['A', 'B', 'C', 'D']
	sum_of_letters = 0
	for group in final_values:
		for x in group:
			sum_of_letters += 1
			if x[1] == 0:
				print('~', end = '')
			print(numeric_to_abcd[x[0]], end = '')
		if group != final_values[len(final_values) - 1]:
			print(' \u2228', end = ' ')
	print(' ', sum_of_letters)


keys = ['00', '01', '11', '10']
keys_10 = [0, 1, 3, 2]
square = create_square([int(x) for x in sys.argv[1:]])
square_zipped = list(zip(*square))

if (sum([sum(x) for x in square]) in [0, 16]): #if square only has 0 or 1
	print(square[0][0])
	sys.exit()

groups = find_groups()
final_values = find_same_values()
print_values(final_values)
