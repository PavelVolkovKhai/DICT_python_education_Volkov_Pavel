bot_name = "DICT_Bot"
birth_year = 2026

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")
print("Please, remind me your name.")
your_name = input()

print(f"What a great name you have, {your_name}!")
print(f"Let me guess your age.")
print(f"Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {age}; that's a good time to start programming!")
print(f"Now I will prove to you that I can count to any number you want.")

number = int(input())
for i in range(number + 1):
    print(f"{i} !")

print(f"Let's test your programming knowledge.")
print(f"Why do we use methods?")
print(f"1. To repeat a statement multiple times.")
print(f"2. To decompose a program into several small subroutines.")
print(f"3. To determine the execution time of a program.")
print(f"4. To interrupt the execution of a program.")

answer = int(input())
while answer != 2:
    print("Please, try again.")
    answer = int(input())

print("Congratulations, have a nice day!")