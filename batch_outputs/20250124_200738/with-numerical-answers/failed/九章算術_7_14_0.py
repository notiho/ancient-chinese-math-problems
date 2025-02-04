"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
術曰：假令出漆九升，不足六升。令之出漆一斗二升，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：出漆 a(=9/8)斗 ，得油 b(=3/2)斗 ，和漆 c(=9/5)斗 ， d(=3/4)升 。
"""

#----- content starts here -----
"""
Suppose 3 dou of lacquer yield 4 dou of oil, and 4 dou of oil mix with 5 dou of lacquer.
Now, suppose there are 3 dou of lacquer, and it is desired to divide it to exchange for oil, and then mix the remaining lacquer with the oil.
Question: how much lacquer is used for exchange, how much oil is obtained, and how much lacquer is mixed with the oil?

The procedure says: Suppose 9 sheng of lacquer is used, but it is insufficient by 6 sheng. Let it be 1 dou and 2 sheng, with 2 sheng remaining.
The procedure for surplus and deficiency says: Place the exchange rate, with surplus and deficiency each below it.
Multiply the exchange rate by the surplus and deficiency, and add them to form the dividend.
Add the surplus and deficiency to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
For surplus and deficiency that correspond to the same exchanged item, place the exchange rate, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: lacquer used for exchange *a*(=9/8) dou, oil obtained *b*(=3/2) dou, lacquer mixed with oil *c*(=9/5) dou and *d*(=3/4) sheng.
"""

from fractions import Fraction

# 漆三得油四
漆率 = 3
油率 = 4

# 油四和漆五
和油率 = 4
和漆率 = 5

# 今有漆三斗
總漆 = 3

# 假令出漆九升，不足六升
盈 = Fraction(9, 10)  # 9 sheng = 9/10 dou
不足 = Fraction(6, 10)  # 6 sheng = 6/10 dou

# 置所出率，盈、不足各居其下
所出率 = Fraction(漆率, 油率)

# 令維乘所出率，并以為實
實 = 盈 * 所出率 + 不足 * 所出率

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
出漆 = 實 / 法  # a = 9/8 dou

# 得油
得油 = 出漆 * Fraction(油率, 漆率)  # b = 3/2 dou

# 和漆
和漆 = 總漆 - 出漆  # 漆剩下的部分
和漆 = 和漆 * Fraction(和漆率, 和油率)  # c = 9/5 dou

# 和漆餘量
和漆餘 = 和漆 - int(和漆)  # d = 3/4 sheng#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'"""
