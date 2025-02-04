"""
今有邑方二百步各中開門出東門十五步有木問出南門幾何步而見木
術曰出東門步數為法半邑方自乘為實實如法得一步
荅曰 a步 
"""

"""
Suppose there is a square city with each side 200 bu. A gate is opened in the middle of each side.
From the east gate, walking 15 bu, there is a tree.
Question: how many bu must one walk from the south gate to see the tree?

The procedure says: Take the number of bu walked out of the east gate as the divisor.
Take half the side of the city, square it, as the dividend.
Divide the dividend by the divisor to obtain the number of bu.

The answer says: *a* bu.
"""

# 邑方二百步
邑方 = 200

# 出東門十五步
東門步數 = 15

# 半邑方
半邑方 = Fraction(邑方, 2)

# 半邑方自乘，為實
實 = 半邑方 * 半邑方

# 出東門步數為法
法 = 東門步數

# 實如法得一步
a = Fraction(實, 法)
"""
"""
