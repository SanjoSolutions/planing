class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


class Node:
    def __init__(self):
        self.connections = set()


def connect(a: Node, b: Node):
    a.connections.add(b)
    b.connections.add(a)


def find_path_in_graph(graph, from_node, to_node):
    paths = [
        [from_node]
    ]
    path_to_node = find_path_to_node(to_node, paths)
    while path_to_node is None and len(paths) >= 1:
        paths = expand_paths(paths)
        path_to_node = find_path_to_node(to_node, paths)

    if path_to_node:
        if len(path_to_node) > 1:
            path_to_node = path_to_node[1:]

        path_to_node = tuple(path_to_node)

        return path_to_node
    else:
        return None


def find_path_to_node(node, paths):
    try:
        return next(path for path in paths if has_path_reached_node(node, path))
    except StopIteration:
        return None


def has_path_reached_node(node, path):
    return path[-1] == node


def expand_paths(paths):
    expanded_paths = []
    for path in paths:
        node = path[-1]
        for connected_node in node.connections:
            expanded_paths.append(path + [connected_node])
    return expanded_paths
