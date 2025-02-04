"""
今有圓田周三百九十六步欲為方問得幾何
術曰周自相乗十二而一所得開方除之即得方
答曰 a步
"""

"""
Suppose there is a circular field with a circumference of 396 bu.
It is desired to convert it into a square field.
Question: what is the side length of the square?

The procedure says: Multiply the circumference by itself. Divide the result by 12. 
Take the square root of the result, and that is the side length of the square.

Answer: *a* bu.
"""

from fractions import Fraction

# 圓田周三百九十六步
圓田周 = 396

# 周自相乘
積 = 圓田周 * 圓田周

# 十二而一
積除十二 = Fraction(積, 12)

# 所得開方
# Since we cannot use external libraries, we manually compute the square root using approximation.
def 開方(x):
    guess = x / 2
    for _ in range(20):  # Perform 20 iterations for approximation
        guess = (guess + x / guess) / 2
    return guess

a = 開方(積除十二)  # 方田的邊長 (side length of the square)
"""
Timed out"""
