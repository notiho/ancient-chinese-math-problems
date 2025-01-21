"""
今有大器五小器一容三斛大器一小器五容二斛問大小器各容幾何
術曰假令大器五斗小器亦五斗盈一十斗令之大器五斗五升小器二斗五升不足二斗
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰大器容 a斛 小器容 b斛 
"""

"""
Suppose there is a large vessel and a small vessel. Five large vessels and one small vessel together hold 3 hu.
One large vessel and five small vessels together hold 2 hu.
Question: how much does each large vessel and small vessel hold?

The procedure says: Assume the large vessel holds 5 dou and the small vessel also holds 5 dou, making a total of 10 dou.
Adjust it such that the large vessel holds 5 dou 5 sheng and the small vessel holds 2 dou 5 sheng, leaving a shortage of 2 dou.

The procedure for surplus and shortage says: Place the rates of output (盈, surplus, and 不足, shortage) under their respective conditions.
Let them be multiplied by the rates of output and summed to form the dividend.
Sum the surplus and shortage to form the divisor.
Divide the dividend by the divisor, and if there is a remainder, simplify it.
The surplus and shortage are then adjusted to match the conditions.

Answer: The large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

from fractions import Fraction

# Conditions
# Five large vessels and one small vessel hold 3 hu
rate1_large = 5
rate1_small = 1
total1 = 3

# One large vessel and five small vessels hold 2 hu
rate2_large = 1
rate2_small = 5
total2 = 2

# 盈不足術
# Place the rates of output (盈 and 不足)
盈 = total1
不足 = total2

# Multiply the rates of output and sum to form the dividend (實)
實 = (rate1_small * 不足) + (rate2_small * 盈)

# Sum the surplus and shortage to form the divisor (法)
法 = (rate1_large * 不足) + (rate2_large * 盈)

# Divide the dividend by the divisor to find the value of one unit
unit_value = Fraction(實, 法)

# Calculate the capacity of the large vessel (a) and small vessel (b)
a = unit_value * rate1_large
b = unit_value * rate1_small
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 85/13
Variable 'b' has wrong value. Expected: 7/24, Actual: 17/13"""
