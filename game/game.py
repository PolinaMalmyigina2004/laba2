import random

def get_user_choice():
  """Получает выбор пользователя."""
  while True:
    user_choice = input("Выберите камень, ножницы или бумагу: ").lower()
    if user_choice in ["камень", "ножницы", "бумага"]:
      return user_choice
    else:
      print("Неверный выбор. Попробуйте снова.")

def get_computer_choice():
  """Генерирует случайный выбор компьютера."""
  choices = ["камень", "ножницы", "бумага"]
  return random.choice(choices)

def determine_winner(user_choice, computer_choice):
  """Определяет победителя."""
  print(f"Вы выбрали: {user_choice}")
  print(f"Компьютер выбрал: {computer_choice}")

  if user_choice == computer_choice:
    return "Ничья!"
  elif (
      (user_choice == "камень" and computer_choice == "ножницы") or
      (user_choice == "ножницы" and computer_choice == "бумага") or
      (user_choice == "бумага" and computer_choice == "камень")
  ):
    return "Вы победили!"
  else:
    return "Компьютер победил!"

def play_game():
  """Запускает игру."""
  user_choice = get_user_choice()
  computer_choice = get_computer_choice()
  winner = determine_winner(user_choice, computer_choice)
  print(winner)

if __name__ == "__main__":
  play_game()
