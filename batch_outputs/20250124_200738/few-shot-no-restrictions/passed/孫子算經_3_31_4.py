"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
術曰：置九百里以三百步乘之，得二十七萬步，又以六尺乘之，得一百六十二萬尺，以車輪一丈八尺為法，除之，即得。
答曰： a 匝。
"""

#----- content starts here -----
"""
Suppose the distance between Chang'an and Luoyang is 900 li. A single rotation of a cartwheel covers 1 zhang and 8 chi.
Question: how many rotations does the wheel make to travel from Luoyang to Chang'an?

The procedure says: Take 900 li and multiply it by 300 bu, obtaining 270,000 bu. Then multiply it by 6 chi, obtaining 1,620,000 chi. 
Use the cartwheel's circumference of 1 zhang and 8 chi as the divisor. Divide to obtain the number of rotations.

Answer: *a* rotations.
"""

from fractions import Fraction

# 長安、洛陽相去九百里
距離里 = 900

# 一里 = 300 步
步每里 = 300
距離步 = 距離里 * 步每里

# 一步 = 6 尺
尺每步 = 6
距離尺 = 距離步 * 尺每步

# 車輪一匝一丈八尺
車輪周長 = 1 * 10 + 8  # 1 丈 = 10 尺, so 1 丈 8 尺 = 18 尺

# 以車輪周長為法，除之
a = Fraction(距離尺, 車輪周長)

# Output the result
a#----- content ends here -----

"""
"""
