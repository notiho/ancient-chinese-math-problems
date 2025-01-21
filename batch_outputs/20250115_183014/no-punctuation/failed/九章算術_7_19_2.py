"""
今有人持錢之蜀賈利十三初返歸一萬四千次返歸一萬三千次返歸一萬二千次返歸一萬一千後返歸一萬凡五返歸錢本利俱盡問本持錢及利各幾何
術曰假令本錢三萬不足一千七百三十八錢半令之四萬多三萬五千三百九十錢八分
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰本 a錢 利 b錢 
"""

"""
Suppose someone holds money to trade in Shu, gaining a profit rate of 13%.
On the first return, they bring back 14,000. On the second return, they bring back 13,000. On the third return, they bring back 12,000. On the fourth return, they bring back 11,000. On the final return, they bring back 10,000.
In total, they return five times, and the money, both principal and profit, is completely exhausted.
Question: How much was the principal money held, and how much was the profit?

The procedure says: Suppose the principal money is 30,000. It is insufficient by 1,738.5 money.
Suppose it is 40,000. It is excessive by 3,539.8 money.
The "Excess and Deficiency" procedure says: Place the profit rate and the excess and deficiency values below each other.
Multiply the profit rate by the excess and deficiency values, and add them together to form the dividend.
Add the excess and deficiency values to form the divisor.
Divide the dividend by the divisor to obtain the principal. If there is a fractional part, adjust it.
The excess and deficiency values are used together.
For the goods purchased, place the profit rate, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the goods, and the divisor becomes the number of people.

Answer: The principal is *a* money, and the profit is *b* money.
"""

# 利率 13%
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
本錢1 = 30000
不足 = -1738.5

# 假令本錢四萬，多三萬五千三百九十錢八分
本錢2 = 40000
多 = 3539.8

# 盈不足術：置所出率，盈不足各居其下
盈不足1 = 不足
盈不足2 = 多

# 令維乘所出率，并以為實
實 = (本錢1 * 盈不足2) + (本錢2 * abs(盈不足1))

# 并盈不足為法
法 = 盈不足2 - 盈不足1

# 實如法而一
本錢 = Fraction(實, 法)

# 利 b 錢
利 = 本錢 * 利率

# 答案
a = 本錢
b = 利
"""
Code error: both arguments should be Rational instances"""
