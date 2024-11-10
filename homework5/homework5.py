def get_number():
  for i in range(30):
    if i % 2 != 0:
      yield i

# Инициализация генератора
numbers = get_number()

# Получение и вывод первого, пятого и последнего значений
print(f"Первое значение: {next(numbers)}")
for _ in range(4):
  next(numbers)
print(f"Пятое значение: {next(numbers)}")

# Получение и вывод последнего значения
last_value = None
try:
  while True:
    last_value = next(numbers)
except StopIteration:
  pass

print(f"Последнее значение: {last_value}") 


