"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

#----- content starts here -----
"""
Suppose there is a jade cube of 1 cun on each side, weighing 7 liang; and a stone cube of 1 cun on each side, weighing 6 liang.
Now there is a cube of stone with a side length of 3 cun, containing some jade inside, and the total weight is 11 jin.
Question: how much jade and stone are there, and what are their respective weights?

The procedure says: Suppose it is all jade, then it exceeds by 13 liang.
Suppose it is all stone, then it falls short by 14 liang.
The shortfall corresponds to jade, and the excess corresponds to stone.
Multiply each by the weight per cun³ to find the respective volumes and weights of jade and stone.

Answer: the jade is *a* cun³, weighing *b* jin; the stone is *c* cun³, weighing *d* jin.
"""

from fractions import Fraction

# Constants
jade_weight_per_cubic_cun = 7  # 7 liang per cun³
stone_weight_per_cubic_cun = 6  # 6 liang per cun³
total_volume = 3**3  # 3 cun³ cube
total_weight = 11 * 16  # 11 jin = 176 liang

# Excess and shortfall
excess_if_all_jade = total_weight - (total_volume * jade_weight_per_cubic_cun)  # 13 liang
shortfall_if_all_stone = (total_volume * stone_weight_per_cubic_cun) - total_weight  # 14 liang

# Solve for jade and stone volumes
jade_volume = Fraction(shortfall_if_all_stone, excess_if_all_jade + shortfall_if_all_stone) * total_volume
stone_volume = total_volume - jade_volume

# Calculate weights
jade_weight = jade_volume * jade_weight_per_cubic_cun
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
"""
