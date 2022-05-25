print("Welcome to the Tip Calculator!")
try:
    print("Welcome to the Tip Calculator!")
    bill = float(input("What was the total bill? $"))
    tip_amount = int(input("!How much tip would you want to give $: 5, 7, 10, 12? $"))
    num_of_persons = int(input("Number of persons that would split the bill? "))


    def calculate_tip(bill, tip_amount, num_of_persons):
        return round((bill / num_of_persons) * ((100 + tip_amount) / 100), 2)


    result = calculate_tip(bill, tip_amount, num_of_persons)

    print(f"Each person will pay ${result}")

except ValueError:
    print("Please enter a valid number.")
