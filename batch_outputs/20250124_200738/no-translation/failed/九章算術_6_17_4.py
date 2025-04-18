"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 置錢錐行衰
錢分配 = [5, 4, 3, 2, 1]

# 并上二人為九
上二人 = 錢分配[0] + 錢分配[1]

# 并下三人為六
下三人 = 錢分配[2] + 錢分配[3] + 錢分配[4]

# 六少於九，三
差 = 上二人 - 下三人

# 以三均加焉
錢分配 = [x + 差 for x in 錢分配]

# 副并為法
法 = sum(錢分配)

# 以所分錢乘未并者各自為實
總錢 = 5
實 = [總錢 * x for x in 錢分配]

# 實如法得一錢
分配結果 = [Fraction(x, 法) for x in 実]

a, b, c, d, e = 分配結果
#----- content ends here -----


"""

"""


"""
Code error: name '実' is not defined"""
