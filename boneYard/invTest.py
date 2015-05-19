from classes import *

#add some items
hammer = Item('hammer', 2, 'metal', 50000)
coffeeMachine = Item('coffee machine', 2, 'metal', 50000)

#setup some people
john = Person('John', 'medium')

#Add items to inventory
john.inventory.add(hammer)
john.inventory.add(coffeeMachine)

#Interogate inventory
print('output of john.inventory.list()')
print(john.inventory.list())
print('output of john.inventory.list(hammer).name')
print(john.inventory.list(hammer).name)
invlist = []
for key in john.inventory.list():
    invlist.append(key)
print invlist
