"""
又有田廣二里，從三里。問：為田幾何？
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 2 li and a length of 3 li.
Question: how large is the field?

Answer: it makes *a* qing.
"""

# 廣二里
廣 = 2

# 從三里
從 = 3

# Multiply width and length to get the area in square li
area_in_square_li = 廣 * 從

# Convert square li to qing (1 qing = 100 square li)
a = Fraction(area_in_square_li, 100)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 45/2, Actual: 3/50"""
