"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

#----- content starts here -----
"""
Suppose there is a cube of jade with a side length of 1 cun, weighing 7 liang; and a cube of stone with a side length of 1 cun, weighing 6 liang.
Now, there is a cube of stone with a side length of 3 cun, containing some jade inside, with a total weight of 11 jin.
Question: how much jade and stone are there, and what are their respective weights?

The procedure says: Assume the entire cube is jade, and it exceeds the weight by 13 liang.
Assume the entire cube is stone, and it falls short by 14 liang.
The shortfall is jade, and the excess is stone.
Multiply each by the weight per cun^3 to determine the respective weights of jade and stone.

Answer: The jade is *a* cun^3, weighing *b* jin. The stone is *c* cun^3, weighing *d* jin.
"""

from fractions import Fraction

# Constants
jade_density = 7  # Jade weighs 7 liang per cun^3
stone_density = 6  # Stone weighs 6 liang per cun^3
total_volume = 3**3  # Total volume of the cube (3 cun)^3
total_weight = 11 * 16  # Total weight in liang (1 jin = 16 liang)

# Step 1: Assume the entire cube is jade
jade_weight_excess = jade_density * total_volume - total_weight  # Excess weight in liang

# Step 2: Assume the entire cube is stone
stone_weight_shortfall = total_weight - stone_density * total_volume  # Shortfall in liang

# Step 3: Solve for jade and stone volumes
jade_volume = Fraction(stone_weight_shortfall, jade_weight_excess + stone_weight_shortfall) * total_volume
stone_volume = total_volume - jade_volume

# Step 4: Calculate weights
jade_weight = jade_volume * jade_density
stone_weight = stone_volume * stone_density

# Convert weights to jin and liang
jade_weight_jin = jade_weight // 16
jade_weight_liang = jade_weight % 16

stone_weight_jin = stone_weight // 16
stone_weight_liang = stone_weight % 16

# Results
a = jade_volume
b = Fraction(jade_weight, 16)  # Weight of jade in jin
c = stone_volume
d = Fraction(stone_weight, 16)  # Weight of stone in jin

# Outputs
a, b, c, d#----- content ends here -----

"""
"""
