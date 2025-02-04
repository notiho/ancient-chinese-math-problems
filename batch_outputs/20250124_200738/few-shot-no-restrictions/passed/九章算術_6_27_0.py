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
The total tax across all five checkpoints equals exactly 1 jin.
Question: how much gold was originally carried?

The procedure says: Place 1 jin (the total tax), and multiply it by the product of all the tax rates to obtain the dividend.
Also multiply the product of all the non-taxed portions to subtract from the total product, and the remainder becomes the divisor.
Divide the dividend by the divisor to obtain the original amount of gold.

Answer: *a* jin.
"""

from fractions import Fraction

# Tax rates for each checkpoint
rates = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# Total tax
total_tax = 1

# Calculate the product of all tax rates (numerators)
tax_product = 1
for rate in rates:
    tax_product *= rate.numerator

# Calculate the product of all denominators (total portions)
total_product = 1
for rate in rates:
    total_product *= rate.denominator

# Calculate the product of all non-taxed portions (denominator - numerator)
non_taxed_product = 1
for rate in rates:
    non_taxed_product *= (rate.denominator - rate.numerator)

# The divisor
法 = total_product - non_taxed_product

# The dividend
實 = total_tax * total_product

# Original amount of gold
a = Fraction(實, 法)

a  # Output the result in jin#----- content ends here -----

"""
"""
