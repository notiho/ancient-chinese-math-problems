"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
術曰：置堤，上廣三丈，下廣五丈。并之，得八丈；半之，得四丈。以二丈乘之，得八百尺；以長六十尺乘之，得四萬八千；以一千尺除之，即得。
答曰： a(=48) 方。
"""

"""
Suppose there is a dike. The bottom width is 5 zhang, the top width is 3 zhang, the height is 2 zhang, and the length is 60 chi. 
It is desired to calculate how many units of 1000 cubic chi can be formed.

The procedure says: Place the dike, with the top width of 3 zhang and the bottom width of 5 zhang.
Add them, obtaining 8 zhang. Halve it, obtaining 4 zhang.
Multiply it by the height of 2 zhang, obtaining 800 cubic chi.
Multiply it by the length of 60 chi, obtaining 48000 cubic chi.
Divide it by 1000 cubic chi, obtaining the result.

The answer says: *a*(=48) units.
"""

# 下廣五丈
下廣 = 5

# 上廣三丈
上廣 = 3

# 高二丈
高 = 2

# 長六十尺
長 = 60

# 一千尺
單位 = 1000

# 并之，得八丈
總廣 = 上廣 + 下廣

# 半之，得四丈
平均廣 = 總廣 / 2

# 以二丈乘之，得八百尺
截面積 = 平均廣 * 高

# 以長六十尺乘之，得四萬八千
體積 = 截面積 * 長

# 以一千尺除之，即得
a = Fraction(體積, 單位) # 48
"""
Code error: both arguments should be Rational instances"""
