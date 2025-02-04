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
Take the remainder of 2 bu, convert it into zhang and chi (6 bu = 1 zhang, 10 chi = 1 zhang), obtaining 1 zhang and 2 chi.
Divide the chi by 4, obtaining 3 chi.
Combine all the results to obtain the total side length.

Answer: *a* bu.
"""

from fractions import Fraction

# 索長
索長 = 5794  # in bu

# 以四除之
整步 = 索長 // 4  # integer part in bu
餘步 = 索長 % 4  # remainder in bu

# 餘步以六因之 (6 bu = 1 zhang)
餘丈 = 餘步 // 6  # integer part in zhang
餘尺 = 餘步 % 6  # remainder in chi (1 bu = 6 chi)

# 餘尺以四除之 (divide chi by 4)
餘尺 = Fraction(餘尺, 4)  # fractional chi

# Combine results
a = 整步 + Fraction(餘丈, 10) + Fraction(餘尺, 10)  # total side length in bu

a  # Final answer in bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2897/2, Actual: 28961/20"""
