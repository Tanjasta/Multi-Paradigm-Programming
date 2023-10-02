# https://realpython.com/python-sum-function/
# https://beat0154.github.io/Python-Programming-Portfolio/
# https://www.geeksforgeeks.org/count-sum-of-digits-in-numbers-from-1-to-n/
n = int(input("Please enter a number: "))
choice = int(input("Enter 1 to compute the sum or 2 to compute the product: "))

if choice == 1:
    # Compute the sum of 1 to n
    sum_of_numbers = 0
    for i in range(1, n + 1):
        sum_of_numbers += i
    print(f"The sum of numbers from 1 to {n} is: {sum_of_numbers}")
elif choice == 2:
    # Compute the product of 1 to n
    product_of_numbers = 1
    for i in range(1, n + 1):
        product_of_numbers *= i
    print(f"The product of numbers from 1 to {n} is: {product_of_numbers}")
else:
    print("Wrong choice. Please enter 1 or 2.")