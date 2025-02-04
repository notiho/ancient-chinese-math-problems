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

The procedure says: Suppose the entire block is jade, it would weigh 13 liang more than the actual weight.
Suppose the entire block is stone, it would weigh 14 liang less than the actual weight.
The difference is due to the proportions of jade and stone.
Use the weight per cubic cun of each material to calculate the respective volumes and weights.

Answer: The jade is *a* cun³, weighing *b* jin. The stone is *c* cun³, weighing *d* jin.
"""

from fractions import Fraction

# Given data
jade_weight_per_cubic_cun = 7  # 7 liang per cubic cun
stone_weight_per_cubic_cun = 6  # 6 liang per cubic cun
total_volume = 3**3  # 3 cun × 3 cun × 3 cun = 27 cun³
total_weight = 11 * 16  # 11 jin = 176 liang (1 jin = 16 liang)

# Weight differences
if_all_jade = total_weight + 13  # If all jade, 13 liang more
if_all_stone = total_weight - 14  # If all stone, 14 liang less

# Difference in weight per cubic cun between jade and stone
weight_difference_per_cun = jade_weight_per_cubic_cun - stone_weight_per_cubic_cun

# Calculate the volume of jade
jade_volume = Fraction(if_all_jade - total_weight, weight_difference_per_cun)

# Calculate the volume of stone
stone_volume = total_volume - jade_volume

# Calculate the weight of jade
jade_weight = jade_volume * jade_weight_per_cubic_cun

# Calculate the weight of stone
stone_weight = stone_volume * stone_weight_per_cubic_cun

# Convert weights to jin
jade_weight_in_jin = jade_weight / 16
stone_weight_in_jin = stone_weight / 16

# Results
a = jade_volume
b = jade_weight_in_jin
c = stone_volume
d = stone_weight_in_jin

a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14, Actual: 13
Variable 'b' has wrong value. Expected: 49/8, Actual: 91/16
Variable 'c' has wrong value. Expected: 13, Actual: 14
Variable 'd' has wrong value. Expected: 39/8, Actual: 21/4"""
