"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a斤 。
"""

"""
To solve this problem, we need to calculate the original amount of gold (denoted as `a`) that a person carried through five checkpoints. At each checkpoint, a fraction of the gold is taxed, and the total tax collected across all checkpoints equals 1 jin. The tax rates at the checkpoints are as follows:

- At the first checkpoint, 1/2 of the gold is taxed.
- At the second checkpoint, 1/3 of the gold is taxed.
- At the third checkpoint, 1/4 of the gold is taxed.
- At the fourth checkpoint, 1/5 of the gold is taxed.
- At the fifth checkpoint, 1/6 of the gold is taxed.

The solution involves calculating the original amount of gold such that the total tax collected equals 1 jin.

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Tax rates at each checkpoint
tax_rates = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# Total tax collected
total_tax = Fraction(1, 1)

# Calculate the original amount of gold (a)
a = total_tax / sum(tax_rates)

# Output the result
a


"""


The value of `a` will represent the original amount of gold in jin.
"""


"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 20/29"""
