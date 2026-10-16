# Program to help Rohan choose weather-appropriate clothes

# Take temperature input from Rohan
temperature = float(input("Enter the current temperature in Celsius: "))

# Set a suitable threshold for light clothes (e.g., 20 degrees Celsius)
if temperature >= 20:
    print("It's warm enough! You can wear light and soft clothes today. ☀️")
else:
    print("It's too cold! Keep your jacket and pullover on so you don't catch a cold. ❄️")
