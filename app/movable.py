class Movable(object):
    def __init__(self, initial_x, initial_y, initial_heading):
        self._x = initial_x
        self._y = initial_y
        self._heading = initial_heading
        self.directions = ['N', 'E', 'S', 'W']
        self._forwards_movements = {
            'N': self._increment_y,
            'E': self._increment_x,
            'S': self._decrement_y,
            'W': self._decrement_x
        }


    def _increment_x(self):
        self._x += 1


    def _increment_y(self):
        self._y += 1


    def _decrement_x(self):
        self._x -= 1


    def _decrement_y(self):
        self._y -= 1


    def _get_direction_index(self):
        index = self.directions.index(self._heading)
        return index


    def rotate_right(self):
        index = self._get_direction_index() + 1
        if index == len(self.directions):
            index = 0

        self._heading = self.directions[index]


    def rotate_left(self):
        index = self._get_direction_index() - 1
        self._heading = self.directions[index]


    def move_forward(self):
        self._forwards_movements[self._heading]()


    def get_current_location(self):
        return {'x': self._x, 'y': self._y, 'heading': self._heading}
