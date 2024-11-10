import random

def find_multiples(x, numbers):
  """
  Функция ищет все числа, кратные заданному числу X в списке.

  Args:
    x: Число, кратные которому нужно найти.
    numbers: Список чисел.

  Returns:
    Список чисел, кратных X.
  """
  multiples = list(filter(lambda num: num % x == 0, numbers))
  return multiples

# Генерация случайного списка чисел
numbers = [random.randint(0, 200) for _ in range(10)]

# Запрос числа X
while True:
  try:
    x = input("Введите число X: ")
    # Проверка на корректность ввода - только цифры
    if not x.isdigit():
      raise ValueError("Введите целое число.")
    x = int(x)
    # Проверка на корректность диапазона X
    if x > 200 or x < 0:
      raise ValueError("Число X должно быть в диапазоне от 0 до 200.")
    break  # Выход из цикла, если ввод корректный
  except ValueError as e:
    print(e)

# Поиск кратных чисел и вывод результата
multiples = find_multiples(x, numbers)
print(f"Числа, кратные {x}, в списке: {multiples}")






