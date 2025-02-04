"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
術曰：置米積尺，以十二乘之，令高而一，所得，開方除之，即周。
荅曰： a丈 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction
import math

# 高一丈三尺三寸、少半寸
高 = 10 + 3 + Fraction(3, 10) - Fraction(1, 20)

# 容米二千斛
米積 = 2000

# 置米積尺，以十二乘之
米積尺 = 米積 * 12

# 令高而一
積高 = 米積尺 / 高

# 所得，開方除之，即周
周 = math.sqrt(積高)

# Convert to 丈
a = 周 / 10
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 27/5, Actual: 4.255961412791452"""
