"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the price per unit weight (銖 rate) and the total weight in different units (鈞 and 石). We will use the `Fraction` class to handle calculations involving fractions.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_money = 13970  # Total money in 錢
total_weight_stone = 1  # 石
total_weight_jun = 2  # 鈞
total_weight_jin = 28  # 斤
total_weight_liang = 3  # 兩
total_weight_zhu = 5  # 銖

# Conversion factors
jin_to_liang = 16  # 1 斤 = 16 兩
liang_to_zhu = 24  # 1 兩 = 24 銖
jun_to_jin = 30  # 1 鈞 = 30 斤
stone_to_jun = 4  # 1 石 = 4 鈞

# Convert total weight to 銖
total_weight_in_zhu = (
    total_weight_stone * stone_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    total_weight_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    total_weight_jin * jin_to_liang * liang_to_zhu +
    total_weight_liang * liang_to_zhu +
    total_weight_zhu
)

# Calculate the 銖 rate (price per 銖)
zhu_rate = Fraction(total_money, total_weight_in_zhu)

# Calculate the 鈞 rate (price per 鈞)
weight_per_jun_in_zhu = jun_to_jin * jin_to_liang * liang_to_zhu
jun_rate = zhu_rate * weight_per_jun_in_zhu

# Calculate the 石 rate (price per 石)
weight_per_stone_in_zhu = stone_to_jun * weight_per_jun_in_zhu
stone_rate = zhu_rate * weight_per_stone_in_zhu

# Assign the results to the variables
a = jun_rate.numerator  # 鈞 rate numerator
b = jun_rate.denominator  # 鈞 rate denominator
c = stone_rate.numerator  # 石 rate numerator
d = stone_rate.denominator  # 石 rate denominator

# Results
print(f"a = {a}, b = {b}, c = {c}, d = {d}")
#----- content ends here -----


"""


This code calculates the values of `a`, `b`, `c`, and `d` as described in the problem. The results are stored in the respective variables and printed at the end.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 160934400
Variable 'b' has wrong value. Expected: 5, Actual: 79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 643737600
Variable 'd' has wrong value. Expected: 6, Actual: 79949"""
