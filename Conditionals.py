# 1
# password = "password123"

# admin = "password123"



# if admin == password:
#     print("Ви увійшли в систему")
# else:
#     print("Неправильний пароль")

#2
day_number = 1

days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]

if 1 <= day_number <= 7:
    print(days[day_number - 1])
else:
    print("Помилка: недійсний номер дня (має бути від 1 до 7)")
