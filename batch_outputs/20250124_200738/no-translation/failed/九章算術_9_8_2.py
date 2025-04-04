"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 深一寸
深寸 = Fraction(1, 10)  # 1 寸 = 1/10 尺

# 鐻道長一尺
鐻道 = 1

# 半鐻道自乘
半鐻道 = Fraction(鐻道, 2)
半鐻道平方 = 半鐻道 * 半鐻道

# 如深寸而一
深寸平方 = 深寸 * 深寸

# 以深寸增之
材徑平方 = 半鐻道平方 + 深寸平方

# 即材徑
a = 材徑平方 ** Fraction(1, 2)  # 開平方
#----- content ends here -----


"""
 

材徑 `a` 的單位為尺。
"""


"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 0.5099019513592785"""
