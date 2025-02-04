"""
今有絲一斤，耗七兩。今有絲二十三斤五兩，問︰耗幾何？
荅曰： a兩 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk, and it loses 7 liang during processing.  
Now, there are 23 jin and 5 liang of silk.  
Question: how much silk is lost in total?

Answer: *a* liang.
"""

from fractions import Fraction

# Define the loss per jin
loss_per_jin = 7  # liang

# Total silk: 23 jin and 5 liang
total_silk_in_liang = 23 * 16 + 5  # 1 jin = 16 liang

# Calculate the total loss
a = Fraction(total_silk_in_liang, 16) * loss_per_jin

# Convert back to liang
a = a#----- content ends here -----

"""
"""
