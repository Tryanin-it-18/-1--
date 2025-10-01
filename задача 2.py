import pickle
from collections import deque


class QueueIterator:
    """Класс-итератор для просмотра очереди в прямом и обратном порядке"""

    def __init__(self, queue):
        """
        Конструктор итератора
        queue - очередь для итерации
        """
        self.queue = list(queue)  # Сохраняем КОПИЮ очереди как список
        self.index = 0  # Текущий индекс
        self.direction = 'forward'  # Направление обхода

    def __iter__(self):
        """Возвращает сам объект как итератор"""
        return self

    def __next__(self):
        """Возвращает следующий элемент в зависимости от направления"""
        if self.direction == 'forward':
            # Прямой обход (от начала к концу)
            if self.index < len(self.queue):
                element = self.queue[self.index]
                self.index += 1
                return element
            else:
                raise StopIteration
        else:
            # Обратный обход (от конца к началу)
            if self.index >= 0:
                element = self.queue[self.index]
                self.index -= 1
                return element
            else:
                raise StopIteration

    def set_direction(self, direction):
        """Устанавливает направление обхода и сбрасывает индекс"""
        if direction not in ['forward', 'backward']:
            raise ValueError("Направление должно быть 'forward' или 'backward'")

        self.direction = direction
        if direction == 'forward':
            self.index = 0  # Начинаем с начала
        else:
            self.index = len(self.queue) - 1  # Начинаем с конца


def process_queue():
    """Основная функция для обработки очереди"""

    # Создаем очередь и заполняем ее данными
    queue = deque()

    print("=== Заполнение очереди ===")
    try:
        n = int(input("Введите количество элементов в очереди: "))
        if n <= 0:
            raise ValueError("Количество элементов должно быть положительным числом")

        for i in range(n):
            element = float(input(f"Введите элемент {i + 1}: "))
            queue.append(element)

        print(f"Очередь создана: {list(queue)}")

    except ValueError as e:
        print(f"✗ Ошибка при создании очереди: {e}")
        return

    # Обрабатываем очередь
    try:
        print("\n=== Обработка очереди ===")
        K = int(input("Введите число K (сколько элементов удалить): "))

        # Проверка корректности K
        if K <= 0:
            raise ValueError("K должно быть положительным числом")
        if K > len(queue):
            raise ValueError(f"K не может быть больше размера очереди ({len(queue)})")

        # Сохраняем исходную очередь для демонстрации итератора
        original_queue = deque(queue)  # Копируем исходную очередь

        # Удаляем первые K элементов
        removed_elements = []
        sum_removed = 0

        for i in range(K):
            if queue:  # Проверяем, что очередь не пустая
                element = queue.popleft()  # Удаляем элемент из начала
                removed_elements.append(element)
                sum_removed += element

        # Находим новый первый элемент
        if queue:  # Если очередь не пустая после удаления
            first_element = queue[0]  # Первый элемент
            first_pointer = id(queue[0])  # Указатель на первый элемент
        else:
            first_element = None
            first_pointer = None

        # Выводим результаты
        print(f"\n=== Результаты ===")
        print(f"Удаленные элементы: {removed_elements}")
        print(f"Сумма удаленных элементов: {sum_removed}")

        if first_element is not None:
            print(f"Новый первый элемент: {first_element}")
            print(f"Указатель на новый первый элемент: {first_pointer}")
        else:
            print("Очередь пуста после удаления")

        print(f"Оставшаяся очередь: {list(queue)}")

        # Сохраняем данные в двоичный файл
        data_to_save = {
            'removed_elements': removed_elements,
            'sum_removed': sum_removed,
            'first_element': first_element,
            'first_pointer': first_pointer,
            'remaining_queue': list(queue),
            'original_queue': list(original_queue)  # Сохраняем исходную очередь для справки
        }

        with open('rez.dat', 'wb') as file:
            pickle.dump(data_to_save, file)

        print("✓ Данные сохранены в файл rez.dat")

        # Демонстрация работы итератора на ИСХОДНОЙ очереди
        print(f"\n=== Работа итератора на исходной очереди ===")
        print(f"Исходная очередь: {list(original_queue)}")

        # Создаем итератор для исходной очереди
        iterator = QueueIterator(original_queue)

        print("Прямой обход очереди:")
        iterator.set_direction('forward')
        for element in iterator:
            print(f"  {element}")

        print("Обратный обход очереди:")
        iterator.set_direction('backward')
        for element in iterator:
            print(f"  {element}")

    except ValueError as e:
        print(f"✗ Ошибка при обработке очереди: {e}")


def load_and_display_data():
    """Функция для загрузки и отображения сохраненных данных"""
    try:
        with open('rez.dat', 'rb') as file:
            loaded_data = pickle.load(file)

        print(f"\n=== Загруженные данные из rez.dat ===")
        print(f"Удаленные элементы: {loaded_data['removed_elements']}")
        print(f"Сумма удаленных: {loaded_data['sum_removed']}")
        print(f"Первый элемент: {loaded_data['first_element']}")
        print(f"Указатель: {loaded_data['first_pointer']}")
        print(f"Оставшаяся очередь: {loaded_data['remaining_queue']}")
        print(f"Исходная очередь: {loaded_data['original_queue']}")

    except FileNotFoundError:
        print("✗ Файл rez.dat не найден")
    except Exception as e:
        print(f"✗ Ошибка при загрузке данных: {e}")


# Запуск программы
if __name__ == "__main__":
    process_queue()

    # Предлагаем посмотреть сохраненные данные
    view_data = input("\nХотите посмотреть сохраненные данные? (y/n): ")
    if view_data.lower() == 'y':
        load_and_display_data()

# ТЕСТЫ 

"""
=== Тестирование обработки очереди ===

Тест 1: Нормальная работа
Очередь: [1, 2, 3, 4, 5], K = 3
Ожидается:
  Удаленные: [1, 2, 3]
  Сумма: 6
  Новый первый: 4
  Оставшаяся: [4, 5]
  Прямой обход исходной: 1, 2, 3, 4, 5
  Обратный обход исходной: 5, 4, 3, 2, 1

Тест 2: Удаление всех элементов
Очередь: [10, 20], K = 2
Ожидается:
  Удаленные: [10, 20]
  Сумма: 30
  Новый первый: None
  Оставшаяся: []
  Прямой обход исходной: 10, 20
  Обратный обход исходной: 20, 10

Тест 3: K больше размера очереди
Очередь: [1, 2], K = 5
Ожидается: ValueError "K не может быть больше размера очереди"

Тест 4: K отрицательное
Очередь: [1, 2, 3], K = -1
Ожидается: ValueError "K должно быть положительным числом"

Тест 5: Пустая очередь
Очередь: [], K = 1
Ожидается: ValueError "K не может быть больше размера очереди"

=== Тестирование итератора ===

Тест 6: Прямой обход
Очередь: [1, 2, 3]
Ожидается: 1, 2, 3

Тест 7: Обратный обход  
Очередь: [1, 2, 3]
Ожидается: 3, 2, 1

Тест 8: Пустая очередь
Очередь: []
Ожидается: нет вывода

Тест 9: Один элемент
Очередь: [42]
Ожидается: 
  Прямой: 42
  Обратный: 42
"""