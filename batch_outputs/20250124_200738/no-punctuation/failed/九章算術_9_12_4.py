"""
今有竹高一丈末折抵地去本三尺問折者高幾何
術曰以去本自乘令如高而一所得以減竹高而半其餘即折者之高也
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a bamboo that is 1 zhang tall. Its tip bends and touches the ground, 3 chi away from the base.
Question: how tall is the part of the bamboo that remains standing?

The procedure says: Take the distance from the base (3 chi) and square it. 
Let it be as if it were the height, and divide it by 1. 
Subtract the result from the total height of the bamboo. 
Halve the remainder, and that is the height of the standing part of the bamboo.

Answer: *a* chi.
"""

# 竹高一丈 (convert to chi: 1丈 = 10尺)
竹高 = 10

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一 (divide by 1, which does not change the value)
如高 = 去本平方

# 所得以減竹高
餘高 = 竹高 - 如高

# 而半其餘
a = Fraction(餘高, 2)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 91/20, Actual: 1/2"""
