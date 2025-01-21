"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

"""
Suppose there is a cube of jade with a side length of 1 cun, weighing 7 liang, and a cube of stone with a side length of 1 cun, weighing 6 liang.
Now, there is a cube with a side length of 3 cun, containing both jade and stone, with a total weight of 11 jin.
Question: how much jade and stone are there, and what are their respective weights?

Answer: the jade is *a* cubic cun, weighing *b* jin; the stone is *c* cubic cun, weighing *d* jin.
"""

# Constants
jade_weight_per_cun3 = 7  # 7 liang per cubic cun
stone_weight_per_cun3 = 6  # 6 liang per cubic cun
total_volume = 3**3  # Total volume of the cube (in cubic cun)
total_weight = 11 * 16  # Total weight in liang (1 jin = 16 liang)

# Let the volume of jade be x cubic cun, and the volume of stone be y cubic cun
# x + y = total_volume
# 7x + 6y = total_weight

# Solve the system of equations
from fractions import Fraction

x = Fraction(total_weight - 6 * total_volume, jade_weight_per_cun3 - stone_weight_per_cun3)  # Volume of jade
y = total_volume - x  # Volume of stone

# Calculate weights
b = Fraction(x * jade_weight_per_cun3, 16)  # Weight of jade in jin
d = Fraction(y * stone_weight_per_cun3, 16)  # Weight of stone in jin

# Outputs
a = x  # Volume of jade in cubic cun
c = y  # Volume of stone in cubic cun

# Results
a, b, c, d
"""
"""
