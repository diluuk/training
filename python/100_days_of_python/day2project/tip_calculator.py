print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people will split the bill? "))

tip_percentage = tip_amount / 100

grand_total = bill + (bill * tip_percentage)
amount_paid_per_person = grand_total / split

print(f"{amount_paid_per_person:.2f}")
