"""
今有邑方二百步，各中開門。出東門十五步有木。問︰出南門幾何步而見木？
術曰：出東門步數為法，半邑方自乘為實，實如法得一步。
荅曰： a步 。
"""

"""
Suppose there is a square city with a side length of 200 bu, and there is a gate in the middle of each side.
Exiting the east gate, after walking 15 bu, there is a tree.
Question: how many bu must one walk out of the south gate to see the tree?

The procedure says: Take the number of steps walked out of the east gate as the divisor.
Take half the side length of the city, square it to get the dividend.
Divide the dividend by the divisor to obtain the number of steps.

Answer: *a* bu.
"""

# 邑方二百步
邑方 = 200

# 出東門十五步
東門步數 = 15

# 半邑方
半邑方 = Fraction(邑方, 2)

# 半邑方自乘為實
實 = 半邑方 * 半邑方

# 實如法得一步
a = Fraction(實, 東門步數)
"""
"""
