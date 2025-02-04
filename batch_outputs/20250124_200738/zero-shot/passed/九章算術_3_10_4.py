"""
今有絲一斤價直三百四十五。今有絲七兩一十二銖，問︰得錢幾何？
術曰：以一斤銖數為法，以一斤價數，乘七兩一十二銖為實。實如法得錢數。
荅曰： a錢 。
"""

"""
To solve this problem, we need to calculate the value of 7 taels and 12 zhus (ancient Chinese units of weight) of silk, given that 1 jin (1 pound) of silk costs 345 qian (ancient Chinese currency). Here's the Python code to compute the answer:


"""

#----- content starts here -----

from fractions import Fraction

# Conversion factors
jin_to_liang = 16  # 1 jin = 16 taels (liang)
liang_to_zhu = 24  # 1 tael = 24 zhus

# Known values
price_per_jin = 345  # in qian
weight_liang = 7  # 7 taels
weight_zhu = 12  # 12 zhus

# Total weight in zhus
total_weight_in_zhu = weight_liang * liang_to_zhu + weight_zhu

# Total weight in jin (as a fraction)
total_weight_in_jin = Fraction(total_weight_in_zhu, jin_to_liang * liang_to_zhu)

# Calculate the total price
a = total_weight_in_jin * price_per_jin

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the total price in qian.
"""


"""
"""
