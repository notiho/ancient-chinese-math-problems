"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

#----- content starts here -----

# 下方五丈
下方 = 5

# 上方四丈
上方 = 4

# 高五丈
高 = 5

# 上下方相乘
上下方積 = 下方 * 上方

# 又各自乘
下方積 = 下方 * 下方
上方積 = 上方 * 上方

# 并之
總積 = 上下方積 + 下方積 + 上方積

# 以高乘之
體積 = 總積 * 高

# 三而一
a = Fraction(體積, 3) * 100  # 1丈 = 10尺, so convert to 尺
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 30500/3"""
