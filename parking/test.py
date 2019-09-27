from parking_lot import Parking

x=Parking()
x.create_parking_lot(6)
#print(x.slots)

print(' -----------------' )

x.park('ka-41-y-8957','black')
x.park('ka-41-y-8957','black')

print('****************')

x.leave(1)

x.park('ka-41-y-8957','black')
x.park('ka-41-y-8957','black')
print('****************')
print('****************')


x.status()
x.park('ka-41-y-8957','black')

x.registration_numbers_for_cars_wirh_color("black")
x.registration_numbers_for_cars_wirh_color("Black")

x.slot_number_for_cars_wirh_color("black")
x.slot_number_for_cars_wirh_color("Black")

x.slot_number_for_registration_number("ka-41-y-8957")

x.create_parking_lot(6)