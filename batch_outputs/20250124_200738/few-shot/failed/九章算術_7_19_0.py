"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

#----- content starts here -----
"""
Suppose someone holds money in Shu (a region), and the profit rate is 13%. 
The person returns the following amounts over five instances:
First return: 14,000 qian
Second return: 13,000 qian
Third return: 12,000 qian
Fourth return: 11,000 qian
Fifth return: 10,000 qian
In total, the five returns completely repay both the principal and the profit.

Question: What are the amounts of the principal and the profit?

The procedure says:
Assume the principal is 30,000 qian. It is insufficient by 1,738.5 qian.
Assume the principal is 40,000 qian. It is excessive by 35,390.8 qian.
The "Excess and Deficit" procedure says:
Place the profit rate, and the excess and deficit below it, respectively.
Multiply the assumed principal by the profit rate, and add them to form the dividend.
Add the excess and deficit to form the divisor.
Divide the dividend by the divisor to find the principal. If there is a remainder, adjust it.
For the excess and deficit to align with the same transaction, place the profit rate and subtract the smaller from the larger.
Simplify the divisor and dividend. The dividend represents the price of the goods, and the divisor represents the number of people.

Answer: The principal is *a* qian, and the profit is *b* qian.
"""

from fractions import Fraction

# 利率
利率 = Fraction(13, 100)

# 假設本金 30,000，不足 1,738.5 錢
假設本金1 = 30000
不足 = Fraction(17385, 10)

# 假設本金 40,000，多 35,390.8 錢
假設本金2 = 40000
多 = Fraction(353908, 10)

# 盈不足術
# 置所出率，盈、不足各居其下
盈 = 多
不足 = 不足

# 令維乘所出率，并以為實
實1 = 假設本金1 * 利率 + 不足
實2 = 假設本金2 * 利率 - 多

# 并盈、不足為法
法 = 盈 - 不足

# 實如法而一
本金 = (實1 - 實2) / 法

# 利 = 本金 * 利率
利 = 本金 * 利率

a = 本金
b = 利#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 358293/336523
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 4657809/33652300"""
