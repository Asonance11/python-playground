score = int(input("Enter your score: "))
if score >= 85:
    print("You got an A!")
elif score >= 60:
    print("You got a B!")
elif score >= 50:
    print("You got a C!")
else:
    print("You got an F!")

temperature = float(input("Enter the temperature: "))
if temperature > 0 and temperature < 30:
    print("Weather is nice today!")
elif temperature < 0 or temperature > 30:
    print("Weather is not nice today!")