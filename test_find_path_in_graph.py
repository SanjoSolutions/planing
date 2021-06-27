import unittest

from find_path_in_graph import Node, connect, Graph, find_path_in_graph


class TestFindPathInGraph(unittest.TestCase):
    def test_find_path_in_graph(self):
        nodes = [
            Node(),
            Node(),
            Node()
        ]
        connect(nodes[0], nodes[1])
        connect(nodes[1], nodes[2])
        graph = Graph(nodes)
        path = find_path_in_graph(graph, nodes[0], nodes[2])
        self.assertEqual(
            (
                nodes[1],
                nodes[2]
            ),
            path
        )

    def test_find_path_in_graph_2(self):
        nodes = [
            Node(),
            Node(),
            Node(),
            Node()
        ]
        connect(nodes[0], nodes[1])
        connect(nodes[0], nodes[2])
        connect(nodes[2], nodes[3])
        graph = Graph(nodes)
        path = find_path_in_graph(graph, nodes[0], nodes[3])
        self.assertEqual(
            (
                nodes[2],
                nodes[3]
            ),
            path
        )


if __name__ == '__main__':
    unittest.main()
