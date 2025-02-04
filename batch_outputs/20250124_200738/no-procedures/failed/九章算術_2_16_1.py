"""
今有粟五斗五升，欲為飧。問︰得幾何？
荅曰：為飧 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 dou and 5 sheng of millet. It is desired to turn it into cooked millet (food).
Question: how much cooked millet is obtained?

Answer: it makes *a* dou of cooked millet.
"""

# 粟五斗五升
粟 = 5 + Fraction(5, 10)  # 5 dou and 5 sheng (1 dou = 10 sheng)

# To turn millet into cooked millet, multiply by 2 and divide by 3
a = Fraction(2 * 粟, 3)  # Result in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 99/10, Actual: 11/3"""
