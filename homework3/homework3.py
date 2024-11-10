from datetime import date, datetime

def calculate_age(birthdate_str):
  try:
    birthdate_parts = birthdate_str.split('/')
    # Проверка на наличие цифр в каждой части даты
    if not all(part.isdigit() for part in birthdate_parts):
      raise ValueError("Некорректный формат даты рождения. Введите дату в формате день/месяц/год.")
    
    # Проверка на корректность года (должно быть 4 цифры)
    year = int(birthdate_parts[2])
    if len(str(year)) != 4:
      raise ValueError("Год рождения должен состоять из четырех цифр.")

    # Проверка на корректность года (не может быть больше текущего года)
    if year > datetime.now().year:
      raise ValueError("Год рождения не может быть больше текущего года.")

    birthdate = date(year, int(birthdate_parts[1]), int(birthdate_parts[0]))
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
  except ValueError as e:
    print(e)
    return None

# Пример использования
birthdate = input("Введите дату рождения (день/месяц/год): ")
age = calculate_age(birthdate)
if age is not None:
  print(f"Ваш возраст: {age} лет")





