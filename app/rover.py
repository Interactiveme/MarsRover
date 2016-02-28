from movable import Movable

class Rover(Movable):
    def __init__(self, initial_x, initial_y, initial_heading):
        super(Rover, self).__init__(initial_x, initial_y, initial_heading)
