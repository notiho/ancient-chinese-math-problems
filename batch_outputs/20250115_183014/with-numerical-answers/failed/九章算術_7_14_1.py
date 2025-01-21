"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
術曰：假令出漆九升，不足六升。令之出漆一斗二升，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：出漆 a(=9/8)斗 ，得油 b(=3/2)斗 ，和漆 c(=9/5)斗 ， d(=3/4)升 。
"""

"""
Suppose 3 dou of lacquer yields 4 dou of oil, and 4 dou of oil mixes with 5 dou of lacquer.
Now, given 3 dou of lacquer, it is desired to exchange it for oil and then mix the remaining lacquer with the oil.
Question: how much lacquer is used, how much oil is obtained, and how much lacquer is mixed?

The procedure says: Suppose 9 sheng of lacquer is used, but it is insufficient by 6 sheng. 
Adjust it to use 1 dou and 2 sheng, leaving 2 sheng remaining.

The "excess and deficiency" procedure says: Place the rate of exchange, with the excess and deficiency below it.
Multiply the rate of exchange by the excess and deficiency, summing them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
For the excess and deficiency that correspond to the same exchanged item, place the rate of exchange, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: the lacquer used is *a*(=9/8) dou, the oil obtained is *b*(=3/2) dou, and the lacquer mixed is *c*(=9/5) dou and *d*(=3/4) sheng.
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
假出漆 = Fraction(9, 10)  # 9升 = 9/10斗
不足 = Fraction(6, 10)  # 6升 = 6/10斗

# 盈不足術曰：置所出率，盈、不足各居其下
盈 = 假出漆
不足 = Fraction(漆率, 油率) - 假出漆
"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'"""
