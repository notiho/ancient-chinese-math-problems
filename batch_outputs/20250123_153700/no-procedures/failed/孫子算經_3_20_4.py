"""
今有地，長一千步，廣五百步，尺有鶉、寸有鷃。問鶉、鷃各幾何？
答曰：鶉 a ，鷃 b 。
"""

"""
Suppose there is a piece of land with a length of 1000 bu and a width of 500 bu. 
Each chi contains quails (鶉), and each cun contains sparrows (鷃). 
Question: how many quails (鶉) and sparrows (鷃) are there in total?

Answer: quails (鶉) = *a*, sparrows (鷃) = *b*.
"""

# 地的長和廣
長 = 1000  # in bu
廣 = 500   # in bu

# 1 bu = 6 chi, 1 chi = 10 cun
chi_per_bu = 6
cun_per_chi = 10

# 計算總面積（以 bu 為單位）
總面積_bu = 長 * 廣

# 將面積轉換為 chi 和 cun
總面積_chi = 總面積_bu * chi_per_bu
總面積_cun = 總面積_chi * cun_per_chi

# 鶉（每 chi 一個）
a = 總面積_chi

# 鷃（每 cun 一個）
b = 總面積_cun

a, b  # Output the results
"""
Variable 'a' has wrong value. Expected: 18000000, Actual: 3000000
Variable 'b' has wrong value. Expected: 1000080000000, Actual: 30000000"""
