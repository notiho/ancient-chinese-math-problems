"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose a person carries gold through five checkpoints. 
At the first checkpoint, for every 2 jin, 1 jin is taxed.
At the second checkpoint, for every 3 jin, 1 jin is taxed.
At the third checkpoint, for every 4 jin, 1 jin is taxed.
At the fourth checkpoint, for every 5 jin, 1 jin is taxed.
At the fifth checkpoint, for every 6 jin, 1 jin is taxed.
The total tax across all five checkpoints equals exactly 1 jin.
Question: how much gold did the person originally carry?

The procedure says: Place 1 jin (the total tax), and multiply it by the product of all the tax rates to get the dividend.
Also, subtract the product of all the untaxed portions from the total product to get the divisor.
Divide the dividend by the divisor to find the original amount of gold.

Answer: The person originally carried *a* jin.
"""

from fractions import Fraction

# Tax rates at each checkpoint
rates = [2, 3, 4, 5, 6]

# Total tax across all checkpoints
total_tax = 1

# Calculate the product of all tax rates (通所稅者)
tax_product = 1
for rate in rates:
    tax_product *= rate

# Calculate the product of all untaxed portions (通其不稅者)
untaxed_product = 1
for rate in rates:
    untaxed_product *= (rate - 1)

# Calculate the divisor (餘為法)
法 = tax_product - untaxed_product

# Calculate the dividend (實)
實 = total_tax * tax_product

# Calculate the original amount of gold (實如法得一斤)
a = Fraction(實, 法)

a  # The original amount of gold in jin#----- content ends here -----

"""
"""
