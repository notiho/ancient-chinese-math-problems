"""
今有地，長一千步，廣五百步，尺有鶉、寸有鷃。問鶉、鷃各幾何？
答曰：鶉 a ，鷃 b 。
"""

#----- content starts here -----
"""
Suppose there is a piece of land with a length of 1000 bu and a width of 500 bu. 
For every chi, there is a quail (鶉), and for every cun, there is a sparrow (鷃).
Question: how many quails (鶉) and sparrows (鷃) are there?

Answer: there are *a* quails and *b* sparrows.
"""

# 地的長和廣
長 = 1000  # in bu
廣 = 500   # in bu

# Convert bu to chi (1 bu = 6 chi)
長_in_chi = 長 * 6
廣_in_chi = 廣 * 6

# Calculate the total area in chi^2
面積_in_chi2 = 長_in_chi * 廣_in_chi

# For every chi^2, there is 1 quail (鶉)
a = 面積_in_chi2

# For every chi^2, there are 100 cun^2 (1 chi = 10 cun, so 1 chi^2 = 100 cun^2)
b = 面積_in_chi2 * 100

# Final result
a, b  # a = number of quails, b = number of sparrows#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 1000080000000, Actual: 1800000000"""
