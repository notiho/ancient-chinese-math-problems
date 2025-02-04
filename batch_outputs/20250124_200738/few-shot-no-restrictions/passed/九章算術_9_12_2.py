"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo that is 1 zhang tall. Its tip bends and touches the ground, 3 chi away from the base.
Question: how high is the point where the bamboo is bent?

The procedure says: Square the distance from the base (3 chi), and divide it by the bamboo's height (1 zhang, or 10 chi).
Subtract the result from the bamboo's height, and halve the remainder.
This gives the height of the bent point.

Answer: *a* chi.
"""

from fractions import Fraction

# 竹高一丈 (1丈 = 10尺)
竹高 = 10  # 尺

# 末折抵地，去本三尺
去本 = 3  # 尺

# 以去本自乘
去本平方 = 去本 ** 2

# 令如高而一，所得
所得 = Fraction(去本平方, 竹高)

# 以減竹高
剩餘 = 竹高 - 所得

# 而半其餘，即折者之高
a = 剩餘 / 2

a  # Output the height of the bent point in chi#----- content ends here -----

"""
"""
