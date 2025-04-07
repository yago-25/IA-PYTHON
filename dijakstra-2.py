import heapq

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'D': 2, 'C': 5},
    'C': {'A': 3, 'B': 5, 'D': 1, 'E': 3},
    'D': {'B': 2, 'C': 1, 'E': 4},
    'E': {'C': 3, 'D': 4}
}

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    previous = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous

distances, previous = dijkstra(graph, 'A')

print("Menores distâncias a partir de A:")
for vertex in sorted(graph.keys()):
    print(f"A -> {vertex}: {distances[vertex]}")

def get_path(prev, target):
    path = []
    while target:
        path.append(target)
        target = prev[target]
    return list(reversed(path))

print("\nCaminho mais curto de A até E:")
print(" -> ".join(get_path(previous, 'E')))
