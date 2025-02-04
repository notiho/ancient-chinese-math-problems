"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a斤 。
"""

"""
To solve this problem, we need to calculate the original amount of gold ("a") that a person carried through five checkpoints, where each checkpoint taxes a fraction of the gold. The total tax collected across all checkpoints equals 1 jin. Let's translate this into Python code:


"""


from fractions import Fraction

# Tax rates at each checkpoint
tax_rates = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# Calculate the effective fraction of gold remaining after passing through all checkpoints
remaining_fraction = 1
for rate in tax_rates:
    remaining_fraction *= (1 - rate)

# The total tax collected is 1 jin, so the original amount of gold is:
a = Fraction(1) / (1 - remaining_fraction)

# Output the result
a  # This is the original amount of gold in jin


"""


The variable `a` will contain the original amount of gold in jin as a `Fraction`.
"""


"""
"""
