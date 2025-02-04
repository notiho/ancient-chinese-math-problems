"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
Suppose someone holds money in Shu (a region), and the profit rate is 13%. 
The first return is 14,000 qian, the second return is 13,000 qian, the third return is 12,000 qian, the fourth return is 11,000 qian, and the final return is 10,000 qian. 
In total, there are five returns, and the principal and profit are fully exhausted. 

Question: What are the principal and the profit?

The procedure says: Suppose the principal is 30,000 qian, it is short by 1,738.5 qian. 
Suppose it is 40,000 qian, it exceeds by 35,390.8 qian. 
The "Excess and Deficiency" procedure says: Place the given rates, with the excess and deficiency below them. 
Multiply each rate by its corresponding excess or deficiency, and sum these to form the dividend. 
Sum the excess and deficiency to form the divisor. 
Divide the dividend by the divisor to find the result. If there is a remainder, adjust accordingly. 
For cases where excess and deficiency are related to buying goods, place the rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend represents the price of the goods, and the divisor represents the number of people.

Answer: The principal is *a* qian, and the profit is *b* qian.
"""

from fractions import Fraction

# 利率
利率 = Fraction(13, 100)

# 假設本金 30,000，盈不足計算
本金_假設1 = 30000
不足1 = 1738.5

# 假設本金 40,000，盈不足計算
本金_假設2 = 40000
盈2 = 35390.8

# 盈不足術計算
# 置所出率，盈、不足各居其下
盈不足_乘積1 = 本金_假設1 * 不足1
盈不足_乘積2 = 本金_假設2 * 盈2

# 令維乘所出率，并以為實
實 = 盈不足_乘積1 + 盈不足_乘積2

# 并盈、不足為法
法 = 盈2 + 不足1

# 實如法而一
本金 = Fraction(實, 法)

# 利 = 本金 * 利率
利 = 本金 * 利率

# 答案
a = 本金
b = 利
"""
Code error: both arguments should be Rational instances"""
