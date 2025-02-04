"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

#----- content starts here -----
"""
Suppose there is a cubic jade block with a side length of 1 cun, weighing 7 liang, and a cubic stone block with a side length of 1 cun, weighing 6 liang.
Now, there is a cubic stone block with a side length of 3 cun, containing jade inside, with a total weight of 11 jin.
Question: how much do the jade and stone weigh, and what are their respective volumes?

The procedure says: Suppose the entire block is jade, it exceeds the weight by 13 liang.
Suppose the entire block is stone, it is short by 14 liang.
The shortfall corresponds to the stone, and the excess corresponds to the jade.
Multiply each by the weight per cun³ to find the respective volumes and weights.

Answer: The jade is *a* cun³, weighing *b* jin. The stone is *c* cun³, weighing *d* jin.
"""

from fractions import Fraction

# Constants
jade_weight_per_cubic_cun = 7  # 7 liang per cun³
stone_weight_per_cubic_cun = 6  # 6 liang per cun³
total_weight = 11 * 16  # Convert total weight to liang (1 jin = 16 liang)
total_volume = 3**3  # Total volume in cun³

# Weight differences
excess_if_all_jade = 13  # liang
shortfall_if_all_stone = 14  # liang

# Calculate jade and stone volumes
jade_volume = Fraction(excess_if_all_jade, jade_weight_per_cubic_cun - stone_weight_per_cubic_cun)
stone_volume = total_volume - jade_volume

# Calculate jade and stone weights
jade_weight = jade_volume * jade_weight_per_cubic_cun
stone_weight = stone_volume * stone_weight_per_cubic_cun

# Convert weights back to jin
jade_weight_in_jin = jade_weight / 16
stone_weight_in_jin = stone_weight / 16

# Results
a = jade_volume
b = jade_weight_in_jin
c = stone_volume
d = stone_weight_in_jin

# Output
a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14, Actual: 13
Variable 'b' has wrong value. Expected: 49/8, Actual: 91/16
Variable 'c' has wrong value. Expected: 13, Actual: 14
Variable 'd' has wrong value. Expected: 39/8, Actual: 21/4"""
