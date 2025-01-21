"""
今有漆三得油四油四和漆五今有漆三斗欲令分以易油還自和餘漆問出漆得油和漆各幾何
術曰假令出漆九升不足六升令之出漆一斗二升有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰出漆 a斗 得油 b斗 和漆 c斗  d升 
"""

"""
Suppose there are 3 dou of lacquer that yield 4 dou of oil. 
4 dou of oil mixed with 5 dou of lacquer. 
Now there are 3 dou of lacquer, and it is desired to exchange lacquer for oil, and then mix the remaining lacquer with the oil.
Question: how much lacquer is exchanged, how much oil is obtained, and how much mixed lacquer remains?

The procedure says: Suppose 9 sheng of lacquer is exchanged, but it is insufficient by 6 sheng. 
Let it exchange 1 dou and 2 sheng, leaving 2 sheng remaining.

The procedure for surplus and deficiency says: Place the exchange rate, surplus, and deficiency below each other. 
Multiply the exchange rate by the surplus and deficiency, and add them together to form the dividend. 
Add the surplus and deficiency to form the divisor. 
Divide the dividend by the divisor. If there is a fraction, simplify it. 
The surplus and deficiency are used to adjust the result. 
For the exchanged material, place the exchange rate, subtract the smaller from the larger, and reduce the divisor and dividend proportionally. 
The dividend is the price of the material, and the divisor is the number of people.

Answer: *a* dou of lacquer is exchanged, *b* dou of oil is obtained, and *c* dou and *d* sheng of mixed lacquer remain.
"""

# 漆三得油四
漆率 = 3
油率 = 4

# 漆三斗
漆總量 = 3

# 假令出漆九升不足六升
盈 = 9
不足 = 6

# 置所出率
所出率 = 漆率

# 盈不足術計算
# 實 = 盈 * 所出率 + 不足 * 所出率
實 = 盈 * 所出率 + 不足 * 所出率

# 法 = 盈 + 不足
法 = 盈 + 不足

# 實如法而一
出漆 = Fraction(實, 法)

# 有分者通之
出漆 = 出漆.limit_denominator()

# 出漆轉換為斗和升
出漆斗 = int(出漆)  # 整數部分為斗
出漆升 = (出漆 - 出漆斗) * 10  # 小數部分轉換為升

# 得油
得油 = Fraction(出漆, 漆率) * 油率

# 和漆
剩餘漆 = 漆總量 - 出漆
和漆 = 剩餘漆 + 得油

# 和漆轉換為斗和升
和漆斗 = int(和漆)  # 整數部分為斗
和漆升 = (和漆 - 和漆斗) * 10  # 小數部分轉換為升

# 答案
a = 出漆
b = 得油
c = 和漆斗
d = 和漆升
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: 4
Variable 'd' has wrong value. Expected: 3/4, Actual: 0"""
