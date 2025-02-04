"""
今有積三百步。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a(=60)步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 300 bu.
Question: what is the circumference of the circle?

The procedure for circles says: Place the number of bu in the area.
Multiply it by 12.
Take the square root of the result, and that is the circumference.

Answer: *a*(=60) bu.
"""

# 積三百步
積步數 = 300

# 以十二乘之
積乘十二 = 12 * 積步數

# 以開方除之，即得周
# To compute the square root manually without external functions:
def 開方(n):
    # Babylonian method for square root approximation
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

a = 開方(積乘十二) # 60#----- content ends here -----

"""
"""
