# Odd and Even Number Checker
user ="yes"
try:
    while user =="yes":
        number = int(input("Which number do you want to check? "))

        def check_number(number):
            if number % 2 == 0:
                print(f"{number} is an even number")
            else:
                print(f"{number} is an odd number")
        check_number(number)

        user = input("Do you want to check another number? Yes or No: ").lower()
    else:
        quit()

except ValueError:
    print("Enter a valid number.")