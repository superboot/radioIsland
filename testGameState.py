import classes as ri

world = ri.World()

house = ri.Location('House', doors=['north'])
field = ri.Location('field', house.north(), doors=['south', 'north'])
barn = ri.Location('Barn', field.west(), doors=['east'])

john = ri.Person('John', 'medium')
lauraBeth = ri.Person('Laura Beth', 'medium')
dad = ri.Person('Dad', 'big')
mom = ri.Person('Mom', 'medium')


player = john

kitchenDoorKey = ri.Item('Kitchen door key', 1, 'metal')

house.inventory.add(kitchenDoorKey)

print(player.location.name)
print(player.location.inventory.list(kitchenDoorKey).material)
player.inventory.add(kitchenDoorKey)
if player.inventory == house.inventory
player.action.goNorth()
print(player.location.name)
print 'The doors of location:', player.location.name, 'are:', player.location.doors
