"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel hold 3 hu. 
One large vessel and five small vessels hold 2 hu. 
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou. 
Adjust so that the large vessel holds 5 dou and 5 sheng, and the small vessel holds 2 dou and 5 sheng, resulting in a shortfall of 2 dou.

The procedure for surplus and shortfall says: Place the rates of output, with surplus and shortfall below them. 
Multiply the rates of output by their respective surplus or shortfall, and sum them to obtain the dividend. 
Sum the surplus and shortfall to obtain the divisor. 
Divide the dividend by the divisor to find the result. If there is a remainder, convert it into smaller units. 
If the surplus and shortfall involve the same type of goods, place the rates of output, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend becomes the value of the goods, and the divisor becomes the number of people.

Answer: the large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

from fractions import Fraction

# Given data
# Five large vessels and one small vessel hold 3 hu
rate1_large = 5
rate1_small = 1
total1 = 3

# One large vessel and five small vessels hold 2 hu
rate2_large = 1
rate2_small = 5
total2 = 2

# Surplus and shortfall
# Surplus: Multiply the rates of output by their respective totals
surplus = (rate1_large * total2) - (rate2_large * total1)
shortfall = (rate2_small * total1) - (rate1_small * total2)

# Sum the surplus and shortfall to obtain the divisor
divisor = surplus + shortfall

# Multiply the rates of output by their respective surplus or shortfall
dividend_large = (rate1_large * shortfall) + (rate2_large * surplus)
dividend_small = (rate1_small * shortfall) + (rate2_small * surplus)

# Divide the dividend by the divisor to find the result
a = Fraction(dividend_large, divisor)  # Large vessel capacity in hu
b = Fraction(dividend_small, divisor)  # Small vessel capacity in hu
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 18/5
Variable 'b' has wrong value. Expected: 7/24, Actual: 12/5"""
