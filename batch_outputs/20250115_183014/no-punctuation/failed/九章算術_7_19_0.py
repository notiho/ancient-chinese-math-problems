"""
今有人持錢之蜀賈利十三初返歸一萬四千次返歸一萬三千次返歸一萬二千次返歸一萬一千後返歸一萬凡五返歸錢本利俱盡問本持錢及利各幾何
術曰假令本錢三萬不足一千七百三十八錢半令之四萬多三萬五千三百九十錢八分
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰本 a錢 利 b錢 
"""

"""
Suppose someone holds money and trades in Shu, gaining a profit rate of 13%. 
On the first return, they have 14,000; on the second return, they have 13,000; on the third return, they have 12,000; on the fourth return, they have 11,000; and on the final return, they have 10,000. 
After five returns, the money, including both principal and profit, is completely exhausted.
Question: What is the original principal and the total profit?

The procedure says: Suppose the principal is 30,000; it is insufficient by 1,738.5. 
Suppose it is 40,000; it exceeds by 3,539.8. 
Using the "Excess and Deficiency" method: Place the profit rate and the excess and deficiency below each other. 
Multiply the profit rate by the excess and deficiency, and sum them to obtain the dividend. 
Sum the excess and deficiency to obtain the divisor. 
Divide the dividend by the divisor to find the principal. 
If there is a fraction, convert it. 
The excess and deficiency are mutually adjusted. 
For the goods purchased, place the profit rate, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend becomes the price of the goods, and the divisor becomes the number of people.

Answer: The principal is *a* qian, and the profit is *b* qian.
"""

# 利率
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
本錢1 = 30000
不足 = -1738.5

# 假令本錢四萬，多三千五百三十九錢八分
本錢2 = 40000
盈 = 3539.8

# 盈不足術：置所出率，盈不足各居其下
盈不足乘積1 = 本錢1 * 不足
盈不足乘積2 = 本錢2 * 盈

# 令維乘所出率，并以為實
實 = abs(盈不足乘積1) + abs(盈不足乘積2)

# 并盈不足為法
法 = abs(不足) + abs(盈)

# 實如法而一
本錢 = Fraction(實, 法)

# 利 = 本錢 * 利率
利 = 本錢 * 利率

a = 本錢
b = 利
"""
Code error: both arguments should be Rational instances"""
