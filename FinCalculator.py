import math
import sys

args = sys.argv
function_type = args[1]
function_type = function_type.split("=")
request = function_type[1]

substring1 = "principal"
substring1_in_args = [string for string in args if substring1 in string]
substring2 = "payment"
substring2_in_args = [string for string in args if substring2 in string]
substring3 = "interest"
substring3_in_args = [string for string in args if substring3 in string]
substring4 = "periods"
substring4_in_args = [string for string in args if substring4 in string]


def annuity_function():
    num1 = args[2]
    num1 = num1.split("=")
    p = int(num1[1])
    num2 = args[3]
    num2 = num2.split("=")
    n = int(num2[1])
    num3 = args[4]
    num3 = num3.split("=")
    i = (float(num3[1]) / 100) / 12
    a = p * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    annuity = math.ceil(a)
    full_payment = int(annuity) * int(n)
    overpay = full_payment - p
    print(f"Your annuity payment {annuity}!")
    print(f"Overpayment = {overpay}")

def period_function():
    num1 = args[2]
    num1 = num1.split("=")
    p = float(num1[1])
    num2 = args[3]
    num2 = num2.split("=")
    a = int(num2[1])
    num3 = args[4]
    num3 = num3.split("=")
    i = (float(num3[1]) / 100) / 12
    n = math.log(a / (a - i * p), (1 + i))
    number = math.ceil(n)
    years = number // 12
    months = number % 12
    over = a * (years * 12) - p
    if months == 0:
        print(f"You need {years} years to repay this credit!")
        print(f"Overpayment = {over}")
    else:
        print(f"You need {years} years and {months} months to repay this credit!")
        print(f"Overpayment = {over}")

def principal_function():
    num1 = args[2]
    num1 = num1.split("=")
    a = float(num1[1])
    num2 = args[3]
    num2 = num2.split("=")
    n = int(num2[1])
    num3 = args[4]
    num3 = num3.split("=")
    i = (float(num3[1]) / 100) / 12
    p = a / ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1))
    principle = round(p, 0)
    overpay = a * n - p
    print(f"Your credit principal = {principle}!")
    print(f"Overpayment = {overpay}")

def differentiated_payment():
    num1 = args[2]
    num1 = num1.split("=")
    p = int(num1[1])
    num2 = args[3]
    num2 = num2.split("=")
    n = int(num2[1])
    num3 = args[4]
    num3 = num3.split("=")
    i = (float(num3[1]) / (100 * 12))
    m = 1
    sum_ = 0
    while m <= n:
        formula = math.ceil(p / n + i * (p - (p * (m - 1)) / n))
        sum_ += formula
        print(f"Month {m}: paid out {formula}")
        m += 1
    over = int(sum_ - p)
    print(f"Overpayment = {over}")

if request == "annuity":
    if len(substring3_in_args) == 0:
        print("Incorrect parameters")
    elif len(substring3_in_args) == 1 and len(substring2_in_args) == 1 and len(substring4_in_args) == 1:
        principal_function()
    elif len(substring3_in_args) == 1 and len(substring1_in_args) == 1 and len(substring2_in_args) == 1:
        period_function()
    elif len(substring3_in_args) == 1 and len(substring1_in_args) == 1 and len(substring4_in_args) == 1:
        annuity_function()
    else:
        print("Incorrect parameters")

elif request == "diff":
    if len(substring2_in_args) == 1 or len(substring3_in_args) == 0:
        print("Incorrect parameters")
    else:
        differentiated_payment()
else:
    print("Incorrect parameters")