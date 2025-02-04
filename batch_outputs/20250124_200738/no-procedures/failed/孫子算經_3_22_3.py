"""
今有方物一束外周，一市有三十二枚。問：積幾何？
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a square bundle of objects, with the total perimeter of one side being 32 items.
Question: how many items are in the bundle?

Answer: *a* items.
"""

# 外周 (perimeter) = 32 枚
外周 = 32

# Since the perimeter of a square is 4 times the side length, calculate the side length
邊長 = Fraction(外周, 4)

# The area (total items in the square) is the side length squared
a = 邊長 * 邊長#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 81, Actual: 64"""
