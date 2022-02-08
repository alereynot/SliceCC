from unittest import TestCase


class TestApproach1(TestCase):
    def test_find_directions_correct_parameters(self):
        from py.approach_1.pizzabot import find_directions

        dimension = [5, 5]
        coordinates = [(1, 3), (4, 4)]

        result = find_directions(dimension, coordinates)
        expected = "ENNNDEEEND"
        self.assertEqual(result, expected)

        dimension = [9, 9]
        coordinates = [(1, 1), (9, 1), (9, 4), (4, 5), (4, 8), (1, 8), (1, 3)]

        result = find_directions(dimension, coordinates)
        expected = "ENDEEEEEEEEDNNNDWWWWWNDNNNDWWWDSSSSSD"
        self.assertEqual(result, expected)

    def test_find_directions_incorrect_parameters(self):
        from py.approach_1.pizzabot import find_directions
        from py.common import constants

        dimension = [5, 5]
        coordinates = [(1, 30), (40, 4)]
        result = find_directions(dimension, coordinates)
        expected = constants.ERR_COORD_NOT_IN_GRID
        self.assertEqual(result, expected)

        dimension = [5, 5]
        coordinates = [(1, 1), (-4, 4)]
        result = find_directions(dimension, coordinates)
        expected = constants.ERR_COORD_NOT_IN_GRID
        self.assertEqual(result, expected)

        dimension = [-5, 5]
        coordinates = [(1, 1), (4, 4)]
        result = find_directions(dimension, coordinates)
        expected = constants.ERR_COORD_NOT_IN_GRID
        self.assertEqual(result, expected)

    def test_moves(self):
        from py.approach_1.pizzabot import moves

        result = "EEEEEE"
        expected = moves("x", 1, 7)
        self.assertEqual(result, expected)
