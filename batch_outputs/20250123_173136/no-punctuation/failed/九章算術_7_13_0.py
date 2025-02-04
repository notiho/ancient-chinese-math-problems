"""
今有大器五小器一容三斛大器一小器五容二斛問大小器各容幾何
術曰假令大器五斗小器亦五斗盈一十斗令之大器五斗五升小器二斗五升不足二斗
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰大器容 a斛 小器容 b斛 
"""

"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel together hold 3 hu.
One large vessel and five small vessels together hold 2 hu.
Question: how much does each large vessel and each small vessel hold?

The procedure says: Assume that each large vessel holds 5 dou, and each small vessel also holds 5 dou, making a total of 10 dou.
Adjust this by letting each large vessel hold 5 dou and 5 sheng, and each small vessel hold 2 dou and 5 sheng, which results in a shortfall of 2 dou.

The procedure for surplus and shortfall says: Place the rates of surplus and shortfall under their respective conditions.
Multiply the rates of surplus and shortfall by their respective coefficients, and sum them to form the dividend.
Sum the surplus and shortfall to form the divisor.
Divide the dividend by the divisor to find the value of one unit. If there is a remainder, adjust it proportionally.
For the surplus and shortfall, adjust them to match the given conditions.

Answer: Each large vessel holds *a* hu, and each small vessel holds *b* hu.
"""

from fractions import Fraction

# Given data
大器數 = 5  # Number of large vessels
小器數 = 1  # Number of small vessels
總量1 = 3  # Total volume in the first condition (3 hu)

大器數2 = 1  # Number of large vessels in the second condition
小器數2 = 5  # Number of small vessels in the second condition
總量2 = 2  # Total volume in the second condition (2 hu)

# Surplus and shortfall rates
盈率 = 小器數2  # Surplus rate (5 small vessels)
不足率 = 大器數  # Shortfall rate (5 large vessels)

# Surplus and shortfall totals
盈總 = 總量2  # Surplus total (2 hu)
不足總 = 總量1  # Shortfall total (3 hu)

# Calculate the divisor (sum of surplus and shortfall rates)
法 = 盈率 + 不足率

# Calculate the dividend (sum of surplus and shortfall totals weighted by their rates)
實 = (盈率 * 不足總) + (不足率 * 盈總)

# Calculate the value of one unit
單位值 = Fraction(實, 法)

# Calculate the volume of each large vessel and small vessel
a = Fraction(盈總, 盈率) * 單位值
b = Fraction不足
"""
Code error: name 'Fraction不足' is not defined"""
