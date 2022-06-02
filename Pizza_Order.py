# PIZZA ORDER
bill=0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
peperoni_small = 2
peperoni_medium = 3
peperoni_large = 3
cheese = 1


#Defining a function that take small sized pizza
def small_size():
    if size == "s" and add_pepperoni== "y" and extra_cheese=="y":
        bill = small_pizza + peperoni_small + cheese
        print(f"Your final total bill is ${bill}")
    elif size == "s" and add_pepperoni == "y" and extra_cheese == "n":
        bill = small_pizza + peperoni_small
        print(f"Your final total bill is ${bill}")
    elif size == "s" and add_pepperoni == "n" and extra_cheese == "y":
        bill = small_pizza + cheese
        print(f"Your final total bill is ${bill}")
    elif size == "s" and add_pepperoni == "n" and extra_cheese == "n":
        print(f"Your final total bill is ${small_pizza}")


#Defining a function that take medium sized pizza
def medium_size():
    if size == "m" and add_pepperoni == "y" and extra_cheese == "y":
        bill = medium_pizza + peperoni_medium + cheese
        print(f"Your final total bill is ${bill}")
    elif size == "m" and add_pepperoni == "y" and extra_cheese == "n":
        bill = medium_pizza + peperoni_medium
        print(f"Your final total bill is ${bill}")
    elif size == "m" and add_pepperoni == "n" and extra_cheese == "y":
        bill = medium_pizza + cheese
        print(f"Your final total bill is ${bill}")
    elif size == "m" and add_pepperoni == "n" and extra_cheese == "n":
        print(f"Your final total bill is ${medium_pizza}")


#Defining a function that take large sized pizza
def large_size():
    if size == "l" and add_pepperoni == "y" and extra_cheese == "y":
        bill = large_pizza + peperoni_large + cheese
        print(f"Your final total bill is ${bill}")
    elif size == "l" and add_pepperoni == "y" and extra_cheese == "n":
        bill = large_pizza + peperoni_large
        print(f"Your final total bill is ${bill}")
    elif size == "l" and add_pepperoni == "n" and extra_cheese == "y":
        bill = large_pizza + cheese
        print(f"Your final total bill is ${bill}")
    elif size == "l" and add_pepperoni == "n" and extra_cheese == "n":
        print(f"Your final total bill is ${large_pizza}")


def Pizza_order():
    small_size()
    medium_size()
    large_size()


print("WELCOME TO OZ PIZZA DELIVERIES!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()


Pizza_order()

