"""
今有句三尺，股四尺，問︰為弦幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with one leg (base, "ju") of 3 chi and the other leg (height, "gu") of 4 chi.
Question: how long is the hypotenuse ("xian")?

Answer: it is *a* chi.
"""

# 句 (base) = 3 尺
句 = 3

# 股 (height) = 4 尺
股 = 4

# Use the Pythagorean theorem to calculate the hypotenuse
# 弦 = sqrt(句^2 + 股^2)
弦_squared = 句**2 + 股**2
a = 弦_squared**0.5  # Taking the square root

a  # Output the result in chi#----- content ends here -----

"""
"""
