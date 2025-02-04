"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a斤 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the original weight of gold (`a`) that, after passing through five checkpoints with different tax rates, results in a total tax of 1 jin.

Here is the Python code:


"""


from fractions import Fraction

# Tax rates at each checkpoint
tax_rates = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# Let the total tax be 1 jin
total_tax = Fraction(1)

# Calculate the original weight of gold (a)
a = total_tax
for rate in reversed(tax_rates):
    a = a / (1 - rate)

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the original weight of gold in jin.
"""


"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 6"""
