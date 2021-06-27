import unittest

from find_path import find_path


class TestFindPath(unittest.TestCase):
    def test_find_path(self):
        space = (
            (1, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 2)
        )

        from_position = (0, 0)
        to_position = (3, 2)
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

        from_position = (0, 0)
        to_position = (3, 2)
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

        from_position = (0, 0)
        to_position = (3, 3)
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

        from_position = (0, 1)
        to_position = (0, 0)
        path = find_path(space, from_position, to_position)

        self.assertEqual(
            (
                (0, 0),
            ),
            path
        )

    def test_find_path_going_left(self):
        space = (
            (1, 2),
        )

        from_position = (1, 0)
        to_position = (0, 0)
        path = find_path(space, from_position, to_position)

        self.assertEqual(
            (
                (0, 0),
            ),
            path
        )


if __name__ == '__main__':
    unittest.main()
