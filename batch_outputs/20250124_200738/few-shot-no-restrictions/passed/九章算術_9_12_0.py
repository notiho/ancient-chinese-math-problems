"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo that is 1 zhang tall. Its tip bends and touches the ground, 3 chi away from its base.
Question: how tall is the remaining upright portion of the bamboo?

The procedure says: Take the distance from the base (3 chi) and square it. 
Let the result be divided by the height of the bamboo (1 zhang = 10 chi). 
Subtract the result from the total height of the bamboo, and halve the remainder.
This gives the height of the upright portion of the bamboo.

Answer: *a* chi.
"""

from fractions import Fraction

# 竹高一丈 (1丈 = 10尺)
竹高 = 10  # in chi

# 去本三尺
去本 = 3  # in chi

# 以去本自乘
去本平方 = 去本 ** 2

# 令如高而一
分數 = Fraction(去本平方, 竹高)

# 所得，以減竹高
剩餘高度 = 竹高 - 分數

# 而半其餘
a = 剩餘高度 / 2

# Output the result
a#----- content ends here -----

"""
"""
