# python compount interest calculator
# we are not allowed to enter 0
principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
        print("principle can't be less than or equal to 0")

while rate  <=0:
    rate = float(input("Enter the interest rate: "))
    if rate <=0:
        print("rate can't be less than or equal to 0")


while time <=0:
    time = int(input("Enter the time in years: "))
    if time <=0:
        print("time can't be less than or equal to 0")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total: .2f}")


# we are allowed to enter 0
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
        print("principle can't be less than or equal to 0")
    # if we don't use else this loop will never stop
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <=0:
        print("rate can't be less than or equal to 0")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <=0:
        print("time can't be less than or equal to 0")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total: .2f}")


# is ma condition while ki false h to while kabhi execute hi nhi ho ga direct last wla print ho ga
principle = 0
rate = 0
time = 0

while principle < 0:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
        print("principle can't be less than or equal to 0")

while rate  < 0:
    rate = float(input("Enter the interest rate: "))
    if rate <=0:
        print("rate can't be less than or equal to 0")


while time < 0:
    time = int(input("Enter the time in years: "))
    if time <=0:
        print("time can't be less than or equal to 0")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total: .2f}")