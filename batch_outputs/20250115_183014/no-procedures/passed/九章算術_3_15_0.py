"""
今有絲一斤，耗七兩。今有絲二十三斤五兩，問︰耗幾何？
荅曰： a兩 。
"""

"""
Suppose there is 1 jin of silk, and 7 liang is wasted during processing.
Now, there are 23 jin and 5 liang of silk. 
Question: how much is wasted?

Answer: *a* liang.
"""

from fractions import Fraction

# Define the waste ratio (7 liang wasted per 1 jin)
waste_per_jin = 7

# Total silk: 23 jin and 5 liang
total_silk_jin = 23
total_silk_liang = 5

# Convert everything to liang (1 jin = 16 liang)
total_silk_in_liang = total_silk_jin * 16 + total_silk_liang

# Calculate the waste
a = Fraction(waste_per_jin * total_silk_in_liang, 16)

# Output the result
a
"""
"""
