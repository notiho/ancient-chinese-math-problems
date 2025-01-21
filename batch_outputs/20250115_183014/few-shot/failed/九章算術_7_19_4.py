"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：本 a錢 。利 b錢 。
"""

"""
Suppose someone holds money in Shu (a region), and trades with a profit rate of 13%. 
The first return is 14,000 qian, the second return is 13,000 qian, the third return is 12,000 qian, the fourth return is 11,000 qian, and the final return is 10,000 qian. 
In total, there are five returns, and the principal and profit are fully exhausted.
Question: how much was the original principal and the total profit?

The procedure says: Suppose the principal is 30,000 qian, it is short by 1,738.5 qian. 
Suppose it is 40,000 qian, it is over by 35,390.8 qian. 
The procedure for excess and deficiency says: Place the profit rate, and the excess and deficiency below it. 
Multiply the profit rate by the excess and deficiency, and sum them to form the dividend. 
Sum the excess and deficiency to form the divisor. 
Divide the dividend by the divisor to find the principal. 
If there is a fraction, convert it. 
For the excess and deficiency corresponding to the same trade item, place the profit rate, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: the principal is *a* qian, and the profit is *b* qian.
"""

from fractions import Fraction

# 利率
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
假本1 = 30000
不足 = Fraction(17385, 10)

# 令之四萬，多三萬五千三百九十錢八分
假本2 = 40000
多 = Fraction(353908, 10)

# 盈不足術曰：置所出率，盈、不足各居其下
盈不足 = 多 - 不足

# 令維乘所出率，并以為實
實 = (假本1 * 多) + (假本2 * 不足)

# 并盈、不足為法
法 = 盈不足

# 實如法而一
本 = Fraction(實, 法)

# 利 = 總返歸錢 - 本
總返歸錢 = 14000 + 13000 + 12000 + 11000 + 10000
利 = 總返歸錢 - 本

a = 本
b = 利
"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 11312640000/336523
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 8878740000/336523"""
