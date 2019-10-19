import pprint, time, sys

def open_file(file_path):
	square = []
	with open(file_path) as input_file:
		for line in input_file:
			line = line.strip()
			square.append([int(x) for x in line.split(", ")])
	return square


def find_transversals(position):
	for y in range(len(latin_sq)):
		if (y not in y_used) and (latin_sq[y][position] not in transversal):
			if position == len(latin_sq) - 1:
				transversal[position] = latin_sq[y][position]
				transversals[transversal[0]].append(transversal[:])
				transversal[position] = None
				y_used.pop()
				return
			else:
				transversal[position] = latin_sq[y][position]
				y_used.append(y)
				find_transversals(position + 1)
	if position != 0:
		y_used.pop()
	transversal[position] = None
	return


def find_final_transversals(position):
	for current_transversal in transversals[keys[position]]:
		valid = True
		for x in final_transversals:
			for count, y in enumerate(current_transversal):
				if x[count] == y:
					valid = False
		if valid:
			final_transversals.append(current_transversal)
			if position == len(current_transversal) - 1:
				return True
			else:
				if find_final_transversals(position + 1):
					return True
	if len(final_transversals) > 0:
		final_transversals.pop()
	return False


def create_gr_la_square():
	if final_transversals == []:
		del gr_la_square[:]
		return
	for line in range(len(latin_sq)):
			for column in range(len(latin_sq)):
				for final_transversals_line in range(len(final_transversals)):
					if latin_sq[line][column] == final_transversals[final_transversals_line][column]:
						gr_la_square[line].append((latin_sq[line][column], final_transversals[final_transversals_line][0]))


#time1 = time.time()
file_path = sys.argv[1]
latin_sq = open_file(file_path)
y_used = []
transversals = {x:[] for x in latin_sq[0]}
transversal = [None for x in range(len(latin_sq))]
find_transversals(0)
keys = list(transversals.keys())
final_transversals = []
find_final_transversals(0)
gr_la_square = [[] for x in range(len(latin_sq))]
create_gr_la_square()
if len(latin_sq) > 7:
	pprint.pprint(gr_la_square, width = 140)
else:
	pprint.pprint(gr_la_square)
#print((time.time() - time1) /60)
