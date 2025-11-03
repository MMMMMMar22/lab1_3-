from lib import count_common_elements

def run_tests():
    print("=== ТЕСТИРОВАНИЕ МОДУЛЯ lib.py ===\n")
    # Тест 1: Обычные списки с общими элементами
    print("Тест 1: Обычные списки с общими элементами")
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]
    result1 = count_common_elements(list1, list2, list3)
    print(f"Списки: {list1}, {list2}, {list3}")
    print(f"Общих элементов: {result1} (ожидается: 1)\n")
    # Тест 2: Два одинаковых списка
    print("Тест 2: Два одинаковых списка")
    list4 = [1, 2, 3]
    list5 = [1, 2, 3]
    result2 = count_common_elements(list4, list5)
    print(f"Списки: {list4}, {list5}")
    print(f"Общих элементов: {result2} (ожидается: 3)\n")
    # Тест 3: Совершенно разные списки
    print("Тест 3: Совершенно разные списки")
    list6 = [1, 2, 3]
    list7 = [4, 5, 6]
    result3 = count_common_elements(list6, list7)
    print(f"Списки: {list6}, {list7}")
    print(f"Общих элементов: {result3} (ожидается: 0)\n")
    # Тест 4: Один список
    print("Тест 4: Передан один список")
    list8 = [10, 20, 30]
    result4 = count_common_elements(list8)
    print(f"Список: {list8}")
    print(f"Результат: {result4} (ожидается: 3)\n")
    # Тест 5: Пустые списки
    print("Тест 5: Пустые списки")
    result5 = count_common_elements([], [])
    print(f"Списки: [], []")
    print(f"Общих элементов: {result5} (ожидается: 0)\n")
    # Тест 6: Строки
    print("Тест 6: Списки со строками")
    list9 = ["apple", "banana", "orange"]
    list10 = ["banana", "orange", "grape"]
    list11 = ["orange", "kiwi", "pear"]
    result6 = count_common_elements(list9, list10, list11)
    print(f"Списки: {list9}, {list10}, {list11}")
    print(f"Общих элементов: {result6} (ожидается: 1)\n")
    # Тест 7: Разное количество списков
    print("Тест 7: Разное количество списков")
    list12 = [1, 2, 3, 4]
    list13 = [2, 3, 4, 5]
    list14 = [3, 4, 5, 6]
    list15 = [4, 5, 6, 7]
    result7 = count_common_elements(list12, list13, list14, list15)
    print(f"4 списка: {list12}, {list13}, {list14}, {list15}")
    print(f"Общих элементов: {result7} (ожидается: 1)\n")
    print("=== ТЕСТИРОВАНИЕ ЗАВЕРШЕНО ===")

run_tests()
print("\n=== ИНТЕРАКТИВНЫЙ ТЕСТ ===")
try:
    n = int(input("Введите количество списков для теста: "))
    lists = []
    for i in range(n):
        elements = input(f"Введите элементы списка {i + 1} через пробел: ").split()
        try:
            elements = [int(x) for x in elements]
        except ValueError:
            pass
        lists.append(elements)
    result = count_common_elements(*lists)
    print(f"Общих элементов во всех {n} списках: {result}")
except ValueError:
    print("Ошибка ввода. Завершение программы.")