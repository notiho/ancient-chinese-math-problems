"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 。
"""

#----- content starts here -----
"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where one bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be bought?

The procedure says: Place the total millet (128,940 hu, 9 dou, and 3 sheng) as the dividend.
Use 3 hu, 5 dou, and 7 sheng as the divisor.
Divide the dividend by the divisor to obtain the number of bolts, with a remainder.
If there is a remainder, divide it again by the divisor to refine the result.

Answer: *a* bolts of silk.
"""

from fractions import Fraction

# Define the units in terms of the smallest unit (sheng)
# 1 hu = 10 dou, 1 dou = 10 sheng
hu_to_sheng = 10 * 10
dou_to_sheng = 10

# Total millet: 128,940 hu, 9 dou, 3 sheng
total_millet = (128940 * hu_to_sheng) + (9 * dou_to_sheng) + 3

# Cost of 1 bolt of silk: 3 hu, 5 dou, 7 sheng
cost_per_bolt = (3 * hu_to_sheng) + (5 * dou_to_sheng) + 7

# Divide total millet by the cost per bolt
bolts = total_millet // cost_per_bolt  # Integer division to get the number of full bolts
remainder = total_millet % cost_per_bolt  # Remainder in sheng

# If there's a remainder, calculate the fractional part
fractional_bolt = Fraction(remainder, cost_per_bolt)

# Final result
a = bolts + fractional_bolt

a  # Number of bolts of silk#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
