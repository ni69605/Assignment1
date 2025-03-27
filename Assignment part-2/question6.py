# Loop through numbers between 1500 and 2000 (inclusive)
for number in range(1500, 2001):
    # Check if the number is divisible by 7 and a multiple of 5
    if number % 7 == 0 and number % 5 == 0:
        print(number)
