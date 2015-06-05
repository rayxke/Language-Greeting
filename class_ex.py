class Shape:
	def __init__(self, x,y):
		self.x = x
		self.y = y
		self.description = "This shape has not been described yet"
		self.author = "Nobody has claimed to make this shape yet"
		def area(self):
			return self.x * self.y
		def perimeter(self):
			return 2 * self.x + 2 * self.y
		def describe(self, text):
			self.author = text
		def scaleSize(self, scale):
			self.x = self.x * scale
			self.y = self.y * scale
# Inheritance: Using a previously defined class to define another new class. Oh snap this is cool!

class Sqaure(Shape):
	def __init__(self, x):
		self.x = x
		self.y = x
