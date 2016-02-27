class Rover:
    def __init__(self, movement):
        self._movement = movement

    def rotate_left(self):
        self._movement.rotate_left()

    def rotate_right(self):
        self._movement.rotate_right()

    def move_forward(self):
        self._movement.move_forward()

    def get_current_location(self):
        return self._movement.get_current_location()
