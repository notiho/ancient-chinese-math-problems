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
Suppose the large vessel holds 5 dou 5 sheng, and the small vessel holds 2 dou 5 sheng, falling short by 2 dou.

The "Excess and Deficiency" procedure says: Place the given rates, with the excess and deficiency below each. 
Multiply the rates by their respective excess or deficiency, and sum them to form the dividend. 
Sum the excess and deficiency to form the divisor. 
Divide the dividend by the divisor to find the result. If there is a remainder, adjust it. 
If the excess and deficiency correspond to the same object, place the rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: the large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

from fractions import Fraction

# Given data
rate_large_1 = 5  # Five large vessels
rate_small_1 = 1  # One small vessel
total_1 = 3       # Holds 3 hu

rate_large_2 = 1  # One large vessel
rate_small_2 = 5  # Five small vessels
total_2 = 2       # Holds 2 hu

# Excess and Deficiency method
# Step 1: Multiply rates by their respective totals
实1 = rate_large_1 * total_2
实2 = rate_large_2 * total_1

# Step 2: Subtract to find the dividend
实 = 实1 - 实2

# Step 3: Add rates to find the divisor
法 = rate_large_1 * rate_small_2 - rate_large_2 * rate_small_1

# Step 4: Divide 实 by 法 to find the value of one large vessel
a = Fraction(实, 法)

# Step 5: Substitute back to find the value of one small vessel
b = Fraction(total_1 - rate_large_1 * a, rate_small_1)

# Final answer
a = a  # Large vessel capacity in hu
b = b  # Small vessel capacity in hu
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 7/24
Variable 'b' has wrong value. Expected: 7/24, Actual: 37/24"""
