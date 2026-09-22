"""Лабораторная работа № 2. Вариант 6.

Задания:
1. Калькулятор.
2. Перевернуть строку.
3. Сумма всех нечётных чисел до N.
4. Построить график y = x^2 с matplotlib.
5. Сериализация данных в JSON.
"""

import json
from pathlib import Path


def calculator() -> None:
    """Выполняет арифметическую операцию над двумя числами."""
    first = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /): ").strip()
    second = float(input("Введите второе число: "))

    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        if second == 0:
            print("Ошибка: деление на ноль невозможно.")
            return
        result = first / second
    else:
        print("Ошибка: неизвестная операция.")
        return

    print(f"Результат: {result:g}")


def reverse_string() -> None:
    """Выводит строку в обратном порядке."""
    source = input("Введите строку: ")
    print(f"Перевёрнутая строка: {source[::-1]}")


def sum_odd_numbers() -> None:
    """Находит сумму нечётных чисел от 1 до N включительно."""
    number = int(input("Введите N: "))
    if number < 1:
        print("Сумма: 0")
        return

    result = sum(value for value in range(1, number + 1) if value % 2 != 0)
    print(f"Сумма нечётных чисел от 1 до {number}: {result}")


def plot_parabola() -> None:
    """Строит и сохраняет график функции y = x^2."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Для задания 4 установите библиотеку matplotlib: python -m pip install matplotlib")
        return

    x_values = list(range(-10, 11))
    y_values = [x_value**2 for x_value in x_values]

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, color="blue", label="y = x^2")
    plt.title("График функции y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    output_path = Path("parabola.png")
    plt.savefig(output_path, dpi=150)
    print(f"График сохранён в файл: {output_path.resolve()}")
    plt.show()


def json_serialization() -> None:
    """Сохраняет данные в JSON и загружает их обратно."""
    student = {
        "name": "Студент",
        "group": "ИВТ-1",
        "variant": 6,
        "subjects": ["Python", "Математика", "Информатика"],
    }
    output_path = Path("student_data.json")
    output_path.write_text(
        json.dumps(student, ensure_ascii=False, indent=4), encoding="utf-8"
    )
    loaded_student = json.loads(output_path.read_text(encoding="utf-8"))
    print(f"Данные сохранены в {output_path.resolve()}")
    print("Данные после загрузки:")
    print(json.dumps(loaded_student, ensure_ascii=False, indent=4))


def main() -> None:
    """Выводит меню и запускает выбранное задание."""
    actions = {
        "1": calculator,
        "2": reverse_string,
        "3": sum_odd_numbers,
        "4": plot_parabola,
        "5": json_serialization,
    }

    while True:
        print(
            "\nЛабораторная работа № 2, вариант 6\n"
            "1 — Калькулятор\n"
            "2 — Перевернуть строку\n"
            "3 — Сумма нечётных чисел до N\n"
            "4 — График y = x^2\n"
            "5 — Сериализация в JSON\n"
            "0 — Выход"
        )
        choice = input("Выберите задание: ").strip()
        if choice == "0":
            print("Работа завершена.")
            break
        action = actions.get(choice)
        if action is None:
            print("Ошибка: выберите пункт от 0 до 5.")
            continue
        try:
            action()
        except ValueError:
            print("Ошибка: введено некорректное число.")


if __name__ == "__main__":
    main()

