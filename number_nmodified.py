# https://stackoverflow.com/questions/62986101/python-sum-of-multiples-of-3-or-5-below-1000
# https://www.geeksforgeeks.org/multiples-of-3-or-7/
# https://www.reddit.com/r/haskell/comments/vrmimj/find_the_sum_of_all_the_unique_multiples_of/

# Ask the user for input
n = int(input("Enter a number: "))

# Initialize a variable to store the sum
sum_of_multiples = 0

# Calculate the sum of multiples of 3 or 5 from 1 to n
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_multiples += i

# Print the result
print(f"The sum of multiples of 3 or 5 from 1 to {n} is: {sum_of_multiples}")
