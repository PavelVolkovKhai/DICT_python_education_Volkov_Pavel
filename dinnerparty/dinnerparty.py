import random

number_of_friends = int(input("Enter the number of friends joining (including you):\n"))

if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}

    print("Enter the name of every friend (including you), each on a new line:")

    for _ in range(number_of_friends):
        name = input()
        friends[name] = 0

    print(friends)

    total_amount = float(input("Enter the total amount:\n"))

    share = round(total_amount / len(friends), 2)

    for name in friends:
        friends[name] = share

    print(friends)

    choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if choice == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")

        if len(friends) > 1:
            share = round(total_amount / (len(friends) - 1), 2)
        else:
            share = 0

        for name in friends:
            if name == lucky_one:
                friends[name] = 0
            else:
                friends[name] = share

    else:
        print("No one is going to be lucky")

    print(friends)