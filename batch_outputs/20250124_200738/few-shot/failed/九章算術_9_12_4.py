"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo that is 1 zhang tall. Its tip bends and touches the ground, and the distance from the base to the point where the tip touches the ground is 3 chi.
Question: how tall is the bent bamboo?

The procedure says: Take the distance from the base (3 chi) and square it. Treat it as if it were the height (1 zhang) and divide by it.
Subtract the result from the bamboo's height, then halve the remainder. This gives the height of the bent bamboo.

Answer: *a* chi.
"""

# 竹高一丈 (convert to chi, as 1丈 = 10尺)
竹高 = 10

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一
商 = 去本平方 / 竹高

# 所得，以減竹高
餘 = 竹高 - 商

# 而半其餘，即折者之高
a = Fraction(餘, 2)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
