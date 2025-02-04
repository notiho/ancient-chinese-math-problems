"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
術曰：列絲一百八十八斤，以一十六两乘之、納十两，得三千一十八两；以五文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we will calculate the total cost of 188 jin and 10 liang of silk, where 1 liang costs 5 wen. Note that 1 jin equals 16 liang.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
cost_per_liang = 5  # wen
jin_to_liang = 16  # 1 jin = 16 liang

# Total weight in jin and liang
total_jin = 188
total_liang = 10

# Convert total weight to liang
total_liang_weight = total_jin * jin_to_liang + total_liang

# Calculate total cost in wen
total_cost_wen = total_liang_weight * cost_per_liang

# Convert wen to guan (1 guan = 1000 wen)
a = Fraction(total_cost_wen, 1000)

# Output the result
a
#----- content ends here -----


"""


The variable `a` will contain the total cost in guan as a fraction.
"""


"""
"""
