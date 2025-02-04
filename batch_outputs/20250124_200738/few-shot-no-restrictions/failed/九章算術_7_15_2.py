"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

#----- content starts here -----
"""
Suppose there is a cubic jade block with a side length of 1 cun, weighing 7 liang; and a cubic stone block with a side length of 1 cun, weighing 6 liang.
Now there is a cubic block with a side length of 3 cun, containing both jade and stone, with a total weight of 11 jin.
Question: how much jade and stone are there, and what are their respective weights?

The procedure says: 
If the entire block were jade, it would weigh 13 liang more than the actual weight.
If the entire block were stone, it would weigh 14 liang less than the actual weight.
The difference between the excess weight (jade) and the deficit weight (stone) determines the proportion of jade and stone.
Multiply the respective weights of 1 cun³ of jade and stone by their volumes to obtain the total weight.

Answer: the jade is *a* cun³, weighing *b* jin. The stone is *c* cun³, weighing *d* jin.
"""

from fractions import Fraction

# Known values
jade_weight_per_cubic_cun = 7  # 7 liang per cubic cun
stone_weight_per_cubic_cun = 6  # 6 liang per cubic cun
total_volume = 3**3  # 3 cun x 3 cun x 3 cun = 27 cubic cun
total_weight = 11 * 16  # 11 jin = 11 * 16 liang

# Excess and deficit weights
excess_if_all_jade = 13  # liang
deficit_if_all_stone = 14  # liang

# Total difference between jade and stone weights
weight_difference_per_cun = jade_weight_per_cubic_cun - stone_weight_per_cubic_cun

# Proportion of jade and stone
jade_volume = Fraction(deficit_if_all_stone, weight_difference_per_cun) * total_volume
stone_volume = total_volume - jade_volume

# Calculate weights
jade_weight = jade_volume * jade_weight_per_cubic_cun
stone_weight = stone_volume * stone_weight_per_cubic_cun

# Convert weights to jin (1 jin = 16 liang)
jade_weight_in_jin = jade_weight / 16
stone_weight_in_jin = stone_weight / 16

# Final answers
a = jade_volume
b = jade_weight_in_jin
c = stone_volume
d = stone_weight_in_jin

a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14, Actual: 378
Variable 'b' has wrong value. Expected: 49/8, Actual: 1323/8
Variable 'c' has wrong value. Expected: 13, Actual: -351
Variable 'd' has wrong value. Expected: 39/8, Actual: -1053/8"""
