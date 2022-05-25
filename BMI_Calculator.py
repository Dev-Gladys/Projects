#
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


def bmi_calculator(height, weight):
  return round(weight / (height * height), 2)


bmi = bmi_calculator(height, weight)


if bmi <= 18.5:
    print(f"Your bmi is: {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your bmi is: {bmi}, you are normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your bmi is: {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your bmi is: {bmi}, you are obese.")
else:
    print(f"Your bmi is: {bmi}, you are clinically obese.")