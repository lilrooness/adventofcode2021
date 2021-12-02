def get_final_dh(instructions, starting_depth=0, starting_horizontal=0):
	depth = starting_depth
	horizontal = starting_horizontal

	for code, x in instructions:
		if code == "forward":
			horizontal += x
		elif code == "down":
			depth += x
		elif code == "up":
			depth -= x

	return (depth, horizontal)

def get_final_dh_using_aim(instructions, starting_depth=0, starting_horizontal=0, starting_aim=0):
	depth = starting_depth
	horizontal = starting_horizontal
	aim = starting_aim

	for code, x in instructions:
		if code == "forward":
			horizontal += x
			depth += aim * x
		elif code == "down":
			aim += x
		elif code == "up":
			aim -= x

	return (depth, horizontal)

def read_instructions_from_file(filename):
	instructions = []
	with open(filename) as file:
		for line in file.readlines():
			parts = line.split(" ")
			instructions.append((parts[0], int(parts[1])))

	return instructions

def test():
	instructions = [
		("forward", 5),
		("down", 5),
		("forward", 8),
		("up", 3),
		("down", 8),
		("forward", 2)
	]

	(depth, horizontal) = get_final_dh(instructions)
	assert depth * horizontal == 150

	(depth_2, horizontal_2) = get_final_dh_using_aim(instructions)
	assert depth_2 * horizontal_2 == 900
	print("tests passed")

if __name__ == "__main__":
	test()
	instructions = read_instructions_from_file("input_2")
	(depth, horizontal) = get_final_dh(instructions)
	print(depth * horizontal)

	(depth_2, horizontal_2) = get_final_dh_using_aim(instructions)
	print(depth_2 * horizontal_2)



