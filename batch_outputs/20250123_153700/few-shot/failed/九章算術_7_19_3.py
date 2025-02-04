"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
Suppose someone holds money in Shu (a unit of currency) and trades with a profit rate of 13%.
After the first return, they bring back 14,000; after the second return, 13,000; after the third return, 12,000; after the fourth return, 11,000; and after the fifth return, 10,000.
In total, they return the money five times, and the principal and profit are fully exhausted.
Question: how much was the original principal and how much was the profit?

The procedure says: Suppose the principal is 30,000, it falls short by 1,738.5. 
Suppose it is 40,000, it exceeds by 35,390.8.
The "Excess and Deficiency" procedure says: Place the profit rate, and the excess and deficiency below it respectively.
Multiply the profit rate by the excess and deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the principal.
If there is a fractional part, convert it.
For the excess and deficiency to align with the same transaction, place the profit rate, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the goods, and the divisor becomes the number of people.

Answer: The principal is *a* Shu, and the profit is *b* Shu.
"""

from fractions import Fraction

# 賈利十三 (profit rate of 13%)
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
假本1 = 30000
不足 = Fraction(17385, 10)

# 令之四萬，多三萬五千三百九十錢八分
假本2 = 40000
多 = Fraction(353908, 10)

# 盈不足術曰：置所出率，盈、不足各居其下
盈不足 = 多 - (-不足)

# 令維乘所出率，并以為實
實 = (假本1 * 多) + (假本2 * 不足)

# 并盈、不足為法
法 = 盈不足

# 實如法而一
本錢 = Fraction(實, 法)

# 利 = 本錢 * 利率
利 = 本錢 * 利率

# 答案
a = 本錢
b = 利
"""
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 113126400/28561"""
