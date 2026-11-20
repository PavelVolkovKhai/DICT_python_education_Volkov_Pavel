class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

        self.state = "main"
        self.running = True

        self.drinks = {
            "1": ("espresso", 250, 0, 16, 4),
            "2": ("latte", 350, 75, 20, 7),
            "3": ("cappuccino", 200, 100, 12, 6)
        }

    def print_state(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee_beans} g of coffee beans")
        print(f"{self.disposable_cups} disposable cups")
        print(f"{self.money} UAH of money")

    def show_main_menu(self):
        self.state = "main"
        print("\nWrite action (buy, fill, take, remaining, exit): ")

    def show_buy_menu(self):
        self.state = "buy"
        print("\nWhat do you want to buy?")
        print("1 - espresso")
        print("2 - latte")
        print("3 - cappuccino")
        print("back - return to main menu")
        print("Enter your choice: ")

    def buy(self, choice):
        if choice == "back":
            self.show_main_menu()
            return

        if choice not in self.drinks:
            print("Invalid choice!")
            self.show_buy_menu()
            return

        drink, required_water, required_milk, required_beans, price = self.drinks[choice]

        if self.water < required_water:
            print("Sorry, not enough water!")
        elif self.milk < required_milk:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < required_beans:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            self.water -= required_water
            self.milk -= required_milk
            self.coffee_beans -= required_beans
            self.disposable_cups -= 1
            self.money += price

            print(f"\nI have enough resources, making you a {drink}!")

        self.show_main_menu()

    def start_filling(self):
        self.state = "fill_water"
        print("\nWrite how many ml of water you want to add:")

    def process_fill(self, user_input):
        try:
            amount = int(user_input)

            if amount < 0:
                print("Please enter a non-negative number.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return

        if self.state == "fill_water":
            self.water += amount
            self.state = "fill_milk"
            print("Write how many ml of milk you want to add:")

        elif self.state == "fill_milk":
            self.milk += amount
            self.state = "fill_beans"
            print("Write how many grams of coffee beans you want to add:")

        elif self.state == "fill_beans":
            self.coffee_beans += amount
            self.state = "fill_cups"
            print("Write how many disposable cups you want to add:")

        elif self.state == "fill_cups":
            self.disposable_cups += amount
            print("\nThe coffee machine has been refilled!")
            self.show_main_menu()

    def take(self):
        print(f"\nI gave you {self.money} UAH")
        self.money = 0
        self.show_main_menu()

    def process_input(self, user_input):
        if self.state == "main":
            if user_input == "buy":
                self.show_buy_menu()

            elif user_input == "fill":
                self.start_filling()

            elif user_input == "take":
                self.take()

            elif user_input == "remaining":
                self.print_state()
                self.show_main_menu()

            elif user_input == "exit":
                print("Goodbye!")
                self.running = False

            else:
                print("Unknown action!")
                self.show_main_menu()

        elif self.state == "buy":
            self.buy(user_input)

        elif self.state.startswith("fill_"):
            self.process_fill(user_input)


machine = CoffeeMachine()

machine.show_main_menu()

while machine.running:
    user_input = input()
    machine.process_input(user_input)
