"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel hold 3 hu; one large vessel and five small vessels hold 2 hu.
Question: how much does each large and small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou.
Suppose the large vessel holds 5 dou 5 sheng, and the small vessel holds 2 dou 5 sheng, resulting in a shortfall of 2 dou.

The procedure for surplus and shortfall says: Place the coefficients of the vessels, with the surplus and shortfall below each. Multiply the coefficients by their respective surplus or shortfall, and sum them to form the dividend. Sum the surplus and shortfall to form the divisor. Divide the dividend by the divisor to find the value of one vessel. If there is a remainder, adjust it. For the surplus and shortfall to match the same item, place the coefficients, subtract the smaller from the larger, and simplify the divisor and dividend. The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: the large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

from fractions import Fraction

# Coefficients for the vessels
大器率1 = 5  # Coefficient for large vessels in the first equation
小器率1 = 1  # Coefficient for small vessels in the first equation
大器率2 = 1  # Coefficient for large vessels in the second equation
小器率2 = 5  # Coefficient for small vessels in the second equation

# Surplus and shortfall
盈 = 3  # Total volume for the first equation (surplus)
不足 = 2  # Total volume for the second equation (shortfall)

# Multiply coefficients by their respective surplus or shortfall
實 = (大器率1 * 盈) + (小器率2 * 不足)

# Sum the surplus and shortfall to form the divisor
法 = 盈 + 不足

# Divide the dividend by the divisor to find the value of one large vessel
大器 = Fraction(實, 法)

# Calculate the value of one small vessel using the first equation
小器 = Fraction(盈 - 大器 * 大器率1, 小器率1)

# Assign the results
a = 大器
b = 小器
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 5
Variable 'b' has wrong value. Expected: 7/24, Actual: -22"""
