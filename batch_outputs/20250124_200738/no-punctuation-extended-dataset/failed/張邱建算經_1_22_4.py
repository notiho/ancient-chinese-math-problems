"""
今有金方七銀方九秤之適相當交易其一金輕七兩問金銀各重㡬何
術曰金銀方數相乗各以半輕數乗之為實以超方數乗金銀方數各自為法實如法而一
答曰金方重 a兩 銀方重 b兩
"""

#----- content starts here -----
"""
Suppose there is a block of gold with a side length of 7 and a block of silver with a side length of 9. 
When weighed, they balance perfectly. If one piece of gold is reduced by 7 liang, 
how much does each block of gold and silver weigh?

The procedure says: Multiply the side lengths of gold and silver by themselves. 
Then, multiply each by half the reduced weight to obtain the dividend. 
Multiply the side lengths of the other block by the side length of the block in question to obtain the divisor. 
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
金方平方 = 金方 * 金方
銀方平方 = 銀方 * 銀方

# 各以半輕數乗之為實
金實 = 金方平方 * Fraction(輕數, 2)
銀實 = 銀方平方 * Fraction(輕數, 2)

# 以超方數乗金銀方數各自為法
金法 = 銀方 * 金方
銀法 = 金方 * 銀方

# 實如法而一
a = Fraction(金實, 金法)
b = Fraction(銀實, 銀法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 63/4, Actual: 49/18
Variable 'b' has wrong value. Expected: 49/4, Actual: 9/2"""
