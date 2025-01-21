"""
今有漆三得油四油四和漆五今有漆三斗欲令分以易油還自和餘漆問出漆得油和漆各幾何
術曰假令出漆九升不足六升令之出漆一斗二升有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰出漆 a斗 得油 b斗 和漆 c斗  d升 
"""

"""
Suppose there are 3 dou of lacquer that yield 4 dou of oil. 
4 dou of oil mixed with 5 dou of lacquer creates a mixture.
Now, there are 3 dou of lacquer, and it is desired to exchange lacquer for oil and then mix the remaining lacquer with the oil.
Question: how much lacquer is exchanged, how much oil is obtained, and how much lacquer is left in the mixture?

The procedure says: Suppose 9 sheng of lacquer are exchanged, but it is insufficient by 6 sheng. 
Let it be 1 dou and 2 sheng of lacquer exchanged, with 2 sheng remaining.

The procedure for surplus and deficiency says: Place the exchange rate, surplus, and deficiency below each other. 
Let them be multiplied by the exchange rate and summed to form the dividend. 
Sum the surplus and deficiency to form the divisor. 
Divide the dividend by the divisor to obtain the result. 
If there are fractions, simplify them. 
The surplus and deficiency are treated in the same way. 
For the exchanged goods, place the exchange rate, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend becomes the price of the goods, and the divisor becomes the number of people.

Answer: *a* dou of lacquer is exchanged, *b* dou of oil is obtained, and the mixture contains *c* dou and *d* sheng of lacquer.
"""

from fractions import Fraction

# 漆三得油四
漆率 = 3
油率 = 4

# 油四和漆五
油和率 = 4
漆和率 = 5

# 今有漆三斗
漆總量 = 3

# 假令出漆九升不足六升
盈 = 9
不足 = 6

# 置所出率
所出率 = 漆率

# 盈不足術計算
實 = 所出率 * 盈 + 所出率 * 不足
法 = 盈 + 不足
出漆 = Fraction(實, 法)

# 簡化出漆
出漆斗 = 出漆 // 10  # 每斗10升
出漆升 = 出漆 % 10

# 得油
得油 = Fraction(出漆, 漆率) * 油率

# 剩餘漆
剩餘漆 = 漆總量 - 出漆

# 和漆
和漆 = 剩餘漆

# 和油
和油 = 得油

# 答案
a = 出漆斗 + Fraction(出漆升, 10)  # 出漆 a斗
b = 得油  # 得油 b斗
c = 和漆 // 1  # 和漆 c斗
d = (和漆 % 1) * 10  # 和漆 d升
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3/10
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: 0
Variable 'd' has wrong value. Expected: 3/4, Actual: 0"""
