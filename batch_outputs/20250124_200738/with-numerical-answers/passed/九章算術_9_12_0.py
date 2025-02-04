"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a(=91/20)尺 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo 1 zhang tall. Its tip bends and touches the ground, 3 chi away from the base.
Question: how tall is the bent portion of the bamboo?

The procedure says: Take the distance from the base (去本) and square it. Treat it as if it were the height (高), and divide by 1.
Subtract the result from the total height of the bamboo, and halve the remainder. This gives the height of the bent portion.

Answer: *a*(=91/20) chi.
"""

# 竹高一丈
竹高 = 10  # 1 丈 = 10 尺

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一，所得
所得 = Fraction(去本平方, 竹高)

# 以減竹高
餘高 = 竹高 - 所得

# 而半其餘，即折者之高
a = Fraction(餘高, 2)  # 91/20
#----- content ends here -----

"""
"""
