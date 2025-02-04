"""
今有金方七銀方九秤之適相當交易其一金輕七兩問金銀各重㡬何
術曰金銀方數相乗各以半輕數乗之為實以超方數乗金銀方數各自為法實如法而一
答曰金方重 a兩 銀方重 b兩
"""

"""
Suppose there is a block of gold with a side length of 7 and a block of silver with a side length of 9. 
When weighed, they balance perfectly. 
If one gold block is 7 liang lighter, question: how much does each block of gold and silver weigh?

The procedure says: Multiply the side lengths of gold and silver by themselves. 
Each is then multiplied by half the lighter weight, producing the dividend. 
Multiply the excess side length by the side lengths of gold and silver, producing the divisor for each. 
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
金方數 = 金方 ** 3
銀方數 = 銀方 ** 3

# 各以半輕數乗之，為實
實金 = 金方數 * Fraction(輕數, 2)
實銀 = 銀方數 * Fraction(輕數, 2)

# 以超方數乗金銀方數，各自為法
法金 = (銀方 - 金方) * 金方數
法銀 = (銀方 - 金方) * 銀方數

# 實如法而一
a = Fraction(實金, 法金)
b = Fraction(實銀, 法銀)
"""
Variable 'a' has wrong value. Expected: 63/4, Actual: 7/4
Variable 'b' has wrong value. Expected: 49/4, Actual: 7/4"""
