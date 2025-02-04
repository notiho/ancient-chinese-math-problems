"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
荅曰：為大䵂 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into daqu (a type of fermented grain product).
Question: how much daqu is obtained?

Answer: it makes *a* dou of daqu.
"""

# 粟九斗八升
粟_斗 = 9
粟_升 = 8

# Convert everything to sheng (1 dou = 10 sheng)
總粟_升 = 粟_斗 * 10 + 粟_升

# To make daqu, multiply by 2 and divide by 3
總大䵂_升 = Fraction(2 * 總粟_升, 3)

# Convert back to dou and sheng
a_斗 = 總大䵂_升 // 10  # Whole number of dou
a_升 = 總大䵂_升 % 10   # Remaining sheng

# Final result
a = Fraction(總大䵂_升, 10)  # Represent the result in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1323/125, Actual: 98/15"""
