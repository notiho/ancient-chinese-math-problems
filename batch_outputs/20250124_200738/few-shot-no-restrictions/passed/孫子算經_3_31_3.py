"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
術曰：置九百里以三百步乘之，得二十七萬步，又以六尺乘之，得一百六十二萬尺，以車輪一丈八尺為法，除之，即得。
答曰： a 匝。
"""

#----- content starts here -----
"""
Suppose the distance between Chang'an and Luoyang is 900 li, and the circumference of a wheel is 1 zhang and 8 chi.
If one wishes to travel from Luoyang to Chang'an, how many wheel revolutions are required?

The procedure says: Place 900 li and multiply it by 300 bu, obtaining 270,000 bu.
Then multiply it by 6 chi, obtaining 1,620,000 chi.
Use the wheel circumference of 1 zhang and 8 chi as the divisor, and divide it to obtain the result.

Answer: *a* revolutions.
"""

from fractions import Fraction

# 長安、洛陽相去九百里
距離里 = 900

# 1 里 = 300 步
距離步 = 距離里 * 300

# 1 步 = 6 尺
距離尺 = 距離步 * 6

# 車輪一匝一丈八尺
車輪匝 = 1 * 10 + 8  # 1 丈 = 10 尺, so 1 丈 8 尺 = 18 尺

# 輪匝幾何？
a = Fraction(距離尺, 車輪匝)

a#----- content ends here -----

"""
"""
