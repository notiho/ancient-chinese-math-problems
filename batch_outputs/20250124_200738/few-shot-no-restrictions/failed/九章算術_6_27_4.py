"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose someone carries gold through five checkpoints. 
At the first checkpoint, for every 2 jin, 1 jin is taxed.
At the second checkpoint, for every 3 jin, 1 jin is taxed.
At the third checkpoint, for every 4 jin, 1 jin is taxed.
At the fourth checkpoint, for every 5 jin, 1 jin is taxed.
At the fifth checkpoint, for every 6 jin, 1 jin is taxed.
The total tax across all five checkpoints is exactly 1 jin.
Question: how much gold was originally carried?

The procedure says: Place 1 jin (the total tax), and multiply it by the product of all the tax rates to get the dividend.
Also, subtract the product of all the untaxed portions from the total product to get the divisor.
Divide the dividend by the divisor to get the original amount of gold.

Answer: *a* jin.
"""

from fractions import Fraction

# Tax rates for each checkpoint
rates = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# Untaxed portions for each checkpoint
untaxed = [1 - rate for rate in rates]

# Total tax across all checkpoints
total_tax = 1  # 1 jin

# Multiply all tax rates together to get the numerator (實)
實 = total_tax
for rate in rates:
    實 *= (1 / rate)

# Multiply all untaxed portions together and subtract from the numerator to get the denominator (法)
法 = 1
for portion in untaxed:
    法 *= portion

# Calculate the original amount of gold
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 4320"""
