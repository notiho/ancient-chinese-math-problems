"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a(=2897/2)步 。
"""

"""
Suppose there is a rope, 5794 bu long. It is desired to make it into a square.
Question: what is the side length?

The procedure says: Place the length, 5794 bu, and divide it by 4, obtaining 1448 bu with a remainder of 2 bu.
Multiply the remainder by 6, obtaining 1 zhang and 2 chi.
Divide this by 4, obtaining 3 chi.
Combine everything, and the result is obtained.

Answer: *a*(=2897/2) bu.
"""

# 索長五千七百九十四步
索長 = 5794

# 以四除之
商 = 索長 // 4
餘 = 索長 % 4

# 餘二步，以六因之
餘乘六 = 餘 * 6  # 2 * 6 = 12 chi = 1 zhang 2 chi

# 將餘乘六轉為尺
餘丈 = 餘乘六 // 10  # 1 zhang
餘尺 = 餘乘六 % 10  # 2 chi

# 以四除之
餘尺除四 = Fraction(餘丈 * 10 + 餘尺, 4)  # Convert zhang and chi to chi, then divide by 4

# 通計即得
a = 商 + 餘尺除四  # 1448 + 3 chi = 2897/2 bu
"""
Variable 'a' has wrong value. Expected: 2897/2, Actual: 1451"""
