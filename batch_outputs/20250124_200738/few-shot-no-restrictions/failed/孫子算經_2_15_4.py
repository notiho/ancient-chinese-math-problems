"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a rope, 5794 bu long. It is desired to make it into a square.
Question: what is the side length of the square?

The procedure says: Place the length of 5794 bu and divide it by 4, obtaining 1448 bu with a remainder of 2 bu.
Convert the remainder into zhang and chi by multiplying it by 6, obtaining 1 zhang and 2 chi.
Divide the 2 chi by 4, obtaining 3 cun.
Combine all the results to get the total side length.

Answer: *a* bu.
"""

from fractions import Fraction

# 索長
索長 = 5794  # in bu

# 以四除之
整步 = 索長 // 4  # 整數部分 in bu
餘步 = 索長 % 4  # 餘數部分 in bu

# 餘數以六因之
餘數轉換 = 餘步 * 6  # 餘數轉換為 zhang and chi
餘數_丈 = 餘數轉換 // 10  # 1 zhang = 10 chi
餘數_尺 = 餘數轉換 % 10  # 剩餘 chi

# 餘數_尺以四除之
餘數_尺轉換 = Fraction(餘數_尺, 4)  # 轉換為 cun

# 通計
a = 整步 + 餘數_丈 + Fraction(餘數_尺轉換, 10)  # 最終結果 in bu

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2897/2, Actual: 28981/20"""
