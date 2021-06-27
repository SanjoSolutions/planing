def find_path(space, from_position, to_position):
    paths = [
        [from_position]
    ]
    paths = filter_goable_paths(space, paths)
    path_to_position = find_path_to_positions(to_position, paths)
    while path_to_position is None and len(paths) >= 1:
        paths = expand_paths(space, paths)
        paths = filter_goable_paths(space, paths)
        path_to_position = find_path_to_positions(to_position, paths)

    if path_to_position:
        if len(path_to_position) > 1:
            path_to_position = path_to_position[1:]

        path_to_position = tuple(path_to_position)

        return path_to_position
    else:
        return None


def find_path_to_positions(position, paths):
    try:
        return next(path for path in paths if has_path_reached_position(position, path))
    except StopIteration:
        return None


def has_path_reached_position(position, path):
    return path[-1] == position


def expand_paths(space, paths):
    expanded_paths = []
    for path in paths:
        x, y = path[-1]
        if x + 1 < len(space[0]):
            expanded_paths.append(path + [(x + 1, y)])
        if y + 1 < len(space):
            expanded_paths.append(path + [(x, y + 1)])
    return expanded_paths


def filter_goable_paths(space, paths):
    return [path for path in paths if is_goable(space, path)]


def is_goable(space, path):
    x, y = path[-1]
    value = space[y][x]
    return value == 0 or value == 1 or value == 2
