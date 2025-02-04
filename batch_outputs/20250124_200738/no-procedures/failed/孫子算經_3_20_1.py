"""
今有地，長一千步，廣五百步，尺有鶉、寸有鷃。問鶉、鷃各幾何？
答曰：鶉 a ，鷃 b 。
"""

#----- content starts here -----
"""
Suppose there is a piece of land with a length of 1000 bu and a width of 500 bu.
Each chi contains quails (鶉), and each cun contains sparrows (鷃).
Question: how many quails (鶉) and sparrows (鷃) are there in total?

Answer: there are *a* quails and *b* sparrows.
"""

# 地的長和廣
長 = 1000  # in bu
廣 = 500   # in bu

# 1 bu = 6 chi, and 1 chi = 10 cun
chi_per_bu = 6
cun_per_chi = 10

# Calculate total area in chi^2
total_chi_squared = 長 * 廣 * chi_per_bu**2

# Each chi contains 1 quail (鶉), so the total number of quails is equal to the total chi^2
a = total_chi_squared

# Each chi contains 10 cun, and each cun contains 1 sparrow (鷃)
# Total sparrows = total chi^2 * cun_per_chi
b = total_chi_squared * cun_per_chi

# Final results
a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 1000080000000, Actual: 180000000"""
