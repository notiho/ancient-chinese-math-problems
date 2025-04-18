"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

"""
Suppose there is a bamboo that is 1 zhang tall. Its tip bends and touches the ground, 3 chi away from the base.
Question: how tall is the bent portion of the bamboo?

The procedure says: Take the distance from the base (3 chi) and square it.
Let it be divided by the height of the bamboo (1 zhang = 10 chi), obtaining a result.
Subtract this result from the total height of the bamboo, and halve the remainder.
This gives the height of the bent portion.

Answer: *a* chi.
"""

# 竹高一丈
竹高 = 10  # 1 丈 = 10 尺

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一
所得 = Fraction(去本平方, 竹高)

# 所得，以減竹高
餘 = 竹高 - 所得

# 而半其餘
a = Fraction(餘, 2)
"""
"""
