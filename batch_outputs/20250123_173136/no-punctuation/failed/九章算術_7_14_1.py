"""
今有漆三得油四油四和漆五今有漆三斗欲令分以易油還自和餘漆問出漆得油和漆各幾何
術曰假令出漆九升不足六升令之出漆一斗二升有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰出漆 a斗 得油 b斗 和漆 c斗  d升 
"""

"""
Suppose there are 3 dou of lacquer that yield 4 dou of oil. 
If 4 dou of oil are mixed with 5 dou of lacquer, and now there are 3 dou of lacquer, it is desired to exchange lacquer for oil and then mix the remaining lacquer with the oil.
Question: how much lacquer is exchanged, how much oil is obtained, and how much lacquer remains mixed with the oil?

The procedure says: Suppose 9 sheng of lacquer are exchanged, but it is insufficient by 6 sheng. 
Then suppose 1 dou and 2 sheng of lacquer are exchanged, leaving 2 sheng remaining.

The procedure for surplus and deficit says: Place the exchange rate, surplus, and deficit below each other.
Multiply the exchange rate by the surplus and deficit, and sum them to form the dividend.
Sum the surplus and deficit to form the divisor.
Divide the dividend by the divisor, and if there is a remainder, simplify it.
If the surplus and deficit are equal, the exchange rate is used directly.
If the surplus and deficit differ, reduce the larger by the smaller and simplify the divisor and dividend.
The result is the price of the exchanged item, and the divisor is the number of people involved.

Answer: *a* dou of lacquer is exchanged, *b* dou of oil is obtained, and *c* dou and *d* sheng of lacquer remain mixed with the oil.
"""

# 漆三得油四
漆率 = 3
油率 = 4

# 油四和漆五
油和率 = 4
漆和率 = 5

# 今有漆三斗
漆總量 = 3

# 假令出漆九升不足六升
假出漆盈 = 9  # 盈 (surplus)
假出漆不足 = 6  # 不足 (deficit)

# 令維乘所出率并以為實
實 = (假出漆盈 * 漆率) + (假出漆不足 * 漆率)

# 并盈不足為法
法 = 假出漆盈 + 假出漆不足

# 實如法而一
出漆 = Fraction(實, 法)

# 有分者通之
出漆 = 出漆.limit_denominator()

# 出漆得油
得油 = Fraction(出漆 * 油率, 漆率)

# 和漆餘量
和漆餘量 = 漆總量 - 出漆

# 將和漆餘量分為斗和升
c = 和漆餘量.numerator // 和漆餘量.denominator  # 斗
d = (和漆餘量.numerator % 和漆餘量.denominator) * 10 // 和漆餘量.denominator  # 升

a = 出漆
b = 得油
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: 0
Variable 'd' has wrong value. Expected: 3/4, Actual: 0"""
