from app.rover import Rover
from app.movement import Movement


class TestRover:

    # def test_rover_can_move_forward(self):
    #     rover = Rover(5, 5, 'N')
    #     rover.move_forward()
    #     current = rover.get_current_location()
    #     assert current['y'] == 6
    #
    #     rover.rotate_left()
    #     rover.move_forward()
    #     current = rover.get_current_location()
    #     assert current['y'] == 6
    #     assert current['x'] == 4
    #     assert current['heading'] == 'W'

    def test_rover_can_rotate_left(self):
        move = Movement(5, 5, 'N')
        rover = Rover(move)
        headings = ['N', 'W', 'S', 'E', 'N', 'W', 'S', 'E']

        for i in headings:
            rover.rotate_left()
            location = rover.get_current_location()
            if i == 'N':
                assert location['heading'] == 'W'

            elif i == 'S':
                assert location['heading'] == 'E'

            elif i == 'E':
                assert location['heading'] == 'N'

            elif i == 'W':
                assert location['heading'] == 'S'

    def test_rover_can_rotate_right(self):
        move = Movement(5, 5, 'N')
        rover = Rover(move)
        headings = ['N', 'E', 'S', 'W', 'N', 'E', 'S', 'W']
        for i in headings:
            rover.rotate_right()
            location = rover.get_current_location()

            if i == 'N':
                assert location['heading'] == 'E'

            elif i == 'S':
                assert location['heading'] == 'W'

            elif i == 'E':
                assert location['heading'] == 'S'

            elif i == 'W':
                assert location['heading'] == 'N'
