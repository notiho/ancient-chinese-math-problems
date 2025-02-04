"""
今有金方七銀方九秤之適相當交易其一金輕七兩問金銀各重㡬何
術曰金銀方數相乗各以半輕數乗之為實以超方數乗金銀方數各自為法實如法而一
答曰金方重 a兩 銀方重 b兩
"""

#----- content starts here -----
"""
Suppose there is a gold block with 7 units of volume and a silver block with 9 units of volume. 
When weighed, they balance perfectly. 
If one gold block is 7 liang lighter, how much does each block of gold and silver weigh?

The procedure says: Multiply the volumes of gold and silver by each other. 
Then, for each, multiply by half the lighter weight (7 liang). 
This gives the dividend. 
For each, multiply the excess volume by the volume of the other block. 
This gives the divisor. 
Divide the dividend by the divisor to find the weight of each block.

Answer: The gold block weighs *a* liang, and the silver block weighs *b* liang.
"""

# 金方七
金方 = 7

# 銀方九
銀方 = 9

# 輕七兩
輕數 = 7

# 金銀方數相乗
金銀方積 = 金方 * 銀方

# 各以半輕數乗之，為實
實金 = 金方 * (輕數 / 2)
實銀 = 銀方 * (輕數 / 2)

# 以超方數乗金銀方數，各自為法
法金 = (銀方 - 金方) * 金方
法銀 = (金方 - 銀方) * 銀方

# 實如法而一
a = Fraction(實金, 法金)
b = Fraction(實銀, 法銀)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
