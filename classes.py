import itertools

class World(object):
    '''This class holds all the information of the gameworld, and is the class from which all others should be derived from.'''
    defaultLocation = None
    locations = {}
    people = []

class Location(World):
    '''Locations describe a place, what's in it, what is connected to it.
    Tiles:
        Tiles are single rooms/places/locations. They have their own inventory (instence of Inventory).
    Doors:
        Doors are pathways to adjacent tiles.'''
    startingTile = (100, 100, 100)
    default = (100, 100, 100)
    def __init__(self, name, positionTuple=startingTile, doors=None):
        self.name = name
        self.position = positionTuple
        self.x = positionTuple[0]
        self.y = positionTuple[1]
        self.z = positionTuple[2]
        if doors:
            self.doors = doors
        else:
            self.doors = []
        self.inventory = Inventory()
        if not World.defaultLocation:
            World.defaultLocation = self
        self.locations[self] = positionTuple
    def addDoor(self, door):
        '''Add one of north, south, east, west, up, or down to the available doors out of the location'''
        self.doors.append(door)
    def north(self):
        '''Returns the coordinates of the tile north of the corrent location'''
        return (self.x, self.y + 1, self.z)
    def south(self):
        '''Returns the coordinates of the tile south of the corrent location'''
        return (self.x, self.y - 1, self.z)
    def east(self):
        '''Returns the coordinates of the tile east of the corrent location'''
        return (self.x + 1, self.y, self.z)
    def west(self):
        '''Returns the coordinates of the tile west of the corrent location'''
        return (self.x - 1, self.y, self.z)
    def up(self):
        '''Returns the coordinates of the tile above the corrent location'''
        return (self.x, self.y, self.z + 1)
    def down(self):
        '''Returns the coordinates of the tile below the corrent location'''
        return (self.x, self.y, self.z - 1)


class Item(World):
    '''Class defining framework for items in the game
    The material should be one of: metal, wood, liquid (more will be added here as we implement them).'''
    count = itertools.count()
    def __init__(self, name=None, weight=1, material='mater', life=2880):
        if not name:
            self.name = 'Item ' + str(Item.count.next())
        else:
            self.name = name
        self.weight = weight
        self.material = material
        self.life = life
        self.health = 100

class Inventory(World):
    '''Keeps track of inventory'''
    def __init__(self):
        self.inventory = {}
    def list(self, item=None):
        '''Returns inventory dict. If supplied with an item name, return value of item from inventory dict if exists.'''
        if item:
            return self.inventory[item.name]
        return self.inventory
    def add(self, itemToAdd):
        '''Add item object to inventory with item.name as key'''
        self.inventory[itemToAdd.name] = itemToAdd
    def delete(self, itemToDel):
        '''Delete item object from inventory with item.name as key'''
        self.inventory[itemToDel.name]

class Person(World):
    '''Person class returns person object with correctly filtered and set attributes.'''
    allNames = []
    def __init__(self, name, size='medium'):
        self.name = name
        World.people.append(self.name)
        try:
            assert size in ('big', 'medium', 'small')
        except AssertionError:
            self.size = 'medium'
        self.inventory = Inventory()
        self.location = World.defaultLocation #Starts the player on the default tile. This will be updated as he moves around.
        self.action = Action(self)

class Action(World):
    '''Collection of function deffinitions describing actions available in the game'''
    def __init__(self, person):
        self.person = person
    # Movement
    def goNorth(self):
        '''Finds tile object with position 1 tile north of players current position, and changes the current position to it.'''
        if 'north' in self.person.location.doors:
            positionToFind = self.person.location.north()
            for key, val in self.locations.items():
                if val == positionToFind:
                    self.person.location = key
    def goSouth(self):
        '''Finds tile object with position 1 tile south of players current position, and changes the current position to it.'''
        if 'south' in self.person.location.doors:
            positionToFind = self.person.location.south()
            for key, val in self.locations.items():
                if val == positionToFind:
                    self.person.location = key
    def goEast(self):
        '''Finds tile object with position 1 tile east of players current position, and changes the current position to it.'''
        if 'east' in self.person.location.doors:
            positionToFind = self.person.location.east()
            for key, val in self.locations.items():
                if val == positionToFind:
                    self.person.location = key
    def goWest(self):
        '''Finds tile object with position 1 tile west of players current position, and changes the current position to it.'''
        if 'west' in self.person.location.doors:
            positionToFind = self.person.location.west()
            for key, val in self.locations.items():
                if val == positionToFind:
                    self.person.location = key
    def goUp(self):
        '''Finds tile object with position 1 tile above players current position, and changes the current position to it.'''
        if 'up' in self.person.location.doors:
            positionToFind = self.person.location.up()
            for key, val in self.locations.items():
                if val == positionToFind:
                    self.person.location = key
    def goDown(self):
        '''Finds tile object with position 1 tile below players current position, and changes the current position to it.'''
        if 'down' in self.person.location.doors:
            positionToFind = self.person.location.down()
            for key, val in self.locations.items():
                if val == positionToFind:
                    self.person.location = key
    def walk(self):
        pass
    def run(self):
        pass
    def jump(self):
        pass
    # Stationary
    def sit(self):
        pass
    def stand(self):
        pass
    #Observations
    def look(self):
        pass
    def inspect(self, itemToInspect):
        pass
    def listen(self):
        pass
    def smell(self):
        pass
    def feel(self):
        pass
    #Mental
    def think(self, topic):
        pass
    def remember(self, noun):
        pass
    #Interaction
    def use(self, item):
        pass
    def drop(self, item):
        pass
    def take(self, item):
        pass
    def talk(self, person):
        pass

class NPC(World):
    pass

## Computer related classes ##
class computer(world):
    def __init__(self):
        pass
        



class filesystem(World):
    def __init__(self):
        pass
