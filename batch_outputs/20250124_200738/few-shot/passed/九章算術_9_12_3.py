"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo that is 1 zhang tall. Its tip bends and touches the ground, and the distance from the base of the bamboo to the point where the tip touches the ground is 3 chi.
Question: how tall is the remaining upright part of the bamboo?

The procedure says: Take the distance from the base (3 chi) and square it. 
Make it proportional to the height (1 zhang = 10 chi) as the divisor.
Subtract the result from the total height of the bamboo, and halve the remainder. 
This gives the height of the upright part of the bamboo.

Answer: *a* chi.
"""

# 竹高一丈 (1丈 = 10尺)
竹高 = 10

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一
比例法 = 竹高

# 所得
所得 = Fraction(去本平方, 比例法)

# 以減竹高
剩餘 = 竹高 - 所得

# 而半其餘，即折者之高
a = Fraction(剩餘, 2)#----- content ends here -----

"""
"""
