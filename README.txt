This is Simple 2D virtual world simulator.

The game is representation of collisions, actions and moves made by different entities which have 
strength and health (specified inside their classes).

To add a new entity of specific type, player should chose place on the world then chose
the type of entity that the game should place.

If human is on the board it can be moved by a player using arrows(QWE ASD if on hexworld). 
Rest of entites(animals) move randomly accordingly

to their class specification.
Plants do not move, they randomly spread.

NEXT TURN - makes next turn (entites make their moves, iteractions, collisions)
SAVE - saves current game state (give name of the file by typing herenameoffile.txt in run console)
LOAD - loads game state file (player has to chose the file, it should be one of the files saved previously)
(give name of the file by typing herenameoffile.txt in run console)

i button - gives human immortality
m button - gives human +5 strength
l button - gives human antelope speed (moves 2 fields instead of one)
n button - gives human shield
p button - gives human purification

The hexworld is change by default, it can be change to normal square grid by commenting 5th line in main file
and uncommenting 4th line.