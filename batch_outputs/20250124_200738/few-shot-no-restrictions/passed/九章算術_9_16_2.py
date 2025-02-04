"""
今有邑方二百步，各中開門。出東門十五步有木。問︰出南門幾何步而見木？
術曰：出東門步數為法，半邑方自乘為實，實如法得一步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with sides of 200 bu, and each side has a gate in the middle.
From the east gate, walking 15 bu, there is a tree.
Question: how many bu must one walk from the south gate to see the tree?

The procedure says: Take the number of bu walked from the east gate as the divisor.
Take half the side length of the city, square it to get the dividend.
Divide the dividend by the divisor to obtain the number of bu.

Answer: *a* bu.
"""

from fractions import Fraction

# 邑方二百步
邑方 = 200

# 出東門十五步
東門步數 = 15

# 半邑方
半邑方 = Fraction(邑方, 2)

# 半邑方自乘為實
實 = 半邑方 ** 2

# 實如法得一步
a = Fraction(實, 東門步數)

a#----- content ends here -----

"""
"""
