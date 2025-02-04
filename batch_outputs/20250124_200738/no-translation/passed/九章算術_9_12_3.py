"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 竹高一丈 (convert to 尺, 1 丈 = 10 尺)
竹高 = 10

# 去本三尺
去本 = 3

# 以去本自乘
去本自乘 = 去本 * 去本

# 令如高而一 (竹高 as the denominator)
所得 = Fraction(去本自乘, 竹高)

# 所得，以減竹高
餘 = 竹高 - 所得

# 半其餘，即折者之高
a = Fraction(餘, 2)
#----- content ends here -----


"""

"""


"""
"""
