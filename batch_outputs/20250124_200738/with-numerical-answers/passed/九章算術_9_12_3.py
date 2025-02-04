"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a(=91/20)尺 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo 1 zhang tall. Its tip bends and touches the ground, 3 chi away from the base.
Question: how high is the bent part of the bamboo?

The procedure says: Take the distance from the base (去本) and square it. 
Let this be divided by the height of the bamboo (高), treating the height as the divisor.
Subtract the result from the total height of the bamboo, and halve the remainder.
This gives the height of the bent part.

Answer: *a*(=91/20) chi.
"""

from fractions import Fraction

# 竹高一丈 (convert to chi)
竹高 = 10  # 1丈 = 10尺

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一，所得
所得 = Fraction(去本平方, 竹高)

# 以減竹高
餘 = 竹高 - 所得

# 而半其餘，即折者之高也
a = Fraction(餘, 2)  # 91/20 chi#----- content ends here -----

"""
"""
