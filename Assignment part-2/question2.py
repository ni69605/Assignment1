# Prompt the user for two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display the result with two decimal places
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2:.2f}")
else:
    print("Error: Cannot divide by zero.")
