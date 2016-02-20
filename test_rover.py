from app.rover import Rover


class TestRover:

    def test_rover_can_rotate_left(self):
        rover = Rover(5, 5, 'N')
        headings = ['N', 'W', 'S', 'E']
        result = False
        for i in headings:
            print i
            rover.rotate_left()
            if i == 'N':
                result = rover.is_heading_west() == True

            elif i == 'S':
                result = rover.is_heading_east() == True

            elif i == 'E':
                result = rover.is_heading_north() == True

            elif i == 'W':
                result = rover.is_heading_south() == True

            if not result:
                break

        assert result
