"""
今有絲一斤價直三百四十五。今有絲七兩一十二銖，問︰得錢幾何？
術曰：以一斤銖數為法，以一斤價數，乘七兩一十二銖為實。實如法得錢數。
荅曰： a錢 。
"""

"""
To solve this problem, we need to calculate the value of 7 taels and 12 zhu of silk, given that 1 jin (16 taels) of silk costs 345 qian. Here's the Python code:


"""


from fractions import Fraction

# Given values
price_per_jin = 345  # in qian
jin_to_taels = 16  # 1 jin = 16 taels
tael_to_zhu = 24  # 1 tael = 24 zhu

# Convert 7 taels and 12 zhu into the fraction of a jin
taels = 7
zhu = 12
total_zhu = taels * tael_to_zhu + zhu  # Total zhu
total_jin_fraction = Fraction(total_zhu, jin_to_taels * tael_to_zhu)  # Fraction of a jin

# Calculate the price
a = total_jin_fraction * price_per_jin  # Price in qian

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the answer in qian.
"""


"""
"""
