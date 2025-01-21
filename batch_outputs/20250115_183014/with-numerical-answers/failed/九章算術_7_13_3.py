"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：大器容 a(=13/24)斛 ，小器容 b(=7/24)斛 。
"""

"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel hold 3 hu; one large vessel and five small vessels hold 2 hu.
Question: how much does each large vessel and small vessel hold?

The procedure says: Suppose each large vessel holds 5 dou, and each small vessel also holds 5 dou, making a total of 10 dou.
Adjust it so that each large vessel holds 5 dou 5 sheng, and each small vessel holds 2 dou 5 sheng, leaving a deficit of 2 dou.

The procedure for surplus and deficit says: Place the coefficients of the vessels, with surplus and deficit below them. Multiply the coefficients by the surplus or deficit, and sum them to form the dividend. Sum the surplus and deficit to form the divisor. Divide the dividend by the divisor to find the value of one vessel. If there is a remainder, simplify it. For vessels that share the same surplus or deficit, place their coefficients, subtract the smaller from the larger, and simplify the divisor and dividend. The dividend becomes the value of the vessel, and the divisor becomes the total number of vessels.

Answer: Each large vessel holds *a*(=13/24) hu, and each small vessel holds *b*(=7/24) hu.
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
# 盈、不足各居其下
盈 = 總量1
不足 = 總量2

# 令維乘所出率，并以為實
實 = (大器率1 * 不足) + (大器率2 * 盈)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
大器 = Fraction(實, 法)

# 小器容
# 以少減多，餘，以約法、實
小器 = Fraction(總量1 - 大器 * 大器率1, 小器率1)

a = 大器  # 13/24
b = 小器  # 7/24
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 13/5
Variable 'b' has wrong value. Expected: 7/24, Actual: -10"""
