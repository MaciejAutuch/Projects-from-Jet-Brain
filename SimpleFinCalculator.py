import math

request = input("""What do you want to calculate?
type "n" - for count of months,
type "a" - for annuity monthly payment,
type "d" - for differentiated payment plan
type "p" - for credit principal: \n""")

def annuity_function():
    p = int(input("Enter the credit principal: \n  "))
    n = int(input("Enter count of periods: \n  "))
    i = (float(input("Enter credit interest: \n")) / 100) / 12
    a = p * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    annuity = math.ceil(a)
    print(f"Your annuity payment = {annuity}!")

def period_function():
    p = float(input("Enter the credit principal: \n"))
    a = int(input("Enter monthly payment: \n"))
    i = (float(input("Enter credit interest: \n")) / 100) / 12
    n = math.log(a / (a - i * p), (1 + i))
    number = math.ceil(n)
    years = number // 12
    months = number % 12
    print(f"You need {years} years and {months} months to repay this credit!")

def principle_function():
    a = float(input("Enter monthly payment: \n"))
    n = int(input("Enter count of periods: \n"))
    i = (float(input("Enter credit interest: \n")) / 100) / 12
    p = a / ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1))
    principle = round(p, 0)
    print(f"Your credit principal = {principle}!")

def differentiated_payment():
    p = int(input("Enter the credit principal: \n"))
    n = int(input("Enter count of periods: \n"))
    i = (float(input("Enter credit interest: \n")) / (100 * 12))
    m = 1
    sum_ = 0
    while m <= n:
        formula = math.ceil(p / n + i * (p - (p * (m - 1)) / n))
        sum_ += formula
        print(f"Month {m}: paid out {formula}")
        m += 1
    over = int(sum_ - p)
    print(f"Overpayment = {over}")

if request == "a":
    annuity_function()
elif request == "n":
    period_function()
elif request == "p":
    principle_function()
elif request == "d":
    differentiated_payment()
else:
    print("Invalid command")