"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為菽 b斛 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 下周三丈
下周 = 3 * 10  # 將丈轉換為尺

# 高七尺
高 = 7

# 委粟術曰：下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 三十六而一
積 = Fraction(積, 36)

# 程粟一斛，積二尺七寸
一斛積 = 2 + Fraction(7, 10)  # 2尺7寸轉換為小數

# 為菽
b = Fraction(積, 一斛積)

# 結果
a = 積
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 350, Actual: 175
Variable 'b' has wrong value. Expected: 35000/243, Actual: 1750/27"""
