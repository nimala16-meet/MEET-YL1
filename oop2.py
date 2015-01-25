class Animal:
	def __init__(self, name, age, color, size):
		self.name=name
		self.age=age
		self.color=color
		self.size=size
	def print_all(self):
		print(self.name)
		print(self.age)
		print(self.color)
		print(self.size)
	def print_eat(self,food):
		print(" The animal " + self.name + " is eating " + food)
	def print_sleep(self,dream):
		print(" The animal " + self.name + " is dreaming about " + dream)
	def print_study(self,material):
		print(" The animal " + self.name + " is studying " + material)


pig=Animal("Nour Awad", 1, "pink", "huge")
lion=Animal("Tala", 2, "Black", "tiny")

pig.print_all()
pig.print_eat(" pizza ")
pig.print_sleep(" Clothes and parties ")
pig.print_study(" English ")


lion.print_all()
lion.print_eat(" pasta ")
lion.print_sleep(" Human and meat ")
lion.print_study(" Math ")


