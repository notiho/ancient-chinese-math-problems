"""
今有漆三得油四油四和漆五今有漆三斗欲令分以易油還自和餘漆問出漆得油和漆各幾何
術曰假令出漆九升不足六升令之出漆一斗二升有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰出漆 a斗 得油 b斗 和漆 c斗  d升 
"""

"""
Suppose there are 3 dou of lacquer that yield 4 dou of oil. 
If 4 dou of oil are mixed with 5 dou of lacquer, then the resulting mixture is balanced.
Now, suppose there are 3 dou of lacquer, and it is desired to exchange it for oil, while returning the remaining lacquer after mixing.
Question: how much lacquer is exchanged, how much oil is obtained, and how much lacquer remains in the mixture?

The procedure says: Suppose 9 sheng of lacquer is exchanged, but it is insufficient by 6 sheng. 
Let it exchange 1 dou and 2 sheng, leaving 2 sheng remaining.

The procedure for surplus and deficiency says: Place the exchange rate, surplus, and deficiency, each under its respective term. 
Let them be multiplied by the exchange rate and summed to form the dividend. 
Sum the surplus and deficiency to form the divisor. 
Divide the dividend by the divisor, and if there is a remainder, simplify it. 
The surplus and deficiency are used together. 
For the exchanged material, place the exchange rate, subtract the smaller from the larger, and simplify the remainder with the divisor and dividend. 
The dividend becomes the material price, and the divisor becomes the number of people.

Answer: *a* dou of lacquer is exchanged, *b* dou of oil is obtained, and *c* dou and *d* sheng of lacquer remain in the mixture.
"""

# 漆三得油四
漆率 = 3
油率 = 4

# 油四和漆五
油和漆率 = 5

# 今有漆三斗
漆總量 = 3

# 假令出漆九升不足六升
盈 = 9  # 盈 (surplus)
不足 = 6  # 不足 (deficiency)

# 置所出率
所出率 = 漆率

# 盈不足各居其下，令維乘所出率并以為實
實 = (盈 * 所出率) + (不足 * 所出率)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一，有分者通之
出漆 = Fraction(實, 法)

# 出漆一斗二升有餘二升
a = 出漆  # 出漆 in dou

# 得油
b = Fraction(出漆 * 油率, 漆率)  # 得油 in dou

# 和漆餘量
剩餘漆 = 漆總量 - 出漆
c = int(剩餘漆)  # 和漆 in dou
d = int((剩餘漆 - c) * 10)  # 和漆 in sheng (1 dou = 10 sheng)
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: 0
Variable 'd' has wrong value. Expected: 3/4, Actual: 0"""
