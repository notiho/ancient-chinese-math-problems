"""
今有漆三得油四油四和漆五今有漆三斗欲令分以易油還自和餘漆問出漆得油和漆各幾何
術曰假令出漆九升不足六升令之出漆一斗二升有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰出漆 a斗 得油 b斗 和漆 c斗  d升 
"""

"""
Suppose there are 3 dou of lacquer that yield 4 dou of oil. 
If 4 dou of oil are mixed with 5 dou of lacquer, then the mixture becomes uniform.
Now, suppose there are 3 dou of lacquer. It is desired to exchange lacquer for oil and then mix the remaining lacquer with the oil.
Question: how much lacquer is exchanged, how much oil is obtained, and how much lacquer remains mixed with the oil?

The procedure says: Suppose 9 sheng of lacquer are exchanged, but it is insufficient by 6 sheng. 
Then, suppose 1 dou and 2 sheng of lacquer are exchanged, leaving 2 sheng remaining.

The procedure for surplus and deficiency says: Place the exchange rate and the surplus and deficiency below it. 
Let them be multiplied by the exchange rate and summed to form the dividend. 
Sum the surplus and deficiency to form the divisor. 
Divide the dividend by the divisor. If there is a remainder, simplify it. 
The surplus and deficiency are treated equally. 
For the exchanged item, place the exchange rate, subtract the smaller from the larger, and reduce the divisor and dividend accordingly. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* dou of lacquer are exchanged, *b* dou of oil are obtained, and *c* dou and *d* sheng of lacquer remain mixed with the oil.
"""

# Initial values
漆率 = 3  # 漆三
油率 = 4  # 得油四
混合漆率 = 5  # 和漆五
混合油率 = 4  # 油四
漆總量 = 3  # 漆三斗

# Exchange rate: 漆三得油四
漆得油率 = Fraction(油率, 漆率)

# Mixed ratio: 油四和漆五
混合比例 = Fraction(混合油率, 混合漆率)

# 盈不足術
# 假令出漆九升不足六升
盈 = 9  # 盈
不足 = 6  # 不足

# 令之出漆一斗二升有餘二升
假出漆 = Fraction(1, 1) + Fraction(2, 10)  # 1斗2升 = 1.2斗
假餘漆 = Fraction(2, 10)  # 2升 = 0.2斗

# 盈不足術計算
實 = (盈 * 漆得油率) + (不足 * 漆得油率)  # Dividend
法 = 盈 + 不足  # Divisor
出漆 = Fraction(實, 法)  # 漆 exchanged

# 得油
得油 = 出漆 * 漆得油率

# 餘漆
餘漆 = 漆總量 - 出漆

# 和漆
和漆 = 餘漆

# Convert 和漆 into dou and sheng
和漆斗 = int(和漆)  # Integer part in dou
和漆升 = (和漆 - 和漆斗) * 10  # Remaining part in sheng

# Final results
a = 出漆
b = 得油
c = 和漆斗
d = 和漆升
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 4/3
Variable 'b' has wrong value. Expected: 3/2, Actual: 16/9
Variable 'c' has wrong value. Expected: 9/5, Actual: 1
Variable 'd' has wrong value. Expected: 3/4, Actual: 20/3"""
