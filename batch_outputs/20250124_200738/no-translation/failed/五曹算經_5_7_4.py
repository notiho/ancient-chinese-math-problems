"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

"""

"""

#----- content starts here -----

# 錦一疋直錢八貫
錢 = 8  # 貫

# 一疋等於四十尺
疋長 = 40  # 尺

# 以四十尺除之即尺價
尺價 = Fraction(錢, 疋長)

# 進位即丈價 (1丈 = 10尺)
丈價 = 10 * 尺價

# 退位即寸價 (1尺 = 10寸)
寸價 = Fraction(尺價, 10)

# 答案
a = 丈價  # 一丈價
b = 尺價  # 一尺價
c = 寸價  # 一寸價
#----- content ends here -----


"""

"""


"""
Variable 'b' has wrong value. Expected: 200, Actual: 1/5
Variable 'c' has wrong value. Expected: 20, Actual: 1/50"""
