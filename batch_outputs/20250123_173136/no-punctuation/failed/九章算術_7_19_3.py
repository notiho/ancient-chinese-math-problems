"""
今有人持錢之蜀賈利十三初返歸一萬四千次返歸一萬三千次返歸一萬二千次返歸一萬一千後返歸一萬凡五返歸錢本利俱盡問本持錢及利各幾何
術曰假令本錢三萬不足一千七百三十八錢半令之四萬多三萬五千三百九十錢八分
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰本 a錢 利 b錢 
"""

"""
Suppose someone holds money and trades in Shu, gaining a profit of 13% each time. 
After the first return, they have 14,000 qian. After the second return, they have 13,000 qian. 
After the third return, they have 12,000 qian. After the fourth return, they have 11,000 qian. 
After the fifth and final return, they have 10,000 qian. 
In total, after five returns, the money, including both the principal and profit, is completely exhausted. 
Question: How much was the original principal, and how much was the profit?

The procedure says: Suppose the principal is 30,000 qian. It is insufficient by 1,738.5 qian. 
Suppose it is 40,000 qian. It exceeds by 3,539.8 qian.

The "Excess and Deficit" procedure says: Place the rate of profit, and the excess and deficit, each below their respective positions. 
Multiply the rate of profit by the excess and deficit, and combine them to form the dividend. 
Combine the excess and deficit to form the divisor. 
Divide the dividend by the divisor to obtain the principal. 
If there is a fraction, simplify it. 
The excess and deficit are used together to determine the result.

The answer says: the principal is *a* qian, and the profit is *b* qian.
"""

from fractions import Fraction

# 利率 13%
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
本錢_假1 = 30000
不足 = -1738.5

# 假令本錢四萬，多三萬五千三百九十錢八分
本錢_假2 = 40000
多 = 35390.8

# 盈不足術：置所出率，盈不足各居其下
盈不足_乘積1 = 利率 * 不足
盈不足_乘積2 = 利率 * 多

# 令維乘所出率并以為實
實 = 盈不足_乘積1 + 盈不足_乘積2

# 并盈不足為法
法 = 不足 + 多

# 實如法而一
本錢 = Fraction(實, 法)

# 利 = 本錢 * 利率
利 = 本錢 * 利率

a = 本錢
b = 利
"""
Code error: both arguments should be Rational instances"""
