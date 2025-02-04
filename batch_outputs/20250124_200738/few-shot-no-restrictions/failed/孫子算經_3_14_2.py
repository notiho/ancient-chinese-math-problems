"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 。
"""

#----- content starts here -----
"""
Suppose there is 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where 1 bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be purchased?

The procedure says: Place the total millet (128,940 hu, 9 dou, 3 sheng) as the dividend.
Take 3 hu, 5 dou, and 7 sheng as the divisor.
Divide the two, obtaining the number of bolts and the remainder.
Take the remainder and divide it again by the divisor to determine the fractional part.

Answer: *a* bolts of silk.
"""

from fractions import Fraction

# Define the units in terms of sheng (smallest unit)
# 1 hu = 10 dou, 1 dou = 10 sheng
hu_to_sheng = 10 * 10
dou_to_sheng = 10

# Total millet in sheng
total_millet = (128940 * hu_to_sheng) + (9 * dou_to_sheng) + 3

# Cost of 1 bolt of silk in sheng
cost_per_bolt = (3 * hu_to_sheng) + (5 * dou_to_sheng) + 7

# Perform the division
bolts = total_millet // cost_per_bolt  # Integer part (number of full bolts)
remainder = total_millet % cost_per_bolt  # Remaining millet

# Convert the remainder into fractional bolts
fractional_bolts = Fraction(remainder, cost_per_bolt)

# Total bolts of silk
a = bolts + fractional_bolts

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
