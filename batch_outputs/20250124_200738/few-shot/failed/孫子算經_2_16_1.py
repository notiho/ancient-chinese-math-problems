"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
術曰：置堤，上廣三丈，下廣五丈。并之，得八丈；半之，得四丈。以二丈乘之，得八百尺；以長六十尺乘之，得四萬八千；以一千尺除之，即得。
答曰： a 方。
"""

#----- content starts here -----
"""
Suppose there is a dike with a bottom width of 5 zhang, a top width of 3 zhang, a height of 2 zhang, and a length of 60 chi.
It is desired to calculate how many cubic units (fang) can be made with 1000 cubic chi.

The procedure says: Place the dike, with a top width of 3 zhang and a bottom width of 5 zhang.
Add them together, obtaining 8 zhang.
Halve it, obtaining 4 zhang.
Multiply it by the height of 2 zhang, obtaining 8 zhang-chi (800 chi).
Multiply it by the length of 60 chi, obtaining 48000 cubic chi.
Divide it by 1000 cubic chi, obtaining the result.

The answer says: *a* cubic units (fang).
"""

# 下廣五丈
下廣 = 5

# 上廣三丈
上廣 = 3

# 高二丈
高 = 2

# 長六十尺
長 = 60

# 一千尺作一方
一方 = 1000

# 并之，得八丈
總廣 = 上廣 + 下廣

# 半之，得四丈
平均廣 = Fraction(總廣, 2)

# 以二丈乘之，得八百尺
截面積 = 平均廣 * 高 * 10  # Convert zhang to chi

# 以長六十尺乘之，得四萬八千
體積 = 截面積 * 長

# 以一千尺除之，即得
a = Fraction(體積, 一方)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 48, Actual: 24/5"""
