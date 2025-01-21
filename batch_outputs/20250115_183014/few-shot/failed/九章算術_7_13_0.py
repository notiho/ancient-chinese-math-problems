"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel hold 3 hu. 
One large vessel and five small vessels hold 2 hu. 
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose each large vessel holds 5 dou, and each small vessel also holds 5 dou, making a total of 10 dou. 
Adjust so that each large vessel holds 5 dou and 5 sheng, and each small vessel holds 2 dou and 5 sheng, resulting in a shortfall of 2 dou.

The procedure for surplus and shortfall says: Place the given rates, with surplus and shortfall below them. 
Multiply the rates by their respective surplus or shortfall, and add these to form the dividend. 
Add the surplus and shortfall to form the divisor. 
Divide the dividend by the divisor to find the value of one unit. If there are fractions, simplify them. 
For surplus and shortfall problems involving the same goods, place the rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend represents the price of the goods, and the divisor represents the number of people.

Answer: each large vessel holds *a* hu, and each small vessel holds *b* hu.
"""

from fractions import Fraction

# Given rates and results
大器率1 = 5  # Five large vessels
小器率1 = 1  # One small vessel
總量1 = 3    # Holds 3 hu

大器率2 = 1  # One large vessel
小器率2 = 5  # Five small vessels
總量2 = 2    # Holds 2 hu

# 盈不足術
# 盈、不足各居其下
盈 = (大器率1 * 總量2) - (大器率2 * 總量1)
不足 = (小器率2 * 總量1) - (小器率1 * 總量2)

# 并盈、不足為法
法 = 盈 + 不足

# 令維乘所出率，并以為實
實 = (大器率1 * 總量2 - 大器率2 * 總量1) + (小器率2 * 總量1 - 小器率1 * 總量2)

# 實如法而一
單位值 = Fraction(實, 法)

# 大器容
a = Fraction(總量1 - 小器率1 * 單位值, 大器率1)

# 小器容
b = 單位值

# Final answer
a = Fraction(a)
b = Fraction(b)
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 2/5
Variable 'b' has wrong value. Expected: 7/24, Actual: 1"""
