from car import Car
from lot import Slot


# {1: {'_is_available': True, '_slot_no': 1, '_car': None}, 2: {'_is_available': False, '_slot_no': 2, '_car':
#  {'_color': 'black', '_plate': 'ka-41-y-8957'}}, 
# 3: {'_is_available': True, '_slot_no': 3, '_car': None}, 4: {'_is_available': True, '_slot_no': 4, '_car': None}, 
# 5: {'_is_available': True, '_slot_no': 5, '_car': None}, 6: {'_is_available': True, '_slot_no': 6, '_car': None}}
class Parking(object):
	def __init__(self):
		self.slots={}

	def create_parking_lot(self,value):
		no_of_spots =int(value)

		if len (self.slots) >0:
			print "slots already created" 
			return
		if no_of_spots >0:
			for i in range(1,no_of_spots+1):
				temp_slot = Slot(slot_no = i, is_available =True)
				self.slots[i] =temp_slot.__dict__

			print "Created a parking lot with %s slots" %no_of_spots

		else:
			print "invalid slot number provided"

		return


	def park(self,plate,color):
		

		available_slot=self.get_next_availabe_slot()
		if available_slot:
			car =Car.create(plate,color).__dict__
			self.slots[available_slot]['_car'] = car
			self.slots[available_slot]['_is_available'] =False
			print "Allocated slot with slot no: %s" %available_slot
		else:
			print "slots full"

	def get_next_availabe_slot(self):
		for k,v in self.slots.items():
			if v['_is_available']==True:
				return k
		return None

	def leave(self,value):
		self.slots[value]['_is_available']=True
		self.slots[value]['_car']=None
		print "Slot no %s is free"%value
		return

	def status(self):
		print"Slot No.  Registation No   color"
		spaces = "        "
		for pos in self.slots:
			if self.slots[pos]['_is_available'] ==False:
				print pos,  spaces+self.slots[pos]['_car']['_plate'],  "    "+self.slots[pos]['_car']['_color']

		return 

	def registration_numbers_for_cars_wirh_color(self,color):

		license_plate = ''

		for pos in self.slots:
				if self.slots[pos]['_car'] is not None and self.slots[pos]['_car']['_color'] == color:
					license_plate +='%s ' % self.slots[pos]['_car']['_plate']

		if license_plate:
			print license_plate
		else:
			print "No car matches the given color"
		return

	def slot_number_for_cars_wirh_color(self,color):
		slot_no = ''
		for pos in self.slots:
				if self.slots[pos]['_car'] is not None and self.slots[pos]['_car']['_color'] == color:
					slot_no +='%s ' % self.slots[pos]['_slot_no']

		if slot_no:
			print slot_no
		else:
			print "No car matches the given color"
		return


	def slot_number_for_registration_number(self,plate):
		slot_no = ''
		for pos in self.slots:
				if self.slots[pos]['_car'] is not None and self.slots[pos]['_car']['_plate'] == plate:
					slot_no +='%s ' % self.slots[pos]['_slot_no']

		if slot_no:
			print slot_no
		else:
			print "No car matches the given number"
		return

