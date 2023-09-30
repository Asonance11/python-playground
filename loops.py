import time
# while loop

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

# for loops

for i in range(10):
    print(i)

for i in range(50, 100+1, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Its time to go")

# nested loops
rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input('Enter a symbol: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# control statements
while True:
    name = input('Enter your name: ')
    if name != "":
        break

phone_number = "123-456-789"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
print()
for i in range(20):
    if i == 15:
        pass
    else:
        print(i, end="")