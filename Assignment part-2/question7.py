input_string = input("Enter a string: ")
digits = sum(c.isdigit() for c in input_string)
letters = sum(c.isalpha() for c in input_string)

print(f"Number of digits: {digits}")
print(f"Number of letters: {letters}")
