"""
今有地，長一千步，廣五百步，尺有鶉、寸有鷃。問鶉、鷃各幾何？
術曰：置長一千步，以廣五百步乘之，得五十萬；以三十六乘之，得一千八百萬尺，即得鶉數；上十之，即得鷃數。
答曰：鶉 a ，鷃 b 。
"""

#----- content starts here -----
"""
Suppose there is a piece of land with a length of 1000 bu and a width of 500 bu. 
Each chi contains quails (鶉), and each cun contains sparrows (鷃). 
Question: how many quails and sparrows are there?

The procedure says: Place the length of 1000 bu and multiply it by the width of 500 bu, obtaining 500,000.
Multiply this by 36, obtaining 18,000,000 chi, which is the number of quails (鶉).
Multiply this by 10, obtaining the number of sparrows (鷃).

Answer: quails *a*, sparrows *b*.
"""

# 長一千步
長 = 1000

# 廣五百步
廣 = 500

# 每步36尺
步到尺 = 36

# 每尺10寸
尺到寸 = 10

# 置長一千步，以廣五百步乘之，得五十萬
面積步 = 長 * 廣

# 以三十六乘之，得一千八百萬尺，即得鶉數
鶉 = 面積步 * 步到尺

# 上十之，即得鷃數
鷃 = 鶉 * 尺到寸

a = 鶉
b = 鷃#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 1000080000000, Actual: 180000000"""
