"""
今有長安洛陽相去九百里車輪一匝一丈八尺欲自洛陽至長安問輪匝幾何
術曰置九百里以三百步乘之得二十七萬步又以六尺乘之得一百六十二萬尺以車輪一丈八尺為法除之即得
答曰 a 匝
"""

#----- content starts here -----
"""
Suppose the distance between Chang'an and Luoyang is 900 li. A single revolution of a cartwheel covers 1 zhang and 8 chi.
Question: how many revolutions does the wheel make to travel from Luoyang to Chang'an?

The procedure says: Place 900 li, multiply it by 300 bu, obtaining 270,000 bu.
Then multiply it by 6 chi, obtaining 1,620,000 chi.
Take the cartwheel's 1 zhang and 8 chi as the divisor, and divide it, obtaining the number of revolutions.

The answer says: *a* revolutions.
"""

# 長安洛陽相去九百里
距離里 = 900

# 一里等於三百步
步每里 = 300

# 一步等於六尺
尺每步 = 6

# 車輪一匝一丈八尺
車輪匝 = 1 * 10 + 8  # 1丈 = 10尺, 所以1丈8尺 = 18尺

# 置九百里，以三百步乘之，得二十七萬步
距離步 = 距離里 * 步每里

# 又以六尺乘之，得一百六十二萬尺
距離尺 = 距離步 * 尺每步

# 以車輪一丈八尺為法除之，即得
a = Fraction(距離尺, 車輪匝)  # 匝數#----- content ends here -----

"""
"""
