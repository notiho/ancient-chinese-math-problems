"""
今有絲一斤，耗七兩。今有絲二十三斤五兩，問︰耗幾何？
荅曰： a兩 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk, and it loses 7 liang during processing.  
Now there are 23 jin and 5 liang of silk.  
Question: how much is lost in total?

Answer: *a* liang.
"""

# 1 jin = 16 liang
jin_to_liang = 16

# Loss per jin
loss_per_jin = 7

# Total silk in liang
total_silk_liang = 23 * jin_to_liang + 5

# Calculate the total loss
a = Fraction(total_silk_liang, jin_to_liang) * loss_per_jin

a#----- content ends here -----

"""
"""
