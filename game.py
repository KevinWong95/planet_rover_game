import sys
import loader

def quit_game():
	##Exits game
	sys.exit()
	
def menu_help():
	##Prints help menu
	print("\nSTART <level file> - Starts the game with a provided file.")
	print("QUIT - Quits the game")
	print("HELP - Shows this message\n")
	menu()

def menu_start_game(filepath):
	##Attempts to begin game, checks if valid file
	try:
		play = loader.load_level(filepath)
		if play == False:
			print("\nUnable to load level file\n")
			menu()
		gameplay(play)
	except IOError:
		print("\nLevel file could not be found\n")
		menu()

def menu():
	##Menu for user inputs
	command = input()
	if command == ('QUIT'):
		quit_game()
	elif command == ('HELP'):
		menu_help()
	elif command[:6] == ('START '):
		menu_start_game(command[6:])
	else:
		print('\nNo menu item\n')
		menu()

def gameplay(play):
	##Valid inputs after the game begins
	command = input()
	if command[:4] == 'MOVE':
		move_specs=command.split(' ')
		play.rover.move(move_specs[1], int(move_specs[2]))
		gameplay(play)
	elif command[:4] == 'WAIT':
		wait_specs=command.split(' ')
		play.rover.wait(int(wait_specs[1]))
		gameplay(play)
	elif command == 'STATS':
		print('\nExplored: ' + str(int(100*play.rover.explored/play.size)) + '%')
		print('Battery: ' + str(play.rover.battery) + '/100\n')
		gameplay(play)
	elif command=='FINISH':
		print('\nYou explored {}% of {}\n'.format(str(int(100*play.rover.explored/play.size)), play.name))
		quit_game()	
	elif command[:4] == 'SCAN':
		scan_specs=command.split(' ')
		
		if scan_specs[1] == 'shade':
			scan_string=''
			
			scan_x = play.rover.x
			scan_y = play.rover.y

			scan_x -= 2
			if scan_x < 0:
				scan_x += play.width
			scan_y -= 2
			if scan_y < 0:
				scan_y += play.height
			holder = scan_x
			for i in range(0, 5):
				scan_x = holder
				new_line='|'
				for j in range(0, 5):
					play.map[scan_y][scan_x].scanned(play.rover)
					if i == 2 and j == 2:
						new_line += 'H|'
					elif play.map[scan_y][scan_x].is_shaded():
						new_line += '#|'
					else:
						new_line += ' |'
					scan_x += 1					
					if scan_x == play.width:
						scan_x = 0
						
				scan_string += new_line + '\n'
				scan_y += 1
				if scan_y == play.height:
					scan_y = 0
			print('\n' + scan_string)
			
		elif scan_specs[1]=='elevation':
			scan_string=''
			scan_x = play.rover.x
			scan_y = play.rover.y
			scan_x -= 2
			if scan_x < 0:
				scan_x += play.width
			holder = scan_x
			scan_y -= 2
			if scan_y < 0:
				scan_y += play.height
				
			for i in range(0, 5):
				new_line='|'
				scan_x = holder
				for j in range(0, 5):
					play.map[scan_y][scan_x].scanned(play.rover)
					if i == 2 and j == 2:
						new_line += 'H|'
					elif isinstance(play.map[scan_y][scan_x].elevation, int) and isinstance(play.rover.elevation, int):
						if play.map[scan_y][scan_x].elevation > play.rover.elevation:
							new_line += '+|'
						elif play.map[scan_y][scan_x].elevation < play.rover.elevation:
							new_line += '-|'
						else:
							new_line += ' |'
					
					elif isinstance(play.map[scan_y][scan_x].elevation, tuple) and isinstance(play.rover.elevation, int):
						if play.map[scan_y][scan_x].elevation[0] < play.rover.elevation:
							new_line += '-|'
						elif play.map[scan_y][scan_x].elevation[1] > play.rover.elevation:
							new_line += '+|'
						elif play.map[scan_y][scan_x].elevation[0] == play.rover.elevation:
							new_line += '\|'
						else:
							new_line += '/|'
					
					elif isinstance(play.map[scan_y][scan_x].elevation, int) and isinstance(play.rover.elevation, tuple):
						if play.map[scan_y][scan_x].elevation < play.rover.elevation[1]:
							new_line += '-|'
						elif play.map[scan_y][scan_x].elevation > play.rover.elevation[0]:
							new_line += '+|'
						else:
							new_line += ' |'
							
					else:
						if play.map[scan_y][scan_x].elevation[0] == play.rover.elevation[1]:
							new_line += '\|'
						elif play.map[scan_y][scan_x].elevation[1] == play.rover.elevation[0]:
							new_line += '/|'
						elif play.map[scan_y][scan_x].elevation[0] == play.rover.elevation[0]:
							new_line += ' |'
						elif play.map[scan_y][scan_x].elevation[0] < play.rover.elevation[1]:
							new_line += '-|'
						else:
							new_line += '+|'
							
					scan_x += 1					
					if scan_x == play.width:
						scan_x = 0
						
				scan_string += new_line + '\n'
				scan_y += 1
				if scan_y == play.height:
					scan_y = 0
					
			print('\n' + scan_string)
		gameplay(play)
	else:
		gameplay(play)
menu()