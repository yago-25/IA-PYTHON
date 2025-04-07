graph = {
    'PU': {'PF': 46, 'C': 78, 'SM': 87},
    'PF': {'PU': 46, 'I': 75},
    'C': {'PU': 78, 'TB': 12, 'M': 66, 'SJP': 19, 'Araucaria': 37, 'BalsaNova': 51, 'CampoLargo': 29},
    'SM': {'PU': 87, 'I': 57, 'L': 60, 'Palmeira': 77},
    'I': {'PF': 75, 'SM': 57, 'Palmeira': 75},
    'Palmeira': {'SM': 77, 'I': 75, 'CampoLargo': 55},
    'M': {'C': 66, 'TB': 43},
    'TB': {'C': 12, 'M': 43},
    'L': {'SM': 60, 'M': 57, 'Contenda': 26},
    'Contenda': {'L': 26, 'BalsaNova': 19, 'Araucaria': 18},
    'BalsaNova': {'Contenda': 19, 'CampoLargo': 22, 'C': 51},
    'CampoLargo': {'BalsaNova': 22, 'Palmeira': 55, 'C': 29},
    'SJP': {'C': 19},
    'Araucaria': {'Contenda': 18, 'C': 37},
    'Tijucas': {'M': 99, 'SJP': 49},
}

heuristics = {
    'PU': 160,
    'PF': 140,
    'C': 0,
    'SM': 120,
    'I': 100,
    'Palmeira': 95,
    'M': 150,
    'TB': 130,
    'L': 110,
    'Contenda': 80,
    'BalsaNova': 70,
    'CampoLargo': 50,
    'SJP': 20,
    'Araucaria': 40,
    'Tijucas': 150,
}

import heapq

def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        for neighbor, distance in graph[current].items():
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristics[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    return None, float('inf')

start = 'PU'
goal = 'C'
path, distance = a_star(graph, heuristics, start, goal)

print(f"Menor caminho de {start} a {goal}: {path} com distância {distance} km")
