import planet

class Rover:
	def __init__(self,elevation,battery,planet,x,y):
		##Initializes the rover with specs pertaining to current tile.
		self.x = x
		self.y = y
		self.elevation = elevation
		self.planet = planet
		self.battery = 100
		self.explored = 0
	
	def move(self, direction, cycles):
		##Moves in direction by using terrain set method
		##Checks if went around world
		if direction == 'N':
			for i in range (0, cycles):
				if self.y <= 0:
					self.planet.map[self.planet.height-1][self.x].set_occupant(self)
				else:
					self.planet.map[self.y-1][self.x].set_occupant(self)
			
		elif direction == 'S':
			for i in range (0, cycles):
				if self.y >= self.planet.height-1:
					self.planet.map[0][self.x].set_occupant(self)
				else:
					self.planet.map[self.y+1][self.x].set_occupant(self)
				
		elif direction == 'E':
			for i in range (0, cycles):
				if self.x >= self.planet.width-1:
					self.planet.map[self.y][0].set_occupant(self)
				else:
					self.planet.map[self.y][self.x+1].set_occupant(self)
				
		elif direction == 'W':
			for i in range (0, cycles):
				if self.x <= 0:
					self.planet.map[self.y][self.planet.width-1].set_occupant(self)
				else:
					self.planet.map[self.y][self.x-1].set_occupant(self)
	
	def wait(self, cycles):
		##Boolean variable used to see if battery charges
		if not self.planet.map[self.y][self.x].is_shaded():
			self.battery += cycles
			if self.battery>100:
				self.battery=100