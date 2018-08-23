
class Tile:
		
	def __init__(self, elevation, shaded, position_x, position_y):
		##Initializes tile with specs
		self.occupied = None
		self.elevation = elevation
		self.shaded = shaded
		self.x = position_x
		self.y = position_y
		self.explored = False
	
	
	def elevation(self):
		##Return elevation
		return self.elevation
	
	def is_shaded(self):
		##Returns boolean value 
		return self.shaded

	def set_occupant(self, obj):
		##Moves the rover to this tile if possible based on rover's current location 
		if obj.battery <= 0 and self.shaded:
			return
		if isinstance(self.elevation, int) and isinstance(obj.elevation, int) and self.elevation!=obj.elevation:
			return
		elif isinstance(self.elevation, tuple) and isinstance(obj.elevation, int):
			if obj.elevation != self.elevation[0] and obj.elevation != self.elevation[1]:
				return
		elif isinstance(self.elevation, int) and isinstance(obj.elevation, tuple):
			if obj.elevation[0] != self.elevation and obj.elevation[1] != self.elevation:
				return
		elif isinstance(self.elevation, tuple) and isinstance(obj.elevation, tuple):
			if obj.elevation[0] != self.elevation[1] and obj.elevation[1] != self.elevation[0] and obj.elevation[0] != self.elevation[0] and obj.elevation[1] != self.elevation[1]:
				return

		##Alters stats of the rover if successful move
		obj.elevation = self.elevation
		obj.x = self.x
		obj.y = self.y
		
		if (self.shaded):
			obj.battery -= 1
		if self.explored == False:
			self.explored = True
			obj.explored += 1
	
	def scanned(self, obj):
		if self.explored == False:
			obj.explored += 1
			self.explored = True
	
	def get_occupant(self):
		##Return object on the tile
		return self.occupied