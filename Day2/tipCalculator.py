print("Welcome to the tip calculator.")
bill = round(float(input("What was the total bill? $")),2)
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
party_size = int(input("How many people to split the bill? "))

tip_amount = bill * tip_percentage
total_bill = tip_amount + bill
total_per_person = round(total_bill / party_size, 2)
total_per_person = "{:.2f}".format(total_per_person)

print(f"Each person should pay: ${total_per_person}\n")
