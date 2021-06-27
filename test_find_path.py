import unittest

from find_path import find_path


class TestFindPath(unittest.TestCase):
    def test_find_path(self):
        space = (
            (1, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 2)
        )

        from_position = determine_from_position(space)
        to_position = determine_to_position(space)
        path = find_path(space, from_position, to_position)

        self.assertEqual(
            (
                (1, 0),
                (2, 0),
                (3, 0),
                (3, 1),
                (3, 2)
            ),
            path
        )

    def test_find_path_with_obstacle(self):
        space = (
            (1, 0, 3, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 2)
        )

        from_position = determine_from_position(space)
        to_position = determine_to_position(space)
        path = find_path(space, from_position, to_position)

        self.assertEqual(
            (
                (1, 0),
                (1, 1),
                (2, 1),
                (3, 1),
                (3, 2)
            ),
            path
        )

    def test_find_path_with_obstacles(self):
        space = (
            (1, 0, 3, 0),
            (0, 0, 3, 0),
            (0, 3, 0, 0),
            (0, 0, 0, 2)
        )

        from_position = determine_from_position(space)
        to_position = determine_to_position(space)
        path = find_path(space, from_position, to_position)

        self.assertEqual(
            (
                (0, 1),
                (0, 2),
                (0, 3),
                (1, 3),
                (2, 3),
                (3, 3)
            ),
            path
        )

    def test_find_path_going_up(self):
        space = (
            (2,),
            (1,)
        )

        from_position = determine_from_position(space)
        to_position = determine_to_position(space)
        path = find_path(space, from_position, to_position)

        self.assertEqual(
            (
                (0, 0),
            ),
            path
        )

    def test_find_path_going_left(self):
        space = (
            (2, 1),
        )

        from_position = determine_from_position(space)
        to_position = determine_to_position(space)
        path = find_path(space, from_position, to_position)

        self.assertEqual(
            (
                (0, 0),
            ),
            path
        )

    def test_find_path_zero_paths(self):
        space = (
            (1, 3, 2),
        )

        from_position = determine_from_position(space)
        to_position = determine_to_position(space)
        path = find_path(space, from_position, to_position)

        self.assertEqual(
            None,
            path
        )


def determine_from_position(space):
    return find_value(space, 1)


def determine_to_position(space):
    return find_value(space, 2)


def find_value(space, value):
    for y in range(len(space)):
        for x in range(len(space[0])):
            if space[y][x] == value:
                return (x, y)
    return None


if __name__ == '__main__':
    unittest.main()
