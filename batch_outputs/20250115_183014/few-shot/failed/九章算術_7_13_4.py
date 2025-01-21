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
Adjust so that each large vessel holds 5 dou and 5 sheng, and each small vessel holds 2 dou and 5 sheng, leaving a deficit of 2 dou.

The procedure for surplus and deficit says: Place the coefficients (rates of vessels) with the surplus and deficit below them. 
Multiply the coefficients by the surplus and deficit, and sum them to obtain the dividend. 
Sum the surplus and deficit to obtain the divisor. 
Divide the dividend by the divisor to find the result. If there is a remainder, adjust it. 
For surplus and deficit problems involving the same items, place the coefficients, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend becomes the value of the item, and the divisor becomes the number of people.

Answer: each large vessel holds *a* hu, and each small vessel holds *b* hu.
"""

from fractions import Fraction

# Coefficients for the vessels
大器率_1 = 5  # Five large vessels
小器率_1 = 1  # One small vessel
總量_1 = 3    # Total 3 hu

大器率_2 = 1  # One large vessel
小器率_2 = 5  # Five small vessels
總量_2 = 2    # Total 2 hu

# 盈不足術
# Multiply the coefficients by their respective totals
實_1 = 大器率_1 * 總量_2  # 5 * 2
實_2 = 小器率_2 * 總量_1  # 5 * 3

# Sum the results to get the dividend
實 = 實_1 + 实_2


"""
Code error: name '实_2' is not defined"""
