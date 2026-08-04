# # fruits = ["Apple", "Peach", "Pear"]

# # for fruit in fruits:
# #     print(fruit)
# #     print(fruit + " pie")

# # print(fruits)

# student_scores = [
#     150,
#     142,
#     185,
#     120,
#     171,
#     184,
#     149,
#     24,
#     59,
#     68,
#     199,
#     78,
#     65,
#     89,
#     31,
#     15,
#     39,
#     82,
#     150,
#     33,
#     35,
# ]

# print(max(student_scores))

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(max_score)


# Range Function with For Loop
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# FizzBuzz
for number in range(1, 101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        print(number)
    else:
        print(number)
