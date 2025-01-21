"""
今有漆三得油四油四和漆五今有漆三斗欲令分以易油還自和餘漆問出漆得油和漆各幾何
術曰假令出漆九升不足六升令之出漆一斗二升有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰出漆 a斗 得油 b斗 和漆 c斗  d升 
"""

"""
Suppose there are 3 dou of lacquer that can yield 4 dou of oil. 
If 4 dou of oil are mixed with 5 dou of lacquer, and now there are 3 dou of lacquer, it is desired to exchange lacquer for oil and return the remainder of lacquer after mixing.

Question: How much lacquer is exchanged, how much oil is obtained, and how much lacquer remains mixed?

The procedure says:
Suppose 9 sheng of lacquer are exchanged, but it is insufficient by 6 sheng. 
Let it exchange 1 dou and 2 sheng, leaving 2 sheng remaining.

The procedure for surplus and deficiency says:
Place the rate of exchange, surplus, and deficiency, each below their respective terms. 
Let them be multiplied by the rate of exchange and summed to form the dividend. 
Sum the surplus and deficiency to form the divisor. 
Divide the dividend by the divisor, and if there is a fraction, simplify it. 
The surplus and deficiency are treated equally. 
For the exchanged item, place the rate of exchange, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend is the value of the item, and the divisor is the number of people.

Answer: Lacquer exchanged is *a* dou, oil obtained is *b* dou, and lacquer mixed is *c* dou and *d* sheng.
"""

# 漆三得油四
漆率 = 3
油率 = 4

# 油四和漆五
油和漆率 = 4 + 5

# 今有漆三斗
漆總量 = 3

# 假令出漆九升不足六升
盈 = 9
不足 = 6

# 置所出率
所出率 = 漆率

# 盈不足各居其下，令維乘所出率并以為實
實 = (盈 * 所出率) + (不足 * 所出率)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
出漆 = Fraction(實, 法)

# 有分者通之
出漆 = 出漆.limit_denominator()

# 盈不足相與同，其買物者置所出率以少減多餘以約法實
買物率 = 油率
少減多餘 = abs(盈 - 不足)

# 簡化法與實
法 = 法 // 少減多餘
實 = 實 // 少減多餘

# 實為物價，法為人數
出漆 = Fraction(實, 法)

# 計算得油
得油 = Fraction(出漆, 漆率) * 油率

# 計算和漆
和漆 = 漆總量 - 出漆

# 轉換為斗和升
a = 出漆
b = 得油
c = 和漆.numerator // 和漆.denominator
d = 和漆.numerator % 和漆.denominator
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: 0
Variable 'd' has wrong value. Expected: 3/4, Actual: 0"""
