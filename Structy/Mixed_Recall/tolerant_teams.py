"""
https://structy.net/problems/premium/tolerant-teams
"""


def tolerant_teams(rivalries):
    graph = assemble_graph(rivalries)
    teams = {}

    for person in graph:
        if person not in teams:
            if not valid_team(graph, person, teams, False):
                return False

    return True


def valid_team(graph, person, teams, team_color):
    if person in teams:
        return teams[person] == team_color

    teams[person] = team_color

    for neighbour in graph[person]:
        if not valid_team(graph, neighbour, teams, not team_color):
            return False

    return True


def assemble_graph(rivalries):
    graph = {}

    for rivalry in rivalries:
        a, b = rivalry

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph


if __name__ == '__main__':
    print(tolerant_teams([
        ('philip', 'seb'),
        ('raj', 'nader')
    ]))  # -> True

    print(tolerant_teams([
        ('philip', 'seb'),
        ('raj', 'nader'),
        ('raj', 'philip'),
        ('seb', 'raj')
    ]))  # -> False