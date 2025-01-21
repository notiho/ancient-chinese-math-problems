"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
術曰：假令出漆九升，不足六升。令之出漆一斗二升，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：出漆 a(=9/8)斗 ，得油 b(=3/2)斗 ，和漆 c(=9/5)斗 ， d(=3/4)升 。
"""

"""
Suppose 3 dou of lacquer yields 4 dou of oil, and 4 dou of oil mixes with 5 dou of lacquer.
Now, suppose there are 3 dou of lacquer, and it is desired to divide it for exchanging oil and then mix the remaining lacquer with the oil.
Question: how much lacquer is used for exchange, how much oil is obtained, and how much lacquer is mixed with the oil?

The procedure says: Suppose 9 sheng of lacquer is used for exchange, but it is insufficient by 6 sheng. 
Adjust it to use 1 dou and 2 sheng, leaving 2 sheng remaining.

The procedure for surplus and deficiency says: Place the exchange rate, with surplus and deficiency below it. Multiply the exchange rate by the surplus and deficiency, summing them to obtain the dividend. Sum the surplus and deficiency to obtain the divisor. Divide the dividend by the divisor to find the result. If there is a fraction, simplify it. For surplus and deficiency that involve the same traded item, place the exchange rate, subtract the smaller from the larger, and simplify the dividend and divisor. The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: lacquer used for exchange is *a*(=9/8) dou, oil obtained is *b*(=3/2) dou, lacquer mixed with oil is *c*(=9/5) dou, and remaining lacquer is *d*(=3/4) sheng.
"""

# 漆三得油四
漆率 = 3
油率 = 4

# 油四和漆五
和油率 = 4
和漆率 = 5

# 今有漆三斗
漆總量 = 3

# 假令出漆九升，不足六升
盈 = 9
不足 = 6

# 置所出率，盈、不足各居其下
所出率 = 漆率 / 油率

# 令維乘所出率，并以為實
實 = 盈 * 所出率 + 不足 * 所出率

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
出漆 = Fraction(實, 法)  # a = 9/8 dou

# 得油
得油 = 出漆 * (油率 / 漆率)  # b = 3/2 dou

# 和漆
和漆 = 得油 * (和漆率 / 和油率)  # c = 9/5 dou

# 餘漆
餘漆 = 漆總量 - 出漆 - 和漆  # d = 3/4 dou

# Convert 餘漆 to sheng (1 dou = 10 sheng)
餘漆升 = 餘漆 * 10  # d = 3/4 sheng

a = 出漆  # 9/8 dou
b = 得油  # 3/2 dou
c = 和漆  # 9/5 dou
d = 餘漆升  # 3/4 sheng
"""
Code error: both arguments should be Rational instances"""
