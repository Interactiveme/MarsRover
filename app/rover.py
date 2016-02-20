class Rover:
    def __init__(self, initial_x, initial_y, initial_heading):
        self._x = initial_x
        self._y = initial_y
        self._heading = initial_heading

    def rotate_left(self):
        if self._heading == 'N':
            self._heading = 'W'
        elif self._heading == 'E':
            self._heading = 'N'
        elif self._heading == 'S':
            self._heading = 'E'
        elif self._heading == 'W':
            self._heading = 'S'

    def is_heading_west(self):
        return self._heading == 'W'

    def is_heading_north(self):
        return self._heading == 'N'

    def is_heading_south(self):
        return self._heading == 'S'

    def is_heading_east(self):
        return self._heading == 'E'
