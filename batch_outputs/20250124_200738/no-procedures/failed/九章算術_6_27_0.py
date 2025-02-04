"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose a person carries gold through five checkpoints. At the first checkpoint, for every 2 jin, 1 jin is taxed. At the second checkpoint, for every 3 jin, 1 jin is taxed. At the third checkpoint, for every 4 jin, 1 jin is taxed. At the fourth checkpoint, for every 5 jin, 1 jin is taxed. At the fifth checkpoint, for every 6 jin, 1 jin is taxed. The total tax across all five checkpoints is exactly 1 jin.

Question: how much gold did the person originally carry?

Answer: the person originally carried *a* jin of gold.
"""

# Let the original amount of gold be x jin
from fractions import Fraction

# Define the tax rates at each checkpoint
tax_rate_1 = Fraction(1, 2)  # First checkpoint: 2 taxed 1
tax_rate_2 = Fraction(1, 3)  # Second checkpoint: 3 taxed 1
tax_rate_3 = Fraction(1, 4)  # Third checkpoint: 4 taxed 1
tax_rate_4 = Fraction(1, 5)  # Fourth checkpoint: 5 taxed 1
tax_rate_5 = Fraction(1, 6)  # Fifth checkpoint: 6 taxed 1

# The remaining gold after each checkpoint
# Let x be the original amount of gold
x = Fraction(1)  # Placeholder for the equation

# Work backwards through the checkpoints
# At the fifth checkpoint
remaining_after_5 = x / (1 - tax_rate_5)

# At the fourth checkpoint
remaining_after_4 = remaining_after_5 / (1 - tax_rate_4)

# At the third checkpoint
remaining_after_3 = remaining_after_4 / (1 - tax_rate_3)

# At the second checkpoint
remaining_after_2 = remaining_after_3 / (1 - tax_rate_2)

# At the first checkpoint
remaining_after_1 = remaining_after_2 / (1 - tax_rate_1)

# The total tax is given as 1 jin
total_tax = remaining_after_1 - x

# Solve for x such that total_tax = 1
a = remaining_after_1  # The original amount of gold carried

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 6"""
