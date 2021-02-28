import pyinputplus as pyip

try:
    print("What type of bread you want for your sandwich :")
    print("\n")
    sandwich = pyip.inputMenu(['Wheat', 'White', 'Sourdough'])

    print("What type of protein you want for your sandwich :")
    print("\n")
    protein = pyip.inputMenu(['Chicken', 'Turkey', 'Tufo', 'Ham'])

    print("Do  you want cheese ? ")
    print("\n")
    response = pyip.inputYesNo()

    print("What kind of cheese you want : ")
    print("\n")
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])

    print("Do you want mayo, mustard, lettuce, or tomato? ")
    print("\n")
    ans = pyip.inputYesNo()

    print("How many sandwich you want ? ")
    print("\n")
    NumberOfSand = pyip.inputInt(min=1)

except pyip.Exception:
    print("Opps ! there may be a problem")

finally:
    print("Thank you for your response :D")


