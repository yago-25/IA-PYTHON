"""
Exemplo do algoritmo ganâncioso - Dijastra.
Solução do Caminho mais Curto.
"""


# 1. Definir: Representar o grafo (mapa) e a tabela de soluções.

DISTANCE = 0
PREDECESSOR = 1
INFINITY = float("inf")

map = {
    "A": {"B": 5, "D": 9, "E": 2},
    "B": {"A": 5, "C": 2},
    "C": {"B": 2, "D": 3},
    "D": {"A": 9, "C": 3, "F": 2},
    "E": {"A": 2, "F": 3},
    "F": {"D": 2, "E": 3}
}

table = {
    "A": [0, None],
    "B": [INFINITY, None],
    "C": [INFINITY, None],
    "D": [INFINITY, None],
    "E": [INFINITY, None],
    "F": [INFINITY, None]
}


#TODO: 2. Definir função que retorna a distância mais curta de um vétice a partir da origem.

def get_shortest_distance(table: dict, vertex: str)-> int:
    """
    Função que retorna a distância mais curta de um vétice a partir da origem.
    """
    return table[vertex][DISTANCE]


#TODO: 3. Definir função que atualiza a distância mais curta na tabela.

def set_shortest_distance(table: dict, vertex: str, distance: int):
    """
    Função que atualiza a distância mais curta na tabela.
    """
    table[vertex][DISTANCE] = distance


#TODO: 4. Definir função que atualiza o antecessor na tabela.

def set_predecessor(table: dict, vertex: str, predecessor: str):
    """
    Função que atualiza o antecessor do vértice na tabela.
    """
    table[vertex][PREDECESSOR] = predecessor


#TODO: 5. Definir função que retorna a distância entre 2 vértices.

def get_distance(map: dict, first_vertex: str, second_vertex: str):
    """
    Função que retorna a distância entre 2 vértices.
    """
    return map[first_vertex][second_vertex]


#TODO: 6. Definir função que retorna o próximo vértice a ser visitado.

def get_next_vertex(table: dict, visited: list):
    """
    Função que retorna o próximo vértice a ser visitado.
    """
    unvisited = list(
        set(
            table.keys()
        ).difference(visited)
    )

    min_vertex = unvisited[0]
    min_distance = table[unvisited[0]][DISTANCE]

    for vertex in unvisited:
        if table[vertex][DISTANCE] < min_distance:
            min_vertex = vertex
            min_distance = table[vertex][DISTANCE] 

    return min_vertex


#TODO: 7. Definir função principal que resolve o problema do caminho mais curto.

def find_shortes_path(map: dict, table: dict, origin: str = "A"):
    """
    Função principal que resolve o problema do caminho mais curto.
    """
    visited = []
    current = origin 
    start = origin

    while True: 
        adjacent_vertex = map[current]

        if set(adjacent_vertex).issubset(set(visited)):
            ...

        unvisted = set(adjacent_vertex).difference(set(visited))

        for vertex in unvisted:
            distance_from_start = get_shortest_distance(table, vertex)

            if distance_from_start == INFINITY and current == start:
                total_distance = get_distance(map, vertex, current)
            else:
                total_distance = get_shortest_distance(table, current)
                total_distance += get_distance(map, current, vertex)

            if total_distance < distance_from_start:
                set_shortest_distance(table, vertex, total_distance)
                set_predecessor(table, vertex, current)

        visited.append(current)

        if len(visited) == len(table.keys()):
            break 

        current = get_next_vertex(table, visited)

    return table

result = find_shortes_path(map, table)
print(result)
