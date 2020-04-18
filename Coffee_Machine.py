class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    state = "initial"

    def execute(self, user_input):
        if CoffeeMachine.state == "initial":
            if user_input == "buy":
                CoffeeMachine.state = "buying"
                print("What do you want to buy? 1 - espresso, 2 - latte macciato, 3 - cappucino, back - to main menu:")
            elif user_input == "remaining":
                self.print_summary()
                print("Write action (buy, fill, take, remaining, exit):")
            elif user_input == "fill":
                CoffeeMachine.state = "filling"
                print("Write how many ml of water do you want to add:")
            elif user_input == "take":
                self.take_money()
                print("Write action (buy, fill, take, remaining, exit):")

        elif CoffeeMachine.state == "buying":
            self.buy_coffee(user_input)

        elif CoffeeMachine.state == "filling":
            CoffeeMachine.water += int(user_input)
            CoffeeMachine.state = "filling milk"
            print("Write how many ml of milk do you want to add:")
        elif CoffeeMachine.state == "filling milk":
            CoffeeMachine.milk += int(user_input)
            CoffeeMachine.state = "filling coffee beans"
            print("Write how many grams of coffee beans do you want to add:")
        elif CoffeeMachine.state == "filling coffee beans":
            CoffeeMachine.beans += int(user_input)
            CoffeeMachine.state = "filling cups"
            print("Write how many disposable cups of coffee do you want to add:")
        elif CoffeeMachine.state == "filling cups":
            CoffeeMachine.cups += int(user_input)
            CoffeeMachine.state = "initial"
            print("Write action (buy, fill, take, remaining, exit):")

    def buy_coffee(self, user_input):
        if user_input == "1":
            self.performance_resources(250, 0, 16, 4)
            CoffeeMachine.state = "initial"
            print("Write action (buy, fill, take, remaining, exit):")
        elif user_input == "2":
            self.performance_resources(350, 75, 20, 7)
            CoffeeMachine.state = "initial"
            print("Write action (buy, fill, take, remaining, exit):")
        elif user_input == "3":
            self.performance_resources(200, 100, 12, 6)
            CoffeeMachine.state = "initial"
            print("Write action (buy, fill, take, remaining, exit):")
        elif user_input == "back":
            CoffeeMachine.state = "initial"
            print("Write action (buy, fill, take, remaining, exit):")

    def performance_resources(self, one_cup_water, one_cup_milk, one_cup_beans, cost):
        has_resources = self.has_missing_resources(one_cup_water, one_cup_milk, one_cup_beans, cost)
        if has_resources == "":
            print("I have enough resources, making you a coffee!")
            self.use_resources(one_cup_water, one_cup_milk, one_cup_beans, cost)
        else:
            print("Sorry, not enough", has_resources, "!")

    def has_missing_resources(self, one_cup_water, one_cup_milk, one_cup_beans, cost):
        if CoffeeMachine.water <= one_cup_water:
            return "water"
        if CoffeeMachine.milk <= one_cup_milk:
            return "milk"
        if CoffeeMachine.beans <= one_cup_beans:
            return "beans"
        if CoffeeMachine.money <= cost:
            return "money"
        if CoffeeMachine.cups <= 1:
            return "cups"
        else:
            return ""

    def use_resources(self, one_cup_water, one_cup_milk, one_cup_beans, cost):
        CoffeeMachine.water -= one_cup_water
        CoffeeMachine.milk -= one_cup_milk
        CoffeeMachine.beans -= one_cup_beans
        CoffeeMachine.cups -= 1
        CoffeeMachine.money += cost

    def print_summary(self):
        print("The coffee machine has:")
        print(CoffeeMachine.water, "of water")
        print(CoffeeMachine.milk, "of milk")
        print(CoffeeMachine.beans, "of coffee beans")
        print(CoffeeMachine.cups, "of disposable cups")
        print("$" + str(CoffeeMachine.money), "of money")

    def take_money(self):
        print("I gave you $" + str(CoffeeMachine.money))
        CoffeeMachine.money = 0


coffee_machine = CoffeeMachine()
print("Write action (buy, fill, take, remaining, exit):")

while True:
    user_input = input()
    if user_input == "exit":
        break
    else:
        coffee_machine.execute(user_input)
