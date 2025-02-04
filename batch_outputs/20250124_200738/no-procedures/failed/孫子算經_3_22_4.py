"""
今有方物一束外周，一市有三十二枚。問：積幾何？
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a square bundle of items, with the total perimeter being 32 units (枚).
Question: what is the total number of items in the bundle (its area)?

Answer: *a* items (枚).
"""

# 外周 (perimeter) = 32 枚
外周 = 32

# The side length of the square is the perimeter divided by 4
邊長 = Fraction(外周, 4)

# The area of the square is the side length squared
a = 邊長 * 邊長#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 81, Actual: 64"""
