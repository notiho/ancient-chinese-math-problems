"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為菽 b斛 。
"""

"""

"""


from fractions import Fraction

# 下周三丈，高七尺
下周 = 3 * 10  # 三丈 = 30 尺
高 = 7  # 高七尺

# 委粟術曰：下周自乘
下周積 = 下周 * 下周

# 以高乘之
體積 = 下周積 * 高

# 三十六而一
積 = Fraction(體積, 36)

# 程粟一斛，積二尺七寸
一斛積 = 2 + Fraction(7, 10)  # 2尺7寸 = 2.7尺

# 其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三
菽一斛積 = 2 + Fraction(4, 10) + Fraction(3, 100)  # 2尺4寸3分 = 2.43尺

# 計算為菽幾斛
為菽 = Fraction(積, 菽一斛積)

# 答案
a = 積  # 積 a 尺
b = 為菽  # 為菽 b 斛


"""

"""


"""
Variable 'a' has wrong value. Expected: 350, Actual: 175
Variable 'b' has wrong value. Expected: 35000/243, Actual: 17500/243"""
