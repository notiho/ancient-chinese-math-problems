"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
術曰：置堤，上廣三丈，下廣五丈。并之，得八丈；半之，得四丈。以二丈乘之，得八百尺；以長六十尺乘之，得四萬八千；以一千尺除之，即得。
答曰： a 方。
"""

#----- content starts here -----
"""
Suppose there is an embankment. Its bottom width is 5 zhang, its top width is 3 zhang, its height is 2 zhang, and its length is 60 chi. 
It is desired to calculate how many units of 1000 cubic chi can be made from this embankment.

The procedure says: Place the embankment. The top width is 3 zhang, and the bottom width is 5 zhang. Add them, obtaining 8 zhang. Halve it, obtaining 4 zhang.
Multiply this by the height of 2 zhang, obtaining 800 chi². Multiply this by the length of 60 chi, obtaining 48000 chi³.
Divide this by 1000 chi³, and the result is the number of units.

Answer: *a* units.
"""

from fractions import Fraction

# 下廣五丈
下廣 = 5  # in zhang

# 上廣三丈
上廣 = 3  # in zhang

# 高二丈
高 = 2  # in zhang

# 長六十尺
長 = 60  # in chi

# 一丈 = 10 尺
# Convert widths and height to chi
下廣_尺 = 下廣 * 10
上廣_尺 = 上廣 * 10
高_尺 = 高 * 10

# 并之，得八丈；半之，得四丈
平均廣_尺 = (下廣_尺 + 上廣_尺) / 2

# 以二丈乘之，得八百尺
橫截面積_尺平方 = 平均廣_尺 * 高_尺

# 以長六十尺乘之，得四萬八千
體積_尺立方 = 橫截面積_尺平方 * 長

# 以一千尺除之，即得
a = Fraction(體積_尺立方, 1000)

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
