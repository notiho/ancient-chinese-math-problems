"""
今有絲一斤價直三百四十五。今有絲七兩一十二銖，問︰得錢幾何？
術曰：以一斤銖數為法，以一斤價數，乘七兩一十二銖為實。實如法得錢數。
荅曰： a錢 。
"""

"""
To solve this problem, we need to calculate the value of 7 taels (兩) and 12 zhu (銖) of silk, given that 1 jin (斤) of silk costs 345 qian (錢). 

1 jin = 16 taels  
1 tael = 24 zhu  

Here's the Python code to compute the value:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
price_per_jin = 345  # in qian
jin_to_taels = 16  # 1 jin = 16 taels
tael_to_zhu = 24  # 1 tael = 24 zhu

# Convert 7 taels and 12 zhu into the fraction of a jin
taels = 7
zhu = 12
total_zhu = taels * tael_to_zhu + zhu  # total zhu
zhu_per_jin = jin_to_taels * tael_to_zhu  # total zhu in 1 jin
fraction_of_jin = Fraction(total_zhu, zhu_per_jin)

# Calculate the value in qian
a = fraction_of_jin * price_per_jin

# Result
a  # in qian
#----- content ends here -----


"""


The variable `a` will contain the value in qian.
"""


"""
"""
