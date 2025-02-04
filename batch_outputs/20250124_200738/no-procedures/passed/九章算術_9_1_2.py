"""
今有弦五尺，句三尺，問︰為股幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the hypotenuse (弦) is 5 chi and one leg (句) is 3 chi.
Question: how long is the other leg (股)?

Answer: it is *a* chi.
"""

# 弦五尺
弦 = 5

# 句三尺
句 = 3

# Use the Pythagorean theorem: 弦^2 = 句^2 + 股^2
# 股^2 = 弦^2 - 句^2
股_squared = 弦**2 - 句**2

# 股 = sqrt(股^2)
a = 股_squared**0.5

a#----- content ends here -----

"""
"""
