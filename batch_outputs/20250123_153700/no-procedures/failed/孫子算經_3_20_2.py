"""
今有地，長一千步，廣五百步，尺有鶉、寸有鷃。問鶉、鷃各幾何？
答曰：鶉 a ，鷃 b 。
"""

"""
Suppose there is a piece of land, 1000 bu in length and 500 bu in width. Each chi (foot) contains quails (鶉), and each cun (inch) contains sparrows (鷃).
Question: how many quails (鶉) and sparrows (鷃) are there in total?

Answer: there are *a* quails and *b* sparrows.
"""

# 地的長和廣
長 = 1000  # in bu
廣 = 500   # in bu

# 1 bu = 6 chi (feet), and 1 chi = 10 cun (inches)
# Total area in chi^2
總尺平方 = 長 * 廣 * 6 * 6

# 鶉 (quails) per chi^2
鶉每尺平方 = 1

# 鷃 (sparrows) per cun^2
鷃每寸平方 = 1

# Total quails (鶉)
a = 總尺平方 * 鶉每尺平方

# Total sparrows (鷃)
# Note: 1 chi^2 = 100 cun^2
b = 總尺平方 * 100 * 鷃每寸平方

a, b  # Output the results
"""
Variable 'b' has wrong value. Expected: 1000080000000, Actual: 1800000000"""
