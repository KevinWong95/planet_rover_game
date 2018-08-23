import terrain
import rover
import planet

def load_level(filename):
	##Opens file and creates list of semi-cleaned strings
	file = open(filename, "r")
	file_lines = file.readlines()
	file.close()
	file_lines = [line.rstrip('\n') for line in file_lines]
	##for line in file_lines:
		##print(line)
	##Checks there are 4 lines under [planet]
	if file_lines[5] != '':
		##print('1')
		return False
	
	##Cleaning the strings for use
	value_holder = []
	for i in range(1, 4):
		value_holder.append(file_lines[i].split(',')[1])
	
	##Checks if planet is big enough
	width = int(value_holder[1])
	height = int(value_holder[2])
	if width < 5 or height < 5:
		##print('2')
		return False
	
	##Checks number of tiles matches dimensions
	if file_lines[len(file_lines)-1] == '':
		del file_lines[-1]
	if len(file_lines)-7 != width*height:
		##print('3')
		return False
	
	##Checks rover initiated in legal location
	rover_spot = (file_lines[4])[6:].split(',')
	rover_spot[0] = int(rover_spot[0])
	rover_spot[1] = int(rover_spot[1])
	if rover_spot[0] < 0 or rover_spot[1] < 0 or rover_spot[0] > width-1 or rover_spot[1] > height-1:
		##print('4')
		return False
	
	##Creates a world map of tiles in the form of a list of lists
	current_line = 7
	map = []

	for i in range(0, height):
		map_row = []
		for j in range (0, width):
			tile_specs = file_lines[current_line].split(',')
			tile_specs[1] = int(tile_specs[1])
			if len(tile_specs) == 3:
				tile_specs[2] = int(tile_specs[2])
			if tile_specs[0] == 'shaded':
				shaded = True
			else:
				shaded = False
	
			if len(tile_specs) == 3:
				if tile_specs[2] >= tile_specs[1]:
					##print('5')
					return False
				map_row.append(terrain.Tile((tile_specs[1], tile_specs[2]), shaded, j, i))
			else:
				map_row.append(terrain.Tile(tile_specs[1], shaded, j, i))
			current_line += 1
		map.append(map_row)
		
	##Creates a rover and planet with stats of initial location
	first_planet = planet.Planet(value_holder[0], width, height, map, None)
	first_rover = rover.Rover(map[rover_spot[1]][rover_spot[0]].elevation, 100, first_planet, rover_spot[0], rover_spot[1])
	first_planet.rover = first_rover
	map[rover_spot[1]][rover_spot[0]].scanned(first_rover)
	
	##Returns planet with the full map
	return first_planet