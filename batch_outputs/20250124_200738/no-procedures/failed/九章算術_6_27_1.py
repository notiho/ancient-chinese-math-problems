"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose someone carries gold through five checkpoints. At the first checkpoint, for every 2 jin, 1 jin is taxed. At the second checkpoint, for every 3 jin, 1 jin is taxed. At the third checkpoint, for every 4 jin, 1 jin is taxed. At the fourth checkpoint, for every 5 jin, 1 jin is taxed. At the fifth checkpoint, for every 6 jin, 1 jin is taxed. The total tax across all five checkpoints is exactly 1 jin.

Question: How much gold did the person originally carry?

Answer: The person originally carried *a* jin of gold.
"""

# Define the fractions for each checkpoint
tax_fractions = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# Define the total tax
total_tax = 1

# Let the original amount of gold be x
# The remaining gold after each checkpoint is calculated iteratively
# Solve for x such that the total tax equals 1 jin
x = Fraction(0)  # Initialize x
for i in range(1, 1000):  # Iterate through possible values of x
    remaining_gold = Fraction(i)  # Start with i jin of gold
    taxed_gold = 0  # Initialize taxed gold
    for fraction in tax_fractions:
        tax = remaining_gold * fraction  # Tax at the current checkpoint
        taxed_gold += tax  # Add to the total taxed gold
        remaining_gold -= tax  # Subtract the tax from the remaining gold
    if taxed_gold == total_tax:  # Check if the total tax matches 1 jin
        x = Fraction(i)
        break

# The original amount of gold
a = x
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 0"""
