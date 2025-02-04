"""
今有竹高一丈末折抵地去本三尺問折者高幾何
術曰以去本自乘令如高而一所得以減竹高而半其餘即折者之高也
荅曰 a尺 
"""

"""
Suppose there is a bamboo that is 1 zhang tall. The top of the bamboo bends and touches the ground, 3 chi away from the base.
Question: how tall is the remaining upright part of the bamboo?

The procedure says: Take the distance from the base (3 chi) and square it. 
Let it be as the height (1 zhang = 10 chi), and divide by the height. 
Subtract the result from the total height of the bamboo, then halve the remainder. 
This gives the height of the upright part of the bamboo.

Answer: *a* chi.
"""

# 竹高一丈 (1丈 = 10尺)
竹高 = 10

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一，所得
所得 = Fraction(去本平方, 竹高)

# 以減竹高
餘高 = 竹高 - 所得

# 而半其餘，即折者之高
a = Fraction(餘高, 2)
"""
"""
