# https://stackoverflow.com/questions/20415384/properly-formatted-multiplication-table
# https://www.geeksforgeeks.org/program-to-print-multiplication-table-of-a-number/
# https://beginnersbook.com/2018/06/python-program-print-multiplication-table/
# Iterate over the numbers from 1 to 12
for i in range(1, 13):
    # Iterate over the numbers from 1 to 12
    for j in range(1, 13):
        # Print the multiplication table for the current pair of numbers
        print(f"{i} x {j} = {i*j}")
    # Print a blank line after each multiplication table
    print()
