from app.rover import Rover


class TestRover:

    def test_rover_can_move_forward(self):
        rover = Rover(5, 5, 'N')
        rover.move_forward()
        current = rover.get_current_location()
        assert current['y'] == 6

        rover.rotate_left()
        rover.move_forward()
        current = rover.get_current_location()
        assert current['y'] == 6
        assert current['x'] == 4
        assert current['heading'] == 'W'

    def test_rover_can_rotate_left(self):
        rover = Rover(5, 5, 'N')
        headings = ['N', 'W', 'S', 'E', 'N', 'W', 'S', 'E']

        for i in headings:
            rover.rotate_left()
            print rover._heading
            if i == 'N':
                assert rover.is_heading_west() == True

            elif i == 'S':
                assert rover.is_heading_east() == True

            elif i == 'E':
                assert rover.is_heading_north() == True

            elif i == 'W':
                assert rover.is_heading_south() == True

    def test_rover_can_rotate_right(self):
        rover = Rover(5, 5, 'N')
        headings = ['N', 'E', 'S', 'W', 'N', 'E', 'S', 'W']
        for i in headings:
            rover.rotate_right()
            if i == 'N':
                assert rover.is_heading_east() == True

            elif i == 'S':
                assert rover.is_heading_west() == True

            elif i == 'E':
                assert rover.is_heading_south() == True

            elif i == 'W':
                assert rover.is_heading_north() == True
