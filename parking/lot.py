class Slot(object):
	def __init__(self,slot_no=None,is_available=None):
		self.car=None
		self.slot_no=slot_no
		self.is_available=is_available

	@property
	def car(self):
		return self._car

	@car.setter
	def car(self,value):
		self._car= value


	@property
	def slot_no(self):
		return self._slot_no


	@slot_no.setter
	def slot_no(self,value):
		self._slot_no =value


	@property
	def is_available(self):
		return self._is_available

	@is_available.setter
	def is_available(self,value):
		self._is_available=value
