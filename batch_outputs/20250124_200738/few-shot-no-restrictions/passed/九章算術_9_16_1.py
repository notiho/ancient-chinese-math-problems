"""
今有邑方二百步，各中開門。出東門十五步有木。問︰出南門幾何步而見木？
術曰：出東門步數為法，半邑方自乘為實，實如法得一步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with each side 200 bu. Each side has a gate in the middle.
Exiting the east gate and walking 15 bu, there is a tree.
Question: how many bu must one walk after exiting the south gate to see the tree?

The procedure says: Take the number of bu walked after exiting the east gate as the divisor.
Take half the side length of the city, square it to get the dividend.
Divide the dividend by the divisor to obtain the number of bu.

Answer: *a* bu.
"""

from fractions import Fraction

# 邑方二百步 (side length of the square city)
邑方 = 200

# 出東門十五步 (distance walked after exiting the east gate)
出東門步數 = 15

# 半邑方 (half the side length of the city)
半邑方 = Fraction(邑方, 2)

# 半邑方自乘為實 (square half the side length to get the dividend)
實 = 半邑方 ** 2

# 實如法得一步 (divide the dividend by the divisor to get the result)
a = Fraction(實, 出東門步數)

a  # Result in bu#----- content ends here -----

"""
"""
