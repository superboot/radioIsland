import classes

library = classes.Location('Library', 100, 100, 100)
bank = classes.Location('Bank', *library.south())


print classes.world
