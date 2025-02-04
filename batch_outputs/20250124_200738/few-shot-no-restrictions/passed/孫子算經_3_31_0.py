"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
術曰：置九百里以三百步乘之，得二十七萬步，又以六尺乘之，得一百六十二萬尺，以車輪一丈八尺為法，除之，即得。
答曰： a 匝。
"""

#----- content starts here -----
"""
Suppose the distance between Chang'an and Luoyang is 900 li. A single revolution of the cartwheel covers 1 zhang and 8 chi.
Question: How many revolutions does the wheel make to travel from Luoyang to Chang'an?

The procedure says: Take 900 li and multiply it by 300 bu (steps), obtaining 270,000 bu. Then multiply it by 6 chi, obtaining 1,620,000 chi. Use the cartwheel's circumference of 1 zhang and 8 chi as the divisor, and divide to obtain the number of revolutions.

Answer: *a* revolutions.
"""

from fractions import Fraction

# 長安、洛陽相去九百里
距離_里 = 900

# 1里 = 300步
步每里 = 300
距離_步 = 距離_里 * 步每里

# 1步 = 6尺
尺每步 = 6
距離_尺 = 距離_步 * 尺每步

# 車輪一匝一丈八尺
車輪_匝 = 1 * 10 + 8  # 1丈 = 10尺, so 1丈8尺 = 18尺

# 求輪匝數
a = Fraction(距離_尺, 車輪_匝)

# Output the result
a#----- content ends here -----

"""
"""
