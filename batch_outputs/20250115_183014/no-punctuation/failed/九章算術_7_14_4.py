"""
今有漆三得油四油四和漆五今有漆三斗欲令分以易油還自和餘漆問出漆得油和漆各幾何
術曰假令出漆九升不足六升令之出漆一斗二升有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰出漆 a斗 得油 b斗 和漆 c斗  d升 
"""

"""
Suppose there are 3 dou of lacquer that yield 4 dou of oil. 
4 dou of oil mixed with 5 dou of lacquer creates a mixture.
Now, suppose there are 3 dou of lacquer, and it is desired to exchange lacquer for oil, then mix the remaining lacquer with the oil.
Question: how much lacquer is exchanged for oil, how much oil is obtained, and how much mixed lacquer remains?

The procedure says: Suppose 9 sheng of lacquer is exchanged, but it is insufficient by 6 sheng. 
Let it exchange 1 dou and 2 sheng, leaving 2 sheng remaining.

The "Excess and Deficiency" procedure says: Place the exchange rate, and place the excess and deficiency below it. 
Let them each multiply the exchange rate, and sum them to form the dividend. 
Sum the excess and deficiency to form the divisor. 
Divide the dividend by the divisor to obtain the result. 
If there is a fraction, simplify it. 
If the excess and deficiency are the same, the result is consistent with the exchange rate. 
For the exchanged item, place the exchange rate, subtract the smaller from the larger, and reduce the remainder with the divisor and dividend. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* dou of lacquer is exchanged, *b* dou of oil is obtained, and *c* dou and *d* sheng of mixed lacquer remain.
"""

# Initial data
漆率 = 3  # 漆三
油率 = 4  # 得油四
混合漆率 = 5  # 和漆五
初始漆 = 3  # 漆三斗

# Exchange rate: 3 dou of lacquer yields 4 dou of oil
交換率 = Fraction(油率, 漆率)

# Suppose 9 sheng of lacquer is exchanged, but it is insufficient by 6 sheng
盈 = 9  # 盈
不足 = 6  # 不足

# Let them each multiply the exchange rate and sum them to form the dividend
實 = (盈 * 交換率) + (不足 * 交換率)

# Sum the excess and deficiency to form the divisor
法 = 盈 + 不足

# Divide the dividend by the divisor to obtain the result
出漆 = Fraction(實, 法)

# Convert to dou and sheng
出漆斗 = 出漆.numerator // 出漆.denominator  # Whole dou
出漆升 = (出漆.numerator % 出漆.denominator) * 10 // 出漆.denominator  # Remaining sheng

# Calculate the amount of oil obtained
得油 = 出漆 * 交換率

# Calculate the remaining lacquer
餘漆 = 初始漆 - 出漆

# Calculate the mixed lacquer (remaining lacquer + obtained oil)
和漆 = 餘漆 + 得油

# Convert mixed lacquer to dou and sheng
和漆斗 = 和漆.numerator // 和漆.denominator  # Whole dou
和漆升 = (和漆.numerator % 和漆.denominator) * 10 // 和漆.denominator  # Remaining sheng

# Final results
a = 出漆
b = 得油
c = 和漆斗
d = 和漆升
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 4/3
Variable 'b' has wrong value. Expected: 3/2, Actual: 16/9
Variable 'c' has wrong value. Expected: 9/5, Actual: 3
Variable 'd' has wrong value. Expected: 3/4, Actual: 4"""
