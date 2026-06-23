# # 1
# number = 9

# multiplayer = 1

# while multiplayer <= 10:
#     result = number * multiplayer
#     print( f"{number} * {multiplayer} = {result}")
#     multiplayer = multiplayer + 1

# 2

# numbers = [10, 20, 30, 40]


# total_sum = 0

# index = 0

# while index < len(numbers):
#     total_sum = total_sum + numbers[index]
    
#     index = index + 1

# print(f"Сума чисел у списку: {total_sum}")

# # 3

# number = 7

# factorial = 1

# current = 1

# while current <= number:
  
#     factorial = factorial * current
    
#     current = current + 1

# print(f"Факторіал числа {number} дорівнює {factorial}")

# 4
# number = 2

# while number <= 50:
#     if number % 2 == 0:
#         print(number)
    
#     number = number + 1

# 5 

number = 2

while number <= 20:
    
    divisors_count = 0
    
    test_divisor = 1
    
    while test_divisor <= number:
        if number % test_divisor == 0:
            divisors_count = divisors_count + 1
        
        
        test_divisor = test_divisor + 1
        
   
    if divisors_count == 2:
        print(number)
        
    number = number + 1



