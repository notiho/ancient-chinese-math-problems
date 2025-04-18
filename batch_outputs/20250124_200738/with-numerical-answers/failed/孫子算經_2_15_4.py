"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a(=2897/2)步 。
"""

#----- content starts here -----
"""
Suppose there is a rope with a length of 5794 bu. It is desired to make it into a square.
Question: what is the side length?

The procedure says: Place the length of 5794 bu, divide it by 4, obtaining 1448 bu with a remainder of 2 bu.
Multiply the remainder by 6, obtaining 1 zhang and 2 chi.
Divide it by 4, obtaining 3 chi.
Combine everything, and the result is obtained.

Answer: *a*(=2897/2) bu.
"""

from fractions import Fraction

# 索長五千七百九十四步
索長 = 5794

# 以四除之
整步 = 索長 // 4  # 得一千四百四十八步
餘步 = 索長 % 4   # 餘二步

# 以六因之
餘步換算 = 餘步 * 6  # 得一丈二尺
餘丈 = 餘步換算 // 10  # 一丈
餘尺 = 餘步換算 % 10   # 二尺

# 以四除之
餘尺換算 = Fraction(餘丈 * 10 + 餘尺, 4)  # 得三尺

# 通計即得
a = 整步 + 餘尺換算  # 2897/2 bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2897/2, Actual: 1451"""
