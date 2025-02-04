"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a人 ，絹 b匹 。
"""

"""

"""

#----- content starts here -----

# 人得六匹
右上 = 6

# 盈六匹
右下 = 6

# 人得七匹
左上 = 7

# 不足七匹
左下 = 7

# 維乘之所得
右積 = 右上 * 右下
左積 = 左上 * 左下

# 并之為絹
b = Fraction(右積 + 左積, 左上 + 右上)

# 并盈不足為人
a = Fraction(右積 + 左積, 右下 + 左下)
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 13, Actual: 85/13
Variable 'b' has wrong value. Expected: 84, Actual: 85/13"""
