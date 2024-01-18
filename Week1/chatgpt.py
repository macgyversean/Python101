# Get the temperature in degrees Celsius from the user
celsius_temperature = float(input("Enter the temperature in degrees Celsius: "))

# Convert Celsius to Fahrenheit using the formula F = (C * 9/5) + 32
fahrenheit_temperature = (celsius_temperature * 9/5) + 32

# Display the converted temperature to the user
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")