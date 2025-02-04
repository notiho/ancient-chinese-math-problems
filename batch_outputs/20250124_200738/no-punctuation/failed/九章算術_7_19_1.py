"""
今有人持錢之蜀賈利十三初返歸一萬四千次返歸一萬三千次返歸一萬二千次返歸一萬一千後返歸一萬凡五返歸錢本利俱盡問本持錢及利各幾何
術曰假令本錢三萬不足一千七百三十八錢半令之四萬多三萬五千三百九十錢八分
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰本 a錢 利 b錢 
"""

#----- content starts here -----
"""
Suppose someone holds money to trade in Shu, gaining 13% profit each time. 
Initially, they return with 14,000 qian, then 13,000 qian, then 12,000 qian, then 11,000 qian, and finally 10,000 qian. 
In total, they return five times, and the money, including both principal and profit, is completely exhausted.
Question: What is the principal money held and the total profit?

The procedure says: Suppose the principal money is 30,000 qian. It is insufficient by 1,738.5 qian.
Suppose it is 40,000 qian. It exceeds by 3,539.8 qian.

The "Excess and Deficit" procedure says: Place the given rates of excess and deficit below each other. 
Multiply the given rates by their respective excess or deficit, and sum them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor to find the principal. 
If there are fractions, simplify them.
For the profit, use the principal and the given rate of profit.

Answer: The principal is *a* qian, and the profit is *b* qian.
"""

from fractions import Fraction

# 利率
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
本錢1 = 30000
不足 = -1738.5

# 假令本錢四萬，多三萬五千三百九十錢八分
本錢2 = 40000
多 = 3539.8

# 盈不足術
# 置所出率盈不足各居其下，令維乘所出率并以為實
實 = (本錢1 * 多) + (本錢2 * 不足)

# 并盈不足為法
法 = 多 + 不足

# 實如法而一
本錢 = Fraction(實, 法)

# 利 = 本錢 * 利率
利 = 本錢 * 利率

a = 本錢
b = 利#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
