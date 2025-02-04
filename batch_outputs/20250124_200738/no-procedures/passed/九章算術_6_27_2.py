"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose a person carries gold through five checkpoints. At the first checkpoint, for every 2 jin, 1 jin is taxed. At the second checkpoint, for every 3 jin, 1 jin is taxed. At the third checkpoint, for every 4 jin, 1 jin is taxed. At the fourth checkpoint, for every 5 jin, 1 jin is taxed. At the fifth checkpoint, for every 6 jin, 1 jin is taxed. The total tax collected across all five checkpoints is exactly 1 jin.

Question: how much gold did the person originally carry?

Answer: *a* jin.
"""

from fractions import Fraction

# Total tax collected across all checkpoints
total_tax = 1

# Let the original amount of gold be x jin
# After passing each checkpoint, the remaining gold is reduced by the tax rate.

# At the first checkpoint, for every 2 jin, 1 jin is taxed:
# Remaining gold after the first checkpoint = x * (2 - 1) / 2 = x * (1/2)
checkpoint_1 = Fraction(1, 2)

# At the second checkpoint, for every 3 jin, 1 jin is taxed:
# Remaining gold after the second checkpoint = checkpoint_1 * (3 - 1) / 3 = checkpoint_1 * (2/3)
checkpoint_2 = Fraction(2, 3)

# At the third checkpoint, for every 4 jin, 1 jin is taxed:
# Remaining gold after the third checkpoint = checkpoint_2 * (4 - 1) / 4 = checkpoint_2 * (3/4)
checkpoint_3 = Fraction(3, 4)

# At the fourth checkpoint, for every 5 jin, 1 jin is taxed:
# Remaining gold after the fourth checkpoint = checkpoint_3 * (5 - 1) / 5 = checkpoint_3 * (4/5)
checkpoint_4 = Fraction(4, 5)

# At the fifth checkpoint, for every 6 jin, 1 jin is taxed:
# Remaining gold after the fifth checkpoint = checkpoint_4 * (6 - 1) / 6 = checkpoint_4 * (5/6)
checkpoint_5 = Fraction(5, 6)

# The remaining gold after all checkpoints is the original amount minus the total tax:
# Remaining gold = x * checkpoint_1 * checkpoint_2 * checkpoint_3 * checkpoint_4 * checkpoint_5
remaining_gold = checkpoint_1 * checkpoint_2 * checkpoint_3 * checkpoint_4 * checkpoint_5

# Total tax = original gold - remaining gold
# total_tax = x - (x * remaining_gold)
# total_tax = x * (1 - remaining_gold)

# Solve for x (original gold):
a = Fraction(total_tax) / (1 - remaining_gold)

# Output the result
a#----- content ends here -----

"""
"""
