MOVE_WEST = "W"
MOVE_EAST = "E"
MOVE_SOUTH = "S"
MOVE_NORTH = "N"
DROP = "D"

ERR_NO_ARGUMENTS = "Please specify dimension and coordinates"
ERR_NO_COORDINATES = "Please list coordinates"
ERR_INCOMPLETE_COORD = "Parameters are incomplete or not well structured"
ERR_COORD_NOT_IN_GRID = "Not possible, coordinates outside of map dimension"

DIRECTIONS = {
    "x+": MOVE_EAST,
    "x-": MOVE_WEST,
    "y+": MOVE_NORTH,
    "y-": MOVE_SOUTH,
}
