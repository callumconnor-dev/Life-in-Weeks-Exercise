age = input("What is your current age? ")

expirationDate = 90
timeRemaining = expirationDate - int(age)

daysRemaining = timeRemaining * 365
weeksRemaining = timeRemaining * 52
monthsRemaining = timeRemaining * 12

print(f"You have {daysRemaining} days, {weeksRemaining} weeks, and {monthsRemaining} months left.")

