"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose someone carries gold through five checkpoints. 
- At the first checkpoint, for every 2 jin, 1 jin is taxed.
- At the second checkpoint, for every 3 jin, 1 jin is taxed.
- At the third checkpoint, for every 4 jin, 1 jin is taxed.
- At the fourth checkpoint, for every 5 jin, 1 jin is taxed.
- At the fifth checkpoint, for every 6 jin, 1 jin is taxed.

The total tax from all five checkpoints is exactly 1 jin. 
Question: how much gold did the person originally carry?

Answer: the person originally carried *a* jin of gold.
"""

from fractions import Fraction

# Let the original amount of gold be `x` jin
# After each checkpoint, the remaining gold is reduced by the tax rate.

# First checkpoint: for every 2 jin, 1 jin is taxed
remaining_after_first = Fraction(1, 2)

# Second checkpoint: for every 3 jin, 1 jin is taxed
remaining_after_second = Fraction(2, 3)

# Third checkpoint: for every 4 jin, 1 jin is taxed
remaining_after_third = Fraction(3, 4)

# Fourth checkpoint: for every 5 jin, 1 jin is taxed
remaining_after_fourth = Fraction(4, 5)

# Fifth checkpoint: for every 6 jin, 1 jin is taxed
remaining_after_fifth = Fraction(5, 6)

# The total remaining gold after all checkpoints is the product of these fractions
total_remaining_fraction = (
    remaining_after_first
    * remaining_after_second
    * remaining_after_third
    * remaining_after_fourth
    * remaining_after_fifth
)

# The total tax is 1 jin, so the original amount of gold `x` satisfies:
# x - (x * total_remaining_fraction) = 1
# Simplify to solve for `x`:
# x * (1 - total_remaining_fraction) = 1
# x = 1 / (1 - total_remaining_fraction)

a = Fraction(1, 1 - total_remaining_fraction)

# Output the result
a#----- content ends here -----

"""
"""
