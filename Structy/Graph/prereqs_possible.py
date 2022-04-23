"""
https://structy.net/problems/premium/prereqs-possible
"""


def prereqs_possible(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)
    visiting = set()
    visited = set()

    for node in graph:
        if has_cycle(graph, node, visiting, visited):
            return False

    return True


def has_cycle(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbour in graph[node]:
        if has_cycle(graph, neighbour, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)

    return False


def build_graph(num_courses, prereqs):
    graph = {}

    for course in range(0, num_courses):
        graph[course] = []

    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)

    return graph


if __name__ == '__main__':
    numCourses = 5
    prereqs = [
        (2, 4),
        (1, 0),
        (0, 2),
        (0, 4),
    ]
    print(prereqs_possible(numCourses, prereqs))  # -> True

    numCourses = 6
    prereqs = [
        (2, 4),
        (1, 0),
        (0, 2),
        (0, 4),
        (5, 3),
        (3, 5),
    ]
    print(prereqs_possible(numCourses, prereqs))  # -> False