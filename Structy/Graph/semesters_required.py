"""
https://structy.net/problems/premium/semesters-required
"""


def semesters_required(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)

    distance = {}

    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 1

    for node in graph:
        traverse_count(graph, node, distance)

    return max(distance.values())


def traverse_count(graph, node, distance):
    if node in distance:
        return distance[node]

    max_semesters = 0
    for neighbour in graph[node]:
        attempt = traverse_count(graph, neighbour, distance)
        if attempt > max_semesters:
            max_semesters = attempt

    distance[node] = 1 + max_semesters
    return distance[node]


def build_graph(num_courses, prereqs):
    graph = {}
    for course in range(0, num_courses):
        graph[course] = []

    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)

    return graph


if __name__ == '__main__':
    num_courses = 6
    prereqs = [
        (1, 2),
        (2, 4),
        (3, 5),
        (0, 5),
    ]
    print(semesters_required(num_courses, prereqs))  # -> 3

    num_courses = 7
    prereqs = [
        (4, 3),
        (3, 2),
        (2, 1),
        (1, 0),
        (5, 2),
        (5, 6),
    ]
    print(semesters_required(num_courses, prereqs))  # -> 5