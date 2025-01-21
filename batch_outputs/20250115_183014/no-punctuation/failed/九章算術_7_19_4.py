"""
今有人持錢之蜀賈利十三初返歸一萬四千次返歸一萬三千次返歸一萬二千次返歸一萬一千後返歸一萬凡五返歸錢本利俱盡問本持錢及利各幾何
術曰假令本錢三萬不足一千七百三十八錢半令之四萬多三萬五千三百九十錢八分
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰本 a錢 利 b錢 
"""

"""
Suppose there is a person who holds money and trades in Shu, gaining a profit rate of 13%.
Initially, they return with 14,000 coins, then 13,000 coins, then 12,000 coins, then 11,000 coins, and finally 10,000 coins.
After five returns, the principal and profit are completely exhausted.
Question: What are the original principal and the total profit?

The procedure says: Suppose the principal is 30,000 coins. It is insufficient by 1,738.5 coins.
Suppose it is 40,000 coins. It exceeds by 3,539.8 coins.
The "Excess and Deficit" procedure says: Place the profit rate, the excess, and the deficit below each other.
Multiply the profit rate by the excess and the deficit, and sum them to form the dividend.
Sum the excess and the deficit to form the divisor.
Divide the dividend by the divisor to find the principal. If there is a fraction, convert it.
The excess and deficit are used together.
For the goods purchased, place the profit rate, subtract the smaller from the larger, and reduce the divisor and dividend.
The dividend becomes the price of the goods, and the divisor becomes the number of people.

Answer: The principal is *a* coins, and the profit is *b* coins.
"""

# 利率
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
本錢_1 = 30000
不足 = Fraction(17385, 10)

# 假令本錢四萬，多三萬五千三百九十錢八分
本錢_2 = 40000
多 = Fraction(353908, 100)

# 盈不足術
# 置所出率，盈不足各居其下
盈不足_1 = 不足
盈不足_2 = 多

# 令維乘所出率，并以為實
實 = (盈不足_1 * 本錢_2) + (盈不足_2 * 本錢_1)

# 并盈不足為法
法 = 盈不足_1 + 盈不足_2

# 實如法而一
本錢 = Fraction(實, 法)

# 利 = 本錢 * 利率
利 = 本錢 * 利率

a = 本錢
b = 利
"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 8785620000/263879
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 1142130600/263879"""
