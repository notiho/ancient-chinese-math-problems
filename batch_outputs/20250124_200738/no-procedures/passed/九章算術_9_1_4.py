"""
今有弦五尺，句三尺，問︰為股幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the hypotenuse (弦) is 5 chi, and one leg (句) is 3 chi.
Question: how long is the other leg (股)?

Answer: it is *a* chi.
"""

# 弦 (hypotenuse)
弦 = 5

# 句 (one leg)
句 = 3

# 股 (the other leg) is calculated using the Pythagorean theorem: 弦^2 = 句^2 + 股^2
# 股^2 = 弦^2 - 句^2
股_squared = 弦**2 - 句**2

# 股 = square root of 股_squared
# Since we cannot use external functions, we simplify manually:
# 股_squared = 25 - 9 = 16
# 股 = 4

a = 4  # 股 is 4 chi#----- content ends here -----

"""
"""
