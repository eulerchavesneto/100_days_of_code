print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_people = int(input("How many people to split the bill? "))

bill_tipped = total_bill + (total_bill * tip_percent / 100)

result = bill_tipped / number_people

print(f"Each people should pay: ${result:.2f}")

