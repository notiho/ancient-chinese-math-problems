"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a rope, 5794 bu long. It is desired to make it into a square.
Question: what is the side length of the square?

The procedure says: Place the length of 5794 bu, divide it by 4, obtaining 1448 bu with a remainder of 2 bu.
Convert the remainder into zhang and chi by multiplying it by 6, obtaining 1 zhang and 2 chi.
Divide the result by 4, obtaining 3 chi.
Combine the results to get the total side length.

Answer: *a* bu.
"""

from fractions import Fraction

# 索長五千七百九十四步
索長 = 5794

# 以四除之，得一千四百四十八步，餘二步
整步 = 索長 // 4
餘步 = 索長 % 4

# 以六因之，得一丈二尺
餘轉換 = 餘步 * 6  # 1步 = 6尺
餘丈 = 餘轉換 // 10  # 10尺 = 1丈
餘尺 = 餘轉換 % 10

# 以四除之，得三尺
餘尺除四 = Fraction(餘轉換, 4)

# 通計即得
a = 整步 + 餘尺除四  # Combine the whole steps and fractional steps

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2897/2, Actual: 1451"""
