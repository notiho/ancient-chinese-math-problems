"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the price per unit weight of silk in two different units: 鈞 (a traditional Chinese unit of weight) and 石 (another traditional Chinese unit of weight). The total cost and total weight are given, and we need to compute the price per 鈞 and per 石.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_money = 13970  # in 錢
total_weight_stone = 1  # 石
total_weight_jun = 2  # 鈞
total_weight_jin = 28  # 斤
total_weight_liang = 3  # 兩
total_weight_zhu = 5  # 銖

# Conversion factors
jin_per_jun = 30  # 1 鈞 = 30 斤
liang_per_jin = 16  # 1 斤 = 16 兩
zhu_per_liang = 24  # 1 兩 = 24 銖
jun_per_stone = 4  # 1 石 = 4 鈞

# Convert total weight to 銖 (smallest unit)
total_weight_zhu += (total_weight_liang * zhu_per_liang)
total_weight_zhu += (total_weight_jin * liang_per_jin * zhu_per_liang)
total_weight_zhu += (total_weight_jun * jin_per_jun * liang_per_jin * zhu_per_liang)
total_weight_zhu += (total_weight_stone * jun_per_stone * jin_per_jun * liang_per_jin * zhu_per_liang)

# Price per 銖
price_per_zhu = Fraction(total_money, total_weight_zhu)

# Price per 鈞 (1 鈞 = 30 斤 = 480 兩 = 11520 銖)
price_per_jun = price_per_zhu * jin_per_jun * liang_per_jin * zhu_per_liang

# Price per 石 (1 石 = 4 鈞)
price_per_stone = price_per_jun * jun_per_stone

# Extracting the price per 鈞 in 銖 and 錢
a = price_per_jun.numerator // price_per_jun.denominator  # 鈞
b = price_per_jun.numerator % price_per_jun.denominator  # 銖

# Extracting the price per 石 in 銖 and 錢
c = price_per_stone.numerator // price_per_stone.denominator  # 石
d = price_per_stone.numerator % price_per_stone.denominator  # 銖

# Results
a, b, c, d
#----- content ends here -----


"""


This code calculates the values of `a`, `b`, `c`, and `d` as described in the problem. The results are stored in the variables `a`, `b`, `c`, and `d`.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 2012
Variable 'b' has wrong value. Expected: 5, Actual: 77012
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 8051
Variable 'd' has wrong value. Expected: 6, Actual: 68201"""
