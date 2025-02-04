"""
今有竹高一丈末折抵地去本三尺問折者高幾何
術曰以去本自乘令如高而一所得以減竹高而半其餘即折者之高也
荅曰 a尺 
"""

"""
Suppose there is a bamboo 1 zhang tall. Its tip is bent and touches the ground, 3 chi away from the base.
Question: how tall is the bent part?

The procedure says: Take the distance from the base (3 chi) and square it.
Make it proportional to the height (1 zhang = 10 chi) as the divisor.
Subtract the result from the bamboo's height, and halve the remainder.
This gives the height of the bent part.

Answer: *a* chi.
"""

# 竹高一丈 (1丈 = 10尺)
竹高 = 10

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一 (竹高為法)
比例結果 = Fraction(去本平方, 竹高)

# 所得以減竹高
剩餘 = 竹高 - 比例結果

# 而半其餘
a = 剩餘 / 2
"""
"""
