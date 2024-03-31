print("Welcome to the tip calculator.")
billAmount = float(input("What was the total bill?\n"))
percentage = float(input("What percentage tip would you like to give? \n 10%, 15%, 20%\n"))
contributors = float(input("How many people are contributing to the bill?\n"))
totalPrice = (billAmount * (percentage/100)) + billAmount
pricePerPerson = totalPrice / contributors
roundPerson = round(pricePerPerson,2)
print(f"Each person pays: ${roundPerson}")