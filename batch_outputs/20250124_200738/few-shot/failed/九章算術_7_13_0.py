"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a斛 ，小器容 b斛 。
"""

#----- content starts here -----
"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel hold 3 hu. 
One large vessel and five small vessels hold 2 hu. 
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou. 
Adjust it so that the large vessel holds 5 dou and 5 sheng, and the small vessel holds 2 dou and 5 sheng, leaving a shortfall of 2 dou.

The procedure for surplus and shortfall says: Place the given rates, with the surplus and shortfall below them respectively. 
Multiply the rates by the surplus and shortfall, and add them together to form the dividend. 
Add the surplus and shortfall to form the divisor. 
Divide the dividend by the divisor to find the value of one unit. If there is a remainder, simplify it. 
For surplus and shortfall problems involving the same goods, place the rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the goods, and the divisor becomes the number of people.

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

# 盈不足術
# Step 1: Place the rates and calculate surplus and shortfall
盈 = rate1_large * total2 - rate2_large * total1  # Surplus
不足 = rate2_small * total1 - rate1_small * total2  # Shortfall

# Step 2: Multiply rates by surplus and shortfall, and add them together to form the dividend
實 = rate1_large * 不足 + rate2_small * 盈

# Step 3: Add surplus and shortfall to form the divisor
法 = 盈 + 不足

# Step 4: Divide the dividend by the divisor to find the value of one unit
unit_value = Fraction(實, 法)

# Step 5: Calculate the capacity of the large and small vessels
a = Fraction(total1 - rate1_small * unit_value, rate1_large)  # Large vessel capacity
b = unit_value  # Small vessel capacity

# Final result
a, b  # a is the capacity of the large vessel, b is the capacity of the small vessel#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13/24, Actual: -2/5
Variable 'b' has wrong value. Expected: 7/24, Actual: 5"""
