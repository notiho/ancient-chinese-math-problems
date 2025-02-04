"""
今有粟七斗八升，欲為豉。問︰得幾何？
荅曰：為豉 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 8 sheng of millet. It is desired to turn it into fermented soybean paste (chi).
Question: how much fermented soybean paste does it make?

Answer: it makes *a* dou of fermented soybean paste.
"""

# 粟七斗八升
粟 = 7 + Fraction(8, 10)  # Convert 8 sheng into dou (1 dou = 10 sheng)

# To make fermented soybean paste, millet reduces to 2/3 of its original volume
a = Fraction(2, 3) * 粟#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2457/250, Actual: 26/5"""
