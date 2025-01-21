"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：大器容 a(=13/24)斛 ，小器容 b(=7/24)斛 。
"""

"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel hold 3 hu. One large vessel and five small vessels hold 2 hu.
Question: how much does each large and small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou. Suppose the large vessel holds 5 dou and 5 sheng, and the small vessel holds 2 dou and 5 sheng, making a deficit of 2 dou.

The procedure for surplus and deficit says: Place the given ratios, with the surplus and deficit below them. Multiply the ratios by their respective surplus or deficit, and sum them to obtain the dividend. Add the surplus and deficit to obtain the divisor. Divide the dividend by the divisor to find the value of one unit. If there is a fraction, simplify it. For surplus and deficit problems involving the same goods, place the ratios, subtract the smaller from the larger, and simplify the divisor and dividend. The dividend becomes the price of the goods, and the divisor becomes the number of people.

Answer: The large vessel holds *a*(=13/24) hu, and the small vessel holds *b*(=7/24) hu.
"""

from fractions import Fraction

# 大器五、小器一容三斛
大器率1 = 5
小器率1 = 1
總量1 = 3

# 大器一、小器五容二斛
大器率2 = 1
小器率2 = 5
總量2 = 2

# 盈不足術
# 置所出率，盈、不足各居其下
盈 = 總量1
不足 = 總量2

# 令維乘所出率，并以為實
實 = (大器率1 * 總量1) + (大器率2 * 總量2)

# 并盈、不足為法
法 = (大器率1 + 小器率2)

# 實如法而一
單位值 = Fraction(實, 法)

# 大器容
a = Fraction(大器率1 * 單位值, 總量1)  

# Small
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 17/6
Missing variable in output: 'b'"""
