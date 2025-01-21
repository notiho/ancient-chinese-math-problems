"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
術曰：置堤，上廣三丈，下廣五丈。并之，得八丈；半之，得四丈。以二丈乘之，得八百尺；以長六十尺乘之，得四萬八千；以一千尺除之，即得。
答曰： a 方。
"""

"""
Suppose there is a dike. Its bottom width is 5 zhang, its top width is 3 zhang, its height is 2 zhang, and its length is 60 chi.
It is desired to calculate how many 1000 chi³ blocks can be made from it.

The procedure says: Place the dike, with the top width of 3 zhang and the bottom width of 5 zhang.
Add them together, obtaining 8 zhang. Halve it, obtaining 4 zhang.
Multiply it by the height of 2 zhang, obtaining 8 zhang² (800 chi²).
Multiply it by the length of 60 chi, obtaining 48000 chi³.
Divide it by 1000 chi³, obtaining the result.

The answer says: *a* blocks.
"""

# 下廣五丈
下廣 = 5

# 上廣三丈
上廣 = 3

# 高二丈
高 = 2

# 長六十尺
長 = 60

# 一丈 = 10尺
下廣 = 下廣 * 10
上廣 = 上廣 * 10
高 = 高 * 10

# 并之，得八丈；半之，得四丈
平均廣 = (下廣 + 上廣) / 2

# 以二丈乘之，得八百尺
橫截面積 = 平均廣 * 高

# 以長六十尺乘之，得四萬八千
體積 = 橫截面積 * 長

# 以一千尺除之，即得
a = Fraction(體積, 1000)
"""
Code error: both arguments should be Rational instances"""
