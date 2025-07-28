FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit: float):
    # Convert Fahrenheit to Celsius
    #fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius: float):
    # Convert Celsius to Fahrenheit
    #celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp = int(input("Enter the temperature to convert:"))
choice_of_conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if choice_of_conversion == 'C':
    converted_temp = convert_to_fahrenheit(temp)
    print(f"{temp:.1f}C is {converted_temp:.14f}F")
elif choice_of_conversion == 'F':
    converted_temp = convert_to_celsius(temp)
    print(f"{temp:.1f}F is {converted_temp:.14f}C")
else:
    print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
