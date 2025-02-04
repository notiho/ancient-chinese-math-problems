"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

"""
Suppose there is a cubic piece of jade with a side length of 1 cun, weighing 7 liang, and a cubic piece of stone with a side length of 1 cun, weighing 6 liang. 
Now, there is a cube with a side length of 3 cun, containing both jade and stone, and the total weight is 11 jin.
Question: how much jade and stone are there, and what are their respective weights?

Answer: the jade is *a* cubic cun, weighing *b* jin. The stone is *c* cubic cun, weighing *d* jin.
"""

# Constants
jade_weight_per_cun3 = 7  # Jade weighs 7 liang per cubic cun
stone_weight_per_cun3 = 6  # Stone weighs 6 liang per cubic cun
total_volume = 3**3  # Total volume of the cube in cubic cun
total_weight = 11 * 16  # Total weight in liang (1 jin = 16 liang)

# Let the volume of jade be x (in cubic cun)
# Then the volume of stone is total_volume - x
# The total weight equation is:
# jade_weight_per_cun3 * x + stone_weight_per_cun3 * (total_volume - x) = total_weight

from fractions import Fraction

# Solve for x (volume of jade)
a = Fraction(total_weight - stone_weight_per_cun3 * total_volume, jade_weight_per_cun3 - stone_weight_per_cun3)

# Volume of stone
c = total_volume - a

# Weight of jade
b = jade_weight_per_cun3 * a / 16  # Convert to jin

# Weight of stone
d = stone_weight_per_cun3 * c / 16  # Convert to jin

# Results
a, b, c, d
"""
"""
