"""
今有善行者行一百步不善行者行六十步今不善行者先行一百步善行者追之問幾何步及之
術曰置善行者一百步減不善行者六十步餘四十步以為法以善行者之一百步乘不善行者先行一百步為實實如法得一步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose a good walker walks 100 bu, while a poor walker walks 60 bu.
Now, the poor walker starts 100 bu ahead, and the good walker chases after them.
Question: after how many bu will the good walker catch up?

The procedure says: Place the 100 bu of the good walker and subtract the 60 bu of the poor walker.
The remainder, 40 bu, is taken as the divisor.
Multiply the 100 bu of the good walker by the 100 bu that the poor walker started ahead, obtaining the dividend.
Divide the dividend by the divisor, obtaining the number of bu.

The answer says: *a* bu.
"""

# 善行者行一百步
善行者步 = 100

# 不善行者行六十步
不善行者步 = 60

# 不善行者先行一百步
不善行者先行 = 100

# 置善行者一百步減不善行者六十步，餘四十步以為法
法 = 善行者步 - 不善行者步

# 以善行者之一百步乘不善行者先行一百步，為實
實 = 善行者步 * 不善行者先行

# 實如法得一步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
