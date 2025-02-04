"""
今有金方七銀方九秤之適相當交易其一金輕七兩問金銀各重㡬何
術曰金銀方數相乗各以半輕數乗之為實以超方數乗金銀方數各自為法實如法而一
答曰金方重 a兩 銀方重 b兩
"""

#----- content starts here -----
"""
Suppose there is a block of gold with a side length of 7 and a block of silver with a side length of 9.
When weighed, they are perfectly balanced. If 1 block of gold is made lighter by 7 liang, how much do the gold and silver blocks weigh respectively?

The procedure says: Multiply the side lengths of the gold and silver blocks with each other.
For each, multiply by half the amount of the weight difference (7 liang), obtaining the dividend.
Multiply the side length of the other block by the side length of the block in question, obtaining the divisor.
Divide the dividend by the divisor to obtain the weight of each block.

Answer: the gold block weighs *a* liang, and the silver block weighs *b* liang.
"""

# 金方七
金方 = 7

# 銀方九
銀方 = 9

# 輕七兩
輕數 = 7

# 金銀方數相乗
金銀相乘 = 金方 * 銀方

# 各以半輕數乗之，為實
實金 = 金方 * (輕數 / 2)
實銀 = 銀方 * (輕數 / 2)

# 以超方數乗金銀方數，各自為法
法金 = 銀方 * 金方
法銀 = 金方 * 銀方

# 實如法而一
a = Fraction(實金, 法金)
b = Fraction(實銀, 法銀)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
