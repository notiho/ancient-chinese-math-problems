"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a rope, 5794 bu in length. It is desired to make it into a square.
Question: what is the side length of the square?

The procedure says: Place the length of 5794 bu, divide it by 4, obtaining 1448 bu with a remainder of 2 bu.
Take the remainder and convert it into zhang and chi (1 zhang = 10 chi, 1 bu = 6 chi), obtaining 1 zhang and 2 chi.
Divide the chi by 4, obtaining 3 chi.
Combine all parts to get the total side length.

Answer: *a* bu.
"""

from fractions import Fraction

# 索長
索長 = 5794  # in bu

# 以四除之
整步 = 索長 // 4  # Integer division to get full bu
餘步 = 索長 % 4   # Remainder in bu

# 餘步以六因之 (convert remainder bu to chi, 1 bu = 6 chi)
餘尺 = 餘步 * 6  # in chi

# 得一丈二尺 (convert chi to zhang and chi, 1 zhang = 10 chi)
餘丈 = 餘尺 // 10  # Integer division to get full zhang
餘尺 = 餘尺 % 10   # Remaining chi

# 餘尺以四除之 (divide remaining chi by 4 to get fractional bu)
餘步_分數 = Fraction(餘尺, 4)  # Fractional bu from remaining chi

# 通計即得 (combine all parts)
a = 整步 + 餘步_分數  # Total side length in bu

a#----- content ends here -----

"""
"""
