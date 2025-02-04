"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

"""
Suppose there is a bamboo 1 zhang tall. Its tip bends and touches the ground, 3 chi away from the base.
Question: how high is the point where it bent?

The procedure says: Take the distance from the base (3 chi) and square it.
Let it be divided by the height of the bamboo (1 zhang = 10 chi).
Subtract the result from the height of the bamboo, and halve the remainder.
This gives the height of the point where it bent.

Answer: *a* chi.
"""

# 竹高一丈 (1丈 = 10尺)
竹高 = 10

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一
商 = Fraction(去本平方, 竹高)

# 所得，以減竹高
餘 = 竹高 - 商

# 而半其餘
a = Fraction(餘, 2)
"""
"""
