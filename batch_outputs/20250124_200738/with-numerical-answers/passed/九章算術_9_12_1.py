"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a(=91/20)尺 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo that is 1 zhang tall. Its tip bends and touches the ground, 3 chi away from the base.
Question: how tall is the remaining standing part of the bamboo?

The procedure says: Take the distance from the base (3 chi) and square it.
Let it be divided by the height of the bamboo (1 zhang = 10 chi), treating the height as the divisor.
Subtract the result from the total height of the bamboo.
Halve the remainder, and that is the height of the standing part of the bamboo.

Answer: *a*(=91/20) chi.
"""

# 竹高一丈
竹高 = 10  # 1 zhang = 10 chi

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一，所得
商 = Fraction(去本平方, 竹高)

# 以減竹高
餘 = 竹高 - 商

# 而半其餘，即折者之高
a = Fraction(餘, 2)  # 91/20 chi#----- content ends here -----

"""
"""
