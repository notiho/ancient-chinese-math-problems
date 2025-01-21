"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
術曰：列絲一百八十八斤，以一十六两乘之、納十两，得三千一十八两；以五文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we will calculate the total cost of 188斤 (jin) and 10两 (liang) of silk, given that 1两 costs 5文 (wen). Here's the Python code:


"""


from fractions import Fraction

# Given data
cost_per_liang = 5  # in wen
jin_to_liang = 16  # 1 jin = 16 liang
silk_weight_jin = 188  # in jin
silk_weight_liang = 10  # in liang

# Convert total weight to liang
total_weight_liang = silk_weight_jin * jin_to_liang + silk_weight_liang

# Calculate total cost in wen
total_cost_wen = total_weight_liang * cost_per_liang

# Convert total cost to guan (1 guan = 1000 wen)
a = Fraction(total_cost_wen, 1000)

# Output the result
a


"""


The variable `a` will contain the total cost in 貫 (guan).
"""


"""
"""
