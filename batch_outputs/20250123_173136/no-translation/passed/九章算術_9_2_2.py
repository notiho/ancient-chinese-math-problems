"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""


# 股四尺
股 = 4

# 弦五尺
弦 = 5

# 股自乘
股自乘 = 股 * 股

# 弦自乘
弦自乘 = 弦 * 弦

# 以減弦自乘，其餘開方除之，即句
句自乘 = 弦自乘 - 股自乘

# 開方 (即平方根)
# Since we are not using external libraries, we manually calculate the square root
def 開方(value):
    guess = value / 2
    for _ in range(20):  # Iterative approximation
        guess = (guess + value / guess) / 2
    return guess

a = 開方(句自乘)  # 即句
"""
"""
