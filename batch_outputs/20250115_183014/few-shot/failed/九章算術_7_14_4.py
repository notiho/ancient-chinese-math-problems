"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
術曰：假令出漆九升，不足六升。令之出漆一斗二升，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：出漆 a斗 ，得油 b斗 ，和漆 c斗 ， d升 。
"""

"""
Suppose 3 dou of lacquer yields 4 dou of oil, and 4 dou of oil mixes with 5 dou of lacquer.
Now, there are 3 dou of lacquer, and it is desired to exchange lacquer for oil, and then mix the remaining lacquer with the obtained oil.
Question: how much lacquer is exchanged, how much oil is obtained, and how much lacquer is mixed with the oil?

The procedure says: Suppose 9 sheng of lacquer is exchanged, but it is insufficient by 6 sheng. 
Let it be 1 dou and 2 sheng of lacquer exchanged, with 2 sheng remaining.
The procedure for surplus and deficiency says: Place the rate of exchange, with surplus and deficiency below it.
Multiply the rate of exchange by itself, and add them together to form the dividend.
Add the surplus and deficiency to form the divisor.
Divide the dividend by the divisor to find the result.
If there is a fraction, simplify it.
For surplus and deficiency, when dealing with the same traded item, place the rate of exchange, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* dou of lacquer is exchanged, *b* dou of oil is obtained, and *c* dou and *d* sheng of lacquer are mixed with the oil.
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

# 假令出漆九升，不足六升
盈 = 9 / 10  # 9升 = 9/10斗
不足 = 6 / 10  # 6升 = 6/10斗

# 令維乘所出率，并以為實
實 = 漆率 * 漆率 + 盈 + 不足

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
出漆 = Fraction(實, 法)

# 得油
得油 = (出漆 * 油率) / 漆率

# 和漆
和漆 = 漆總量 - 出漆

# 將和漆轉為斗和升
和漆斗 = 和漆.numerator // 和漆.denominator
和漆升 = (和漆 - 和漆斗) * 10

# 答案
a = 出漆
b = 得油
c = 和漆斗
d = 和漆升
"""
Code error: both arguments should be Rational instances"""
