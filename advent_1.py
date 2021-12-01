def get_file_data(filename):
	with open(filename) as star_1_puzzle:
		lines = star_1_puzzle.readlines()
		return [int(line) for line in lines]

def get_increases_from_data(data):
	number_before = 0
	first_line = True
	count = 0
	for number in data:
		if not first_line and number_before < number:
			count += 1

		number_before = number
		first_line = False

	return count

def get_sliding_window_sums(data, window_size):

	sums = []

	for window_end_position in range(len(data)):
		if min(window_end_position+1, window_size) == window_size:
			sum = 0
			for i in range(window_size):
				sum += data[window_end_position - i]

			sums.append(sum)

	return sums


if __name__ == "__main__":
	data = get_file_data("input")
	sliding_window_data = get_sliding_window_sums(data, window_size=3)
	result = get_increases_from_data(sliding_window_data)

	print(result)
