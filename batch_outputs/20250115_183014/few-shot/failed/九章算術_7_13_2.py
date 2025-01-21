"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel hold 3 hu. 
One large vessel and five small vessels hold 2 hu. 
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou. 
Suppose the large vessel holds 5 dou 5 sheng, and the small vessel holds 2 dou 5 sheng, falling short by 2 dou.

The procedure for surplus and deficit says: Place the given rates, with surplus and deficit below each. 
Multiply the rates by their respective multipliers, and sum them to obtain the dividend. 
Sum the surplus and deficit to obtain the divisor. 
Divide the dividend by the divisor to obtain the result. If there is a remainder, adjust accordingly. 
For surplus and deficit problems involving the same items, place the rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend represents the price of the item, and the divisor represents the number of people.

Answer: the large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

from fractions import Fraction

# Given data
大器率_1 = 5  # First condition: 5 large vessels
小器率_1 = 1  # First condition: 1 small vessel
總量_1 = 3    # First condition: total 3 hu

大器率_2 = 1  # Second condition: 1 large vessel
小器率_2 = 5  # Second condition: 5 small vessels
總量_2 = 2    # Second condition: total 2 hu

# 盈不足術
# 置所出率，盈、不足各居其下
盈_1 = 總量_1
盈_2 = 總量_2

# 令維乘所出率，并以為實
實 = (大器率_1 * 盈_2) - (大器率_2 * 盈_1)

# 并盈、不足為法
法 = (小器率_1 * 盈_2) - (小器率_2 * 盈_1)

# 實如法而一
大器容量 = Fraction(實, 法)

# Calculate 小器容量
小器容量 = Fraction(盈_1 - 大器率_1 * 大器容量, 小器率_1)

# Final results
a = 大器容量
b = 小器容量
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: -7/13
Variable 'b' has wrong value. Expected: 7/24, Actual: 74/13"""
