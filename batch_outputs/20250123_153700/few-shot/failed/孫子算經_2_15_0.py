"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 。
"""

"""
Suppose there is a rope, 5794 bu long. It is desired to make it into a square.
Question: what is the side length?

The procedure says: Place the length of 5794 bu, divide it by 4, obtaining 1448 bu with a remainder of 2 bu.
Multiply the remainder by 6, obtaining 1 zhang and 2 chi.
Divide this by 4, obtaining 3 chi.
Combine all parts, and the result is obtained.

Answer: *a* bu.
"""

# 置長五千七百九十四步
總長 = 5794

# 以四除之，得一千四百四十八步，餘二步
整步 = 總長 // 4
餘步 = 總長 % 4

# 以六因之，得一丈二尺
餘尺 = 餘步 * 6  # 1步 = 6尺
丈 = 餘尺 // 10  # 1丈 = 10尺
尺 = 餘尺 % 10

# 以四除之，得三尺
尺 += 丈 * 10  # Convert 丈 to 尺
尺 = 尺 // 4  # Divide by 4 to get the remaining 尺

# 通計即得
a = 整步 + Fraction(尺, 10)  # Combine 整步 and fractional part in terms of bu
"""
Variable 'a' has wrong value. Expected: 2897/2, Actual: 14483/10"""
