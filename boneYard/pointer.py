class Location(object):
    def __init__(self):
        self.x = 45

house = Location()
house.window = True
barn = house
barn.window = False
print house.window
if barn is house:
    print 'yes'
else:
    print 'no'
