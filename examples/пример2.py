# 2.2. Аргументы и параметры функции
print("Пример функции с одним аргументом: ")
def example(color):
    if color == "green":
        return "This is tree"
    elif color == "blue":
        return "This is sky"
    else:
        return "I don't know"
what_is_it = example('Black')
print(what_is_it)
print()


print("Пример позиционных аргументов: ")

def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}
my_cat = cat('Andrey', 'red', 20)
print(my_cat)
print()


print("Пример аргумент – ключевые слова: ")

def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}
my_cat = cat(color = 'Grey', age = 9, name = 'Alise')
print(my_cat)