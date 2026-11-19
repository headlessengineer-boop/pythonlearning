# age = int(input("Вік?"))

# if age < 18:
#     print("Ви неповнолітній")
# elif age > 200:
#     print("Ага, звичайно.")

# else:
#     print("Ви повнолітній")


# name = "Саша"
# age = 18
# driving_license = True


# if age > 17 and driving_license:
#     print('Ваше ім’я: ' + name + '. Ваш вік: ' + str(age) + '. Вам дозволено керувати автомобілем.')
# else:
#     print('Ваше ім’я: ' + name + '. Ваш вік: ' + str(age) + '. Вам не дозволено керувати автомобілем.')



name = input("Ім'я: ")
timeday = int(input("Хвилин у будній день: "))
freetimed = int(input("Хвилин у вихідний день: "))

weekday_time = timeday * 5
weekend_time = freetimed * 2
total_minutes = weekday_time + weekend_time
hours = total_minutes / 60


print("Ім'я: " + name + "грає:\n" + str(weekday_time) + " хвилин у будні\n" + str(weekend_time) + " хвилин у вихідні\n" + str(total_minutes) + " хвилин за тиждень\n" + "Це " + str(hours) + " години")
