# Globals for the bearings
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self._bearing = bearing
        self.x = x
        self.y = y
        self.map = {
            "NORTH" : [0,1],
            "EAST"  : [1,0],
            "WEST"  : [-1,0],
            "SOUTH" : [0,-1],
        }

        self.bearingMap = {
            "NORTH": ["WEST", "EAST"],
            "EAST":  ["NORTH", "SOUTH"],
            "WEST":  ["SOUTH", "NORTH"],
            "SOUTH": ["EAST", "WEST"],
        }

    def advance(self):
        self.x += self.map[self._bearing][0]
        self.y += self.map[self._bearing][1]

    @property
    def coordinates(self):
        return (self.x,self.y)

    def simulate(self,string):
        for i in string:
            if i == 'L':
                self.turn_left()
            elif i == 'R':
                self.turn_right()
            else:
                self.advance()

    def turn_right(self):
        self._bearing = self.bearingMap[self._bearing][1]

    def turn_left(self):
        self._bearing = self.bearingMap[self._bearing][0]

    @property
    def bearing(self):
        return self._bearing