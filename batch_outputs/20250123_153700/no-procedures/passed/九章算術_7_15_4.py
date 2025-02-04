"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

"""
Suppose there is a cubic piece of jade with a side length of 1 cun, weighing 7 liang; and a cubic piece of stone with a side length of 1 cun, weighing 6 liang.
Now, there is a cube with a side length of 3 cun, made of both jade and stone, weighing 11 jin in total.
Question: how much jade and stone are there, in volume and weight?

Answer: the jade is *a* cubic cun, weighing *b* jin; the stone is *c* cubic cun, weighing *d* jin.
"""

from fractions import Fraction

# Conversion factors
liang_per_jin = 16  # 1 jin = 16 liang

# Known weights
jade_weight_per_cubic_cun = 7  # 7 liang per cubic cun
stone_weight_per_cubic_cun = 6  # 6 liang per cubic cun

# Total volume and weight
total_volume = 3**3  # 3 cun x 3 cun x 3 cun = 27 cubic cun
total_weight = 11 * liang_per_jin  # 11 jin = 176 liang

# Let the volume of jade be x cubic cun, and the volume of stone be y cubic cun
# x + y = total_volume
# 7x + 6y = total_weight

# Solve for x (volume of jade) and y (volume of stone)
x = Fraction(total_weight - stone_weight_per_cubic_cun * total_volume,
             jade_weight_per_cubic_cun - stone_weight_per_cubic_cun)
y = total_volume - x

# Calculate weights
jade_weight = jade_weight_per_cubic_cun * x
stone_weight = stone_weight_per_cubic_cun * y

# Convert weights to jin
b = jade_weight / liang_per_jin
d = stone_weight / liang_per_jin

# Final results
a = x  # Volume of jade in cubic cun
c = y  # Volume of stone in cubic cun

# Output results
a, b, c, d
"""
"""
