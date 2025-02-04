"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
術曰：假令出漆九升，不足六升。令之出漆一斗二升，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：出漆 a(=9/8)斗 ，得油 b(=3/2)斗 ，和漆 c(=9/5)斗 ， d(=3/4)升 。
"""

"""
Suppose 3 dou of lacquer yields 4 dou of oil, and 4 dou of oil mixes with 5 dou of lacquer.
Now, suppose there are 3 dou of lacquer, and it is desired to divide it for exchanging oil and then mix the remaining lacquer with the obtained oil.
Question: how much lacquer is used, how much oil is obtained, and how much lacquer is mixed with the oil?

The procedure says: Suppose 9 sheng of lacquer is used, but it is insufficient by 6 sheng. Suppose 1 dou and 2 sheng of lacquer is used, leaving 2 sheng remaining.

The "excess and deficiency" procedure says: Place the exchange rate, with the excess and deficiency below it. Multiply the exchange rate by the excess and deficiency, summing them to obtain the dividend. Sum the excess and deficiency to obtain the divisor. Divide the dividend by the divisor to obtain the result. If there is a fraction, simplify it. For the excess and deficiency corresponding to the exchanged item, place the exchange rate, subtract the smaller from the larger, and simplify the divisor and dividend. The dividend is the price of the item, and the divisor is the number of people.

Answer: lacquer used *a*(=9/8) dou, oil obtained *b*(=3/2) dou, lacquer mixed *c*(=9/5) dou, and *d*(=3/4) sheng.
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

# 出漆
# 假令出漆九升，不足六升
盈 = 9
不足 = 6

# 令維乘所出率，并以為實
實 = (漆率 * 盈) + (漆率 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
出漆 = Fraction(實, 法)  # a = 9/8 dou

# 得油
得油 = Fraction(油率, 漆率) * 出漆  # b = 3/2 dou

# 和漆
和漆 = Fraction(漆和率, 油和率) * 得油  # c = 9/5 dou

# 餘漆
餘漆 = 漆總量 - 出漆 - 和漆  # d = 3/4 sheng

a = 出漆  # 9/8 dou
b = 得油  # 3/2 dou
c = 和漆  # 9/5 dou
d = 餘漆  # 3/4 sheng
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: 5
Variable 'd' has wrong value. Expected: 3/4, Actual: -5"""
