"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為粟 b斛 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 下周一十二丈
下周 = 12

# 高二丈
高 = 2

# 委粟術曰：下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 三十六而一
積 = Fraction(積, 36)

# 程粟一斛，積二尺七寸
一斛積 = 2 + Fraction(7, 10)

# 為粟幾何
粟斛 = Fraction(積, 一斛積)

# 答案
a = 積  # 積為 a 尺
b = 粟斛  # 粟為 b 斛
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 8000, Actual: 8
Variable 'b' has wrong value. Expected: 80000/27, Actual: 80/27"""
