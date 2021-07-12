def division(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        return round(num2 / num1, 7)
    except:
        print('Division by zero not possible')