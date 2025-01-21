"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
Suppose there is a right triangle with a leg (gu) of 4 chi and a hypotenuse (xian) of 5 chi.
Question: how long is the other leg (ju)?

The procedure for right triangles says:
1. Multiply the gu and ju by themselves, add them together, and take the square root to obtain the xian.
2. Multiply the gu by itself, subtract the square of the xian, and take the square root to obtain the ju.
3. Multiply the ju by itself, subtract the square of the xian, and take the square root to obtain the gu.

Answer: *a* chi.
"""

# 股四尺
股 = 4

# 弦五尺
弦 = 5

# 股自乘
股平方 = 股 * 股

# 弦自乘
弦平方 = 弦 * 弦

# 以減弦自乘，其餘開方除之，即句
句平方 = 弦平方 - 股平方

# 開方 (square root) of 句平方
# Since we cannot use external libraries, we manually calculate the square root using an iterative method.
def 開方(n, iterations=10):
    x = n / 2  # Initial guess
    for _ in range(iterations):
        x = (x + n / x) / 2
    return x

a = 開方(句平方)  # The length of the other leg (句) in chi
"""
"""
