"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
答曰： a匹 。
"""

#----- content starts here -----
"""
Suppose there is 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where one bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be purchased?

Answer: *a* bolts.
"""

from fractions import Fraction

# 粟一十二萬八千九百四十斛九斗三合
total_millet = 128940  # Convert hu to dou (1 hu = 10 dou)
total_millet = total_millet * 10 + 9  # Add dou
total_millet = total_millet * 10 + 3  # Convert dou to sheng (1 dou = 10 sheng)

# 絹一匹，直粟三斛五斗七升
silk_cost = 3  # Convert hu to dou
silk_cost = silk_cost * 10 + 5  # Add dou
silk_cost = silk_cost * 10 + 7  # Convert dou to sheng

# Calculate how many bolts of silk can be purchased
a = total_millet // silk_cost  # Integer division for full bolts of silk

# Output the result
a = Fraction(a)
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 36117"""
