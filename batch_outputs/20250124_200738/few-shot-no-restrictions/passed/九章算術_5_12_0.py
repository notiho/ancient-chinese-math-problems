"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
術曰：方自乘，以高乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square fort with a side length of 1 zhang and 6 chi, and a height of 1 zhang and 5 chi.
Question: what is the volume?

The procedure says: Multiply the side length by itself, then multiply by the height. This gives the volume in cubic chi.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# 方堡壔邊長：1丈6尺
邊長 = 1 * 10 + 6  # Convert to chi (1丈 = 10尺)

# 高：1丈5尺
高 = 1 * 10 + 5  # Convert to chi (1丈 = 10尺)

# 方自乘 (邊長平方)
底面積 = 邊長 * 邊長

# 以高乘之，即積尺
積 = 底面積 * 高

a = 積  # Volume in cubic chi

print(f"Answer: {a} cubic chi.")#----- content ends here -----

"""
"""
