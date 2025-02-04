"""
今有車二萬三千九百乘，欲作方營，每乘占地三步。問：計㡬何？
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there are 23,900 chariots, and each chariot occupies 3 bu of land. It is desired to arrange them into a square formation.
Question: what is the side length of the square in bu?

Answer: *a* bu.
"""

# 車二萬三千九百乘
chariots = 23900

# 每乘占地三步
area_per_chariot = 3

# 總占地面積 (總步數)
total_area = chariots * area_per_chariot

# 方營邊長 (a步) = 總占地面積的平方根
# Since we cannot use external functions, we calculate the square root manually using an iterative method.

def square_root(n, precision=10):
    """Calculate the square root of n using the Babylonian method."""
    x = n
    for _ in range(precision):
        x = (x + n / x) / 2
    return x

# 計算邊長
a = square_root(total_area)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 71700, Actual: 268.02401801223675"""
