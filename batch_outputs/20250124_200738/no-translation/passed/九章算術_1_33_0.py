"""
又有宛田，下周九十九步，徑五十一步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a畝 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 下周九十九步
周 = 99

# 徑五十一步
徑 = 51

# 以徑乘周
積步 = 徑 * 周

# 四而一
積步 = Fraction(積步, 4)

# 畝法二百四十步
畝法 = 240

# 以畝法二百四十步除之，即畝數
a = Fraction(積步, 畝法)
#----- content ends here -----


"""

"""


"""
"""
