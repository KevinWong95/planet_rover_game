class Planet:
	def __init__(self, name, width, height, map, rover):
		##Initializes planet with map and rover on it
		self.name = name
		self.width = width
		self.height = height
		self.size = width*height
		self.map = map
		self.rover = rover
	
	