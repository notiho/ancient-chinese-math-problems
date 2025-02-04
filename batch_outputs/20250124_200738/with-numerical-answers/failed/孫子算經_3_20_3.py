"""
今有地，長一千步，廣五百步，尺有鶉、寸有鷃。問鶉、鷃各幾何？
術曰：置長一千步，以廣五百步乘之，得五十萬；以三十六乘之，得一千八百萬尺，即得鶉數；上十之，即得鷃數。
答曰：鶉 a(=18000000) ，鷃 b(=1000080000000) 。
"""

#----- content starts here -----
"""
Suppose there is a piece of land, 1000 bu in length and 500 bu in width. 
Each chi contains quails (鶉), and each cun contains sparrows (鷃).
Question: how many quails (鶉) and sparrows (鷃) are there?

The procedure says: Place the length of 1000 bu, multiply it by the width of 500 bu, obtaining 500,000.
Multiply this by 36, obtaining 18,000,000 chi, which is the number of quails (鶉).
Multiply this by 10, obtaining the number of sparrows (鷃).

Answer: *a*(=18,000,000) quails (鶉), *b*(=1,000,080,000,000) sparrows (鷃).
"""

# 長一千步
長 = 1000

# 廣五百步
廣 = 500

# 置長一千步，以廣五百步乘之，得五十萬
積步 = 長 * 廣

# 以三十六乘之，得一千八百萬尺，即得鶉數
鶉 = 積步 * 36

# 上十之，即得鷃數
鷃 = 鶉 * 10

a = 鶉 # 18,000,000
b = 鷃 # 1,000,080,000,000#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 1000080000000, Actual: 180000000"""
