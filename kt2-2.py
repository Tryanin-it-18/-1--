from collections import deque


def main():
    print("Введите количество вершин и стартовую вершину (через пробел):")
    first_line = input().split()
    n = int(first_line[0])  # количество вершин
    s = int(first_line[1])  # заданная вершина

    print(f"Введите матрицу смежности {n}x{n} (построчно, числа через пробел):")
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Поиск компоненты связности с помощью BFS
    visited = [False] * n  # массив посещенных вершин
    component = []  # список вершин в компоненте связности

    # BFS начинается с заданной вершины (переводим в 0-индексацию)
    start_vertex = s - 1
    queue = deque([start_vertex])
    visited[start_vertex] = True

    while queue:
        current = queue.popleft()
        component.append(current + 1)  # возвращаем к 1-индексации для вывода

        # Проверяем всех соседей текущей вершины
        for neighbor in range(n):
            # Если есть ребро и вершина еще не посещена
            if matrix[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    # Сортируем вершины для красивого вывода
    component.sort()

    # Вывод результата
    print("\nРезультат:")
    print(len(component))
    print(' '.join(map(str, component)))


# Запуск программы
if __name__ == "__main__":
    main()