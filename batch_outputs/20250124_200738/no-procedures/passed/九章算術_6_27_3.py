"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose someone carries gold through five checkpoints. At the first checkpoint, for every 2 jin, 1 jin is taxed. At the second checkpoint, for every 3 jin, 1 jin is taxed. At the third checkpoint, for every 4 jin, 1 jin is taxed. At the fourth checkpoint, for every 5 jin, 1 jin is taxed. At the fifth checkpoint, for every 6 jin, 1 jin is taxed. The total tax across all five checkpoints is exactly 1 jin.

Question: how much gold did the person originally carry?

Answer: *a* jin.
"""

from fractions import Fraction

# Let the original amount of gold be x jin
# After passing each checkpoint, the remaining gold is reduced by the tax rate.

# Remaining gold after each checkpoint:
# First checkpoint: for every 2 jin, 1 jin is taxed -> remaining = x * (1 - 1/2) = x * 1/2
# Second checkpoint: for every 3 jin, 1 jin is taxed -> remaining = (x * 1/2) * (1 - 1/3) = x * 1/2 * 2/3
# Third checkpoint: for every 4 jin, 1 jin is taxed -> remaining = (x * 1/2 * 2/3) * (1 - 1/4) = x * 1/2 * 2/3 * 3/4
# Fourth checkpoint: for every 5 jin, 1 jin is taxed -> remaining = (x * 1/2 * 2/3 * 3/4) * (1 - 1/5) = x * 1/2 * 2/3 * 3/4 * 4/5
# Fifth checkpoint: for every 6 jin, 1 jin is taxed -> remaining = (x * 1/2 * 2/3 * 3/4 * 4/5) * (1 - 1/6) = x * 1/2 * 2/3 * 3/4 * 4/5 * 5/6

# Total tax is 1 jin:
# Tax = original gold - remaining gold
# 1 = x - (x * 1/2 * 2/3 * 3/4 * 4/5 * 5/6)

# Solve for x:
remaining_fraction = Fraction(1, 2) * Fraction(2, 3) * Fraction(3, 4) * Fraction(4, 5) * Fraction(5, 6)
tax_fraction = 1 - remaining_fraction
a = Fraction(1) / tax_fraction

# Output the result
a#----- content ends here -----

"""
"""
