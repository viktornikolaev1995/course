"""Домашнее задание для курса "Основы Python". Переменные, условия и циклы

# координаты точек
(0, 2)  Почтовое отделение – (0, 2)
(2, 5)  Ул. Грибоедова, 104/25 – (2, 5)
(5, 2)  Ул. Бейкер стрит, 221б – (5, 2)
(6, 6)  Ул. Большая Садовая, 302-бис – (6, 6)
(8, 3)  Вечнозелёная Аллея, 742 – (8, 3)
"""
import re



def calc_dist_between_two_points(point_1, point_2):
    """Вычисление расстояния между двумя точками на плоскости"""
    pattern = re.compile(r'(\d+, \d+)')
    match_1 = re.findall(pattern, point_1)
    match_2 = re.findall(pattern, point_2)
    point_1_0, point_1_1 = map(lambda n: int(n), match_1[0].split(', '))
    point_2_0, point_2_1 = map(lambda n: int(n), match_2[0].split(', '))
    result = ((point_2_0 - point_1_0) ** 2 + (point_2_1 - point_1_1) ** 2) ** 0.5
    return result


def finding_shortest_route(start_vertex: str, coord_points: str):

    coord = {coord_point for coord_point in coord_points.split('-')}
    graph = {}

    for i in coord:
        graph[i] = {coord_point: calc_dist_between_two_points(coord_point, i) for coord_point in coord if coord_point != i}
    visited = set()
    unvisited = {coord for coord, nearest_neighbors in graph.items()}
    end_vertex = start_vertex
    result = start_vertex
    vertex = None
    sum_length = 0

    while True:
        if vertex is None:
            vertex = start_vertex
        min_length = None
        visited.add(vertex)
        unvisited.remove(vertex)

        for nearest_neighbor, length in graph[vertex].items():
            if len(unvisited) == 0 and nearest_neighbor == end_vertex:
                min_length = length
                vertex = nearest_neighbor
                continue
            if nearest_neighbor in visited:
                continue
            if min_length is None:
                min_length = length
                vertex = nearest_neighbor
            if length > min_length:
                continue
            if length < min_length:
                min_length = length
                vertex = nearest_neighbor
        sum_length += min_length
        result += ' - > ' + vertex + str([sum_length])

        if len(unvisited) == 0:
            result += ' = ' + str(sum_length)
            break
    return result


if __name__ == "__main__":
    print(finding_shortest_route('(0, 2)', '(0, 2)-(2, 5)-(5, 2)-(6, 6)-(8, 3)'))
