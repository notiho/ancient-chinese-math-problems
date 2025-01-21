"""
今有金方七銀方九秤之適相當交易其一金輕七兩問金銀各重㡬何
術曰金銀方數相乗各以半輕數乗之為實以超方數乗金銀方數各自為法實如法而一
答曰金方重 a兩 銀方重 b兩
"""

"""
Suppose there is a block of gold with a side length of 7 and a block of silver with a side length of 9. 
When weighed, they are exactly balanced. 
If one gold block is made lighter by 7 liang, how much does each block of gold and silver weigh?

The procedure says: Multiply the side lengths of gold and silver with each other. 
For each, multiply by half the amount of the weight difference, obtaining the dividend. 
Multiply the side lengths of the other block by the side length of the block in question, obtaining the divisor.
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
金實 = Fraction(輕數, 2) * 銀方
銀實 = Fraction(輕數, 2) * 金方

# 以超方數乗金銀方數，各自為法
金法 = 銀方 * 金方
銀法 = 金方 * 銀方

# 實如法而一
a = Fraction(金實, 金法)
b = Fraction(銀實, 銀法)
"""
Variable 'a' has wrong value. Expected: 63/4, Actual: 1/2
Variable 'b' has wrong value. Expected: 49/4, Actual: 7/18"""
