"""
今有地長一千步廣五百步尺有鶉寸有鷃問鶉鷃各幾何
術曰置長一千步以廣五百步乘之得五十萬以三十六乘之得一千八百萬尺即得鶉數上十之即得鷃數
答曰鶉 a 鷃 b 
"""

"""
Suppose there is a piece of land with a length of 1000 bu and a width of 500 bu.
Each bu has 36 chi, and each chi has 10 cun.
Question: how many chi (quail units, 鶉) and cun (sparrow units, 鷃) are there?

The procedure says: Place the length of 1000 bu, multiply it by the width of 500 bu, obtaining 500,000.
Multiply this by 36, obtaining 18,000,000 chi, which gives the number of quail units (鶉).
Multiply this by 10, which gives the number of sparrow units (鷃).

Answer: *a* quail units (chi), *b* sparrow units (cun).
"""

# 置長一千步
長 = 1000

# 廣五百步
廣 = 500

# 以廣五百步乘之，得五十萬
面積步 = 長 * 廣

# 以三十六乘之，得一千八百萬尺，即得鶉數
鶉 = 面積步 * 36

# 上十之，即得鷃數
鷃 = 鶉 * 10

a = 鶉
b = 鷃
"""
Variable 'b' has wrong value. Expected: 1000080000000, Actual: 180000000"""
