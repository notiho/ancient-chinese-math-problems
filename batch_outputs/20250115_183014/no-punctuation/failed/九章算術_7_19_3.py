"""
今有人持錢之蜀賈利十三初返歸一萬四千次返歸一萬三千次返歸一萬二千次返歸一萬一千後返歸一萬凡五返歸錢本利俱盡問本持錢及利各幾何
術曰假令本錢三萬不足一千七百三十八錢半令之四萬多三萬五千三百九十錢八分
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰本 a錢 利 b錢 
"""

"""
Suppose someone carries money to Shu for trade, with a profit rate of 13%. 
Upon returning the first time, they have 14,000 qian. 
The second return, they have 13,000 qian. 
The third return, they have 12,000 qian. 
The fourth return, they have 11,000 qian. 
The fifth and final return, they have 10,000 qian. 
After five returns, the money, including both principal and profit, is completely exhausted. 
Question: What was the initial principal and the total profit?

The procedure says: Suppose the initial principal is 30,000 qian. 
It is insufficient by 1,738.5 qian. 
Suppose it is 40,000 qian. 
It exceeds by 3,539.8 qian. 

The "Excess and Deficit" procedure says: Place the profit rate, the excess, and the deficit in their respective positions. 
Multiply the profit rate by the excess and deficit, and combine them to form the dividend. 
Combine the excess and deficit to form the divisor. 
Divide the dividend by the divisor to find the principal. 
If there is a fractional part, adjust it. 
The excess and deficit must correspond to the same unit. 

For those purchasing goods, place the profit rate. 
Subtract the smaller from the larger, and reduce the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the goods, and the divisor becomes the number of people.

Answer: The principal is *a* qian, and the profit is *b* qian.
"""

from fractions import Fraction

# 利率 13%
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
本錢_假1 = 30000
不足 = Fraction(17385, 10)

# 假令本錢四萬，多三萬五千三百九十錢八分
本錢_假2 = 40000
多 = Fraction(353908, 100)

# 盈不足術：置所出率，盈不足各居其下
盈 = 多
不足 = 不足

# 令維乘所出率，并以為實
實 = (盈 * 本錢_假1) + (不足 * 本錢_假2)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
本錢 = Fraction(實, 法)

# 利 = 本錢 * 利率
利 = 本錢 * 利率

a = 本錢
b = 利
"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 8785620000/263879
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 1142130600/263879"""
