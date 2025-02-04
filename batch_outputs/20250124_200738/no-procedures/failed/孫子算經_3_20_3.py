"""
今有地，長一千步，廣五百步，尺有鶉、寸有鷃。問鶉、鷃各幾何？
答曰：鶉 a ，鷃 b 。
"""

#----- content starts here -----
"""
Suppose there is a piece of land, with a length of 1000 bu and a width of 500 bu. 
Each chi contains quails (鶉), and each cun contains sparrows (鷃).
Question: how many quails (鶉) and sparrows (鷃) are there in total?

Answer: there are *a* quails (鶉) and *b* sparrows (鷃).
"""

# 地的長和廣
長 = 1000  # in bu
廣 = 500   # in bu

# 1 bu = 6 chi, and 1 chi = 10 cun
# Total area in chi^2
面積_in_尺平方 = 長 * 廣 * 6 * 6

# Total area in cun^2
面積_in_寸平方 = 面積_in_尺平方 * 10 * 10

# 鶉 corresponds to chi^2
a = 面積_in_尺平方

# 鷃 corresponds to cun^2
b = 面積_in_寸平方#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 1000080000000, Actual: 1800000000"""
