import heapq

class Vertex:
    def __init__(self, label: str, target_distance: int):
        self.label = label
        self.target_distance = target_distance
        self.adjacent = []
        self.visited = False
    
    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)
    
    def show_adjacent(self):
        for adjacent in self.adjacent:
            print(f"Adjacente: {adjacent.vertex.label} - {adjacent.cost} km")


class Ajacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost


class Romania:
    def __init__(self):
        self.arad = Vertex("Arad", 366)
        self.zerind = Vertex("Zerind", 374)
        self.oradea = Vertex("Oradea", 380)
        self.sibiu = Vertex("Sibiu", 253)
        self.timisoara = Vertex("Timisoara", 329)
        self.lugoj = Vertex("Lugoj", 244)
        self.mehadia = Vertex("Mehadia", 241)
        self.dobreta = Vertex("Dobreta", 242)
        self.craiova = Vertex("Craiova", 160)
        self.rimnicu = Vertex("Rimnicu Vilcea", 193)
        self.fagaras = Vertex("Fagaras", 178)
        self.pitesti = Vertex("Pitesti", 98)
        self.giurgiu = Vertex("Giurgiu", 77)
        self.bucarest = Vertex("Bucarest", 0)

        self.arad.add_adjacent(Ajacent(self.zerind, 75))
        self.arad.add_adjacent(Ajacent(self.timisoara, 118))
        self.arad.add_adjacent(Ajacent(self.sibiu, 140))

        self.zerind.add_adjacent(Ajacent(self.oradea, 71))
        self.zerind.add_adjacent(Ajacent(self.arad, 75))

        self.oradea.add_adjacent(Ajacent(self.zerind, 71))
        self.oradea.add_adjacent(Ajacent(self.sibiu, 151))

        self.sibiu.add_adjacent(Ajacent(self.rimnicu, 80))
        self.sibiu.add_adjacent(Ajacent(self.fagaras, 99))
        self.sibiu.add_adjacent(Ajacent(self.arad, 140))
        self.sibiu.add_adjacent(Ajacent(self.oradea, 151))

        self.timisoara.add_adjacent(Ajacent(self.lugoj, 111))
        self.timisoara.add_adjacent(Ajacent(self.arad, 118))

        self.lugoj.add_adjacent(Ajacent(self.mehadia, 70))
        self.lugoj.add_adjacent(Ajacent(self.timisoara, 111))

        self.mehadia.add_adjacent(Ajacent(self.lugoj, 70))
        self.mehadia.add_adjacent(Ajacent(self.dobreta, 75))

        self.dobreta.add_adjacent(Ajacent(self.mehadia, 75))
        self.dobreta.add_adjacent(Ajacent(self.craiova, 120))

        self.craiova.add_adjacent(Ajacent(self.dobreta, 120))
        self.craiova.add_adjacent(Ajacent(self.pitesti, 138))
        self.craiova.add_adjacent(Ajacent(self.rimnicu, 146))

        self.rimnicu.add_adjacent(Ajacent(self.craiova, 146))
        self.rimnicu.add_adjacent(Ajacent(self.sibiu, 80))
        self.rimnicu.add_adjacent(Ajacent(self.pitesti, 97))

        self.fagaras.add_adjacent(Ajacent(self.sibiu, 99))
        self.fagaras.add_adjacent(Ajacent(self.bucarest, 211))

        self.pitesti.add_adjacent(Ajacent(self.craiova, 138))
        self.pitesti.add_adjacent(Ajacent(self.rimnicu, 97))
        self.pitesti.add_adjacent(Ajacent(self.bucarest, 101))

        self.bucarest.add_adjacent(Ajacent(self.pitesti, 101))
        self.bucarest.add_adjacent(Ajacent(self.giurgiu, 90))
        self.bucarest.add_adjacent(Ajacent(self.fagaras, 211))

        self.vertices = {
            "Arad": self.arad,
            "Zerind": self.zerind,
            "Oradea": self.oradea,
            "Sibiu": self.sibiu,
            "Timisoara": self.timisoara,
            "Lugoj": self.lugoj,
            "Mehadia": self.mehadia,
            "Dobreta": self.dobreta,
            "Craiova": self.craiova,
            "Rimnicu Vilcea": self.rimnicu,
            "Fagaras": self.fagaras,
            "Pitesti": self.pitesti,
            "Giurgiu": self.giurgiu,
            "Bucarest": self.bucarest,
        }

    def dijkstra(self, start, goal):
        queue = [(0, start)]
        distances = {vertex: float('inf') for vertex in self.get_all_vertices()}
        distances[start] = 0
        previous_vertices = {vertex: None for vertex in self.get_all_vertices()}

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_vertex == goal:
                break

            for adjacent in self.vertices[current_vertex].adjacent:
                neighbor = adjacent.vertex.label
                weight = adjacent.cost
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))

        path = []
        current_vertex = goal
        while previous_vertices[current_vertex] is not None:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.append(start)
        path.reverse()

        return path, distances[goal]

    def get_all_vertices(self):
        return {
            "Arad": self.arad,
            "Zerind": self.zerind,
            "Oradea": self.oradea,
            "Sibiu": self.sibiu,
            "Timisoara": self.timisoara,
            "Lugoj": self.lugoj,
            "Mehadia": self.mehadia,
            "Dobreta": self.dobreta,
            "Craiova": self.craiova,
            "Rimnicu Vilcea": self.rimnicu,
            "Fagaras": self.fagaras,
            "Pitesti": self.pitesti,
            "Giurgiu": self.giurgiu,
            "Bucarest": self.bucarest,
        }

romania = Romania()
path, distance = romania.dijkstra("Arad", "Bucarest")
print(f"Caminho mais curto de Arad a Bucarest: {path}")
print(f"Distância: {distance} km")
