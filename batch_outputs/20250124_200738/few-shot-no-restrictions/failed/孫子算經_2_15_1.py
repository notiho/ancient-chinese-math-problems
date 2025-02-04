"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a rope, 5794 bu long. It is desired to make it into a square.
Question: what is the side length of the square?

The procedure says: Place the length, 5794 bu, and divide it by 4. 
The quotient is 1448 bu, with a remainder of 2 bu. 
Convert the remainder into zhang and chi by multiplying it by 6, obtaining 1 zhang and 2 chi. 
Divide the chi by 4, obtaining 3 chi. Combine all parts to get the total side length.

Answer: *a* bu.
"""

from fractions import Fraction

# 索長
索長 = 5794  # in bu

# 以四除之
整步 = 索長 // 4  # Quotient in bu
餘步 = 索長 % 4  # Remainder in bu

# 餘二步，以六因之
餘丈 = 餘步 * 6  # Convert remainder to zhang and chi
餘丈整 = 餘丈 // 10  # Whole zhang
餘尺 = 餘丈 % 10  # Remaining chi

# 餘尺以四除之
餘尺整 = 餘尺 // 4  # Whole chi
餘尺分 = Fraction(餘尺 % 4, 4)  # Fractional chi

# 通計即得
a = 整步 + 餘丈整 + Fraction(餘尺整, 10) + Fraction(餘尺分, 10)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2897/2, Actual: 28981/20"""
