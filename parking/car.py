class Car(object):
	def __init__(self):
		self._color=None
		self._plate=None
	
	@property
	def plate(self):
		return self._plate

	@plate.setter
	def plate(self,plate):
		self._plate=plate

	@property
	def color(self,color):
		return self._color

	@color.setter
	def color(self,color):
		self._color=color

	@classmethod
	def create(cls,plate,color):
		car_obj=cls()
		car_obj.plate = plate
		car_obj.color =color
		return car_obj


