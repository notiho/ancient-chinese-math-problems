"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
術曰：置九百里以三百步乘之，得二十七萬步，又以六尺乘之，得一百六十二萬尺，以車輪一丈八尺為法，除之，即得。
答曰： a(=90000) 匝。
"""

#----- content starts here -----
"""
Suppose the distance between Chang'an and Luoyang is 900 li. A cartwheel completes one revolution in 1 zhang and 8 chi.
It is desired to calculate how many revolutions the wheel makes when traveling from Luoyang to Chang'an.

The procedure says: Place 900 li and multiply it by 300 bu, obtaining 270,000 bu. Then multiply it by 6 chi, obtaining 1,620,000 chi.
Take the cartwheel's circumference of 1 zhang and 8 chi as the divisor, and divide, obtaining the number of revolutions.

Answer: *a*(=90,000) revolutions.
"""

# 長安、洛陽相去九百里
里 = 900

# 一里等於三百步
步每里 = 300

# 一步等於六尺
尺每步 = 6

# 車輪一匝一丈八尺
車輪匝 = 1 * 10 + 8  # 1丈 = 10尺, so 1丈8尺 = 18尺

# 置九百里以三百步乘之，得二十七萬步
總步 = 里 * 步每里

# 又以六尺乘之，得一百六十二萬尺
總尺 = 總步 * 尺每步

# 以車輪一丈八尺為法，除之，即得
a = Fraction(總尺, 車輪匝)  # 90,000 匝#----- content ends here -----

"""
"""
