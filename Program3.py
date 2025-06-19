while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

sum_even = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

print(f"The sum of even numbers between 1 and {n} is {sum_even}")