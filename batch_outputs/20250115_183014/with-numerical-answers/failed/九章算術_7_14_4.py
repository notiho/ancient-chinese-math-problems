"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
術曰：假令出漆九升，不足六升。令之出漆一斗二升，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：出漆 a(=9/8)斗 ，得油 b(=3/2)斗 ，和漆 c(=9/5)斗 ， d(=3/4)升 。
"""

"""
Suppose 3 dou of lacquer yield 4 dou of oil, and 4 dou of oil mix with 5 dou of lacquer. 
Now, there are 3 dou of lacquer, and it is desired to divide it to exchange for oil and then mix the remaining lacquer with the oil.
Question: how much lacquer is used for exchange, how much oil is obtained, and how much lacquer is mixed with the oil?

The procedure says: Suppose 9 sheng of lacquer is exchanged, but it is insufficient by 6 sheng. 
Let it be 1 dou and 2 sheng, with 2 sheng remaining.

The "excess and deficiency" procedure says: Place the exchange rate, with the excess and deficiency below it. 
Multiply the exchange rate by itself and add them together to form the dividend. 
Add the excess and deficiency together to form the divisor. 
Divide the dividend by the divisor to find the result. 
If there is a fraction, simplify it. 
For the excess and deficiency related to the exchanged item, place the exchange rate, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: lacquer exchanged *a*(=9/8) dou, oil obtained *b*(=3/2) dou, lacquer mixed *c*(=9/5) dou, and *d*(=3/4) sheng.
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

# 出漆率
出漆率 = Fraction(油率, 漆率)  # 4/3

# 假令出漆九升，不足六升
盈 = 9
不足 = 6

# 盈不足術曰：置所出率，盈、不足各居其下
盈不足法 = 盈 + 不足  # 9 + 6 = 15

# 令維乘所出率，并以為實
盈不足實 = (盈 * 出漆率) + (不足 * 出漆率)  # (9 * 4/3) + (6 * 4/3)

# 并盈、不足為法
盈不足法 = 盈 + 不足  # 15

# 實如法而一
出漆 = Fraction(盈不足實, 盈不足法)  # (9 * 4/3 + 6 * 4/3) / 15 = 9/8 dou

# 得油
得油 = 出漆 * 出漆率  # 9/8 * 4/3 = 3/2 dou

# 和漆
和漆 = 得油 * Fraction(漆和率, 油和率)  # 3/2 * 5/4 = 15/8 dou

# 餘漆
餘漆 = 漆總量 - 出漆  # 3 - 9/8 = 15/8 dou

# Convert 和漆 into dou and sheng
和漆斗 = 和漆.numerator // 和漆.denominator  # Integer part in dou
和漆升 = 和漆 - 和漆斗  # Fractional part in sheng

a = 出漆  # 9/8 dou
b = 得油  # 3/2 dou
c = 和漆  # 9/5 dou
d = 和漆升  # 3/4 sheng
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 4/3
Variable 'b' has wrong value. Expected: 3/2, Actual: 16/9
Variable 'c' has wrong value. Expected: 9/5, Actual: 20/9
Variable 'd' has wrong value. Expected: 3/4, Actual: 2/9"""
