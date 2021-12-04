# Задание 1
days_of_week = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"
}
choice = int(input("Enter the num of weekday: "))
print(days_of_week.get(choice))

# Задание 2
home_animals = {
    "four-legged" : "cat"
}

# Задание 3
string = str(input("Введите строку текста: "))
num_of_words_of_string = {}
for i in string:
    num_of_words_of_string[i] = num_of_words_of_string.get(i, 0) + 1
print(num_of_words_of_string)
