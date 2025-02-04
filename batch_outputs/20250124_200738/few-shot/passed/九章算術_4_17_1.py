"""
今有積三百步。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 300 bu. 
Question: what is the circumference of the circle?

The procedure for opening a circle says: Place the number of bu in the area.
Multiply it by 12.
Take the square root of the result, and that gives the circumference.

Answer: *a* bu.
"""

# 積三百步
積步數 = 300

# 以十二乘之
積乘十二 = 12 * 積步數

# 以開方除之，即得周
# To compute the square root manually, we use an iterative method (Babylonian method).

def 開方(x):
    # Initial guess
    guess = x / 2
    # Iterate to improve the guess
    for _ in range(20):  # 20 iterations for sufficient precision
        guess = (guess + x / guess) / 2
    return guess

a = 開方(積乘十二)  # 圓周#----- content ends here -----

"""
"""
