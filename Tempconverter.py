def tempConverter(temp, unit):
    if unit == "F":
        return (temp - 32) * 5 / 9
    if unit == "C":
        return temp * 1.8 + 32

temp = int(input("enter a temperature: "))
unit = input("enter a temperature unit: F/C ")

print("Your converted temperature is", tempConverter(temp, unit))





