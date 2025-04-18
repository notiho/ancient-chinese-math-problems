"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
術曰：置堤，上廣三丈，下廣五丈。并之，得八丈；半之，得四丈。以二丈乘之，得八百尺；以長六十尺乘之，得四萬八千；以一千尺除之，即得。
答曰： a 方。
"""

"""

"""

#----- content starts here -----

# 下廣五丈
下廣 = 5

# 上廣三丈
上廣 = 3

# 高二丈
高 = 2

# 長六十尺
長 = 60

# 置堤，上廣三丈，下廣五丈。并之，得八丈
總廣 = 上廣 + 下廣

# 半之，得四丈
平均廣 = Fraction(總廣, 2)

# 以二丈乘之，得八百尺
橫截面積 = 平均廣 * 高 * 10  # 1丈 = 10尺

# 以長六十尺乘之，得四萬八千
堤積 = 橫截面積 * 長

# 以一千尺除之，即得
a = Fraction(堤積, 1000)
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 48, Actual: 24/5"""
