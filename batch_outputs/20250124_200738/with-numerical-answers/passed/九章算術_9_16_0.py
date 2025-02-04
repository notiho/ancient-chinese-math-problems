"""
今有邑方二百步，各中開門。出東門十五步有木。問︰出南門幾何步而見木？
術曰：出東門步數為法，半邑方自乘為實，實如法得一步。
荅曰： a(=2000/3)步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with each side being 200 bu, and gates are opened at the center of each side.
Exiting the east gate, after walking 15 bu, there is a tree.
Question: how many bu must one walk out of the south gate to see the tree?

The procedure says: Take the number of bu walked out of the east gate as the divisor.
Take half the side length of the city, square it, and use it as the dividend.
Divide the dividend by the divisor to obtain the number of bu.

Answer: *a*(=2000/3) bu.
"""

# 邑方二百步
邑方 = 200

# 出東門十五步
出東門步數 = 15

# 半邑方
半邑方 = Fraction(邑方, 2)

# 半邑方自乘為實
實 = 半邑方 * 半邑方

# 實如法得一步
a = Fraction(實, 出東門步數) # 2000/3#----- content ends here -----

"""
"""
