"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
術曰：列絲一百八十八斤，以一十六两乘之、納十两，得三千一十八两；以五文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we will calculate the total value of the silk in "貫" (a unit of currency). Here's the Python code:


"""


from fractions import Fraction

# Given data
price_per_liang = Fraction(5, 1)  # 5 文 per 两
silk_weight_jin = 188  # 188 斤
silk_weight_liang = 10  # 10 两
liang_per_jin = 16  # 1 斤 = 16 两

# Step 1: Convert the total weight into 两
total_liang = silk_weight_jin * liang_per_jin + silk_weight_liang  # 188 * 16 + 10
total_liang = Fraction(total_liang)

# Step 2: Calculate the total value in 文
total_value_wen = total_liang * price_per_liang  # total_liang * 5

# Step 3: Convert the total value into 貫 (1 貫 = 1000 文)
a = total_value_wen / 1000  # Convert 文 to 貫

# The answer is stored in the variable "a"


"""


The variable `a` will contain the total value of the silk in 貫.
"""


"""
"""
