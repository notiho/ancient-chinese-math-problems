"""
今有積三百步。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a(=60)步 。
"""

"""
Suppose there is an area of 300 bu. 
Question: what is the circumference of the circle?

The procedure for circles says: Place the number of bu of the area.
Multiply it by 12.
Extract the square root and divide by it, obtaining the circumference.

Answer: *a*(=60) bu.
"""

# 積三百步
積步數 = 300

# 以十二乘之
積乘十二 = 12 * 積步數

# 開方除之，即得周
# Since we cannot use external functions, we manually compute the square root using an iterative approximation.
def 開方(x):
    guess = x / 2  # Initial guess
    for _ in range(20):  # Perform 20 iterations for approximation
        guess = (guess + x / guess) / 2
    return guess

周 = 開方(積乘十二)

a = 周  # 60 steps
"""
"""
