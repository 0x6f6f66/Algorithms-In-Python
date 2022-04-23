"""
https://structy.net/problems/premium/can-color
"""


def can_color(graph):
    colors = {}
    for node in graph:
        if node not in colors and not valid(graph, node, colors, False):
            return False

    return True


def valid(graph, node, colors, current_color):
    if node in colors:
        return colors[node] == current_color

    colors[node] = current_color

    for neighbour in graph[node]:
        if valid(graph, neighbour, colors, not current_color) is False:
            return False

    return True


if __name__ == '__main__':
    print(can_color({
        "x": ["y"],
        "y": ["x", "z"],
        "z": ["y"]
    }))  # -> True

    """
    print(can_color({
        "q": ["r", "s"],
        "r": ["q", "s"],
        "s": ["r", "q"]
    }))  # -> False

    print(can_color({
        "a": ["b", "c", "d"],
        "b": ["a"],
        "c": ["a"],
        "d": ["a"],
    }))  # -> True

    print(can_color({
        "a": ["b", "c", "d"],
        "b": ["a"],
        "c": ["a", "d"],
        "d": ["a", "c"],
    }))  # -> False

    print(can_color({
        "h": ["i", "k"],
        "i": ["h", "j"],
        "j": ["i", "k"],
        "k": ["h", "j"],
    }))  # -> True

    print(can_color({
        "z": []
    }))  # -> True

    print(can_color({
        "h": ["i", "k"],
        "i": ["h", "j"],
        "j": ["i", "k"],
        "k": ["h", "j"],
        "q": ["r", "s"],
        "r": ["q", "s"],
        "s": ["r", "q"]
    }))  # -> False
    """
