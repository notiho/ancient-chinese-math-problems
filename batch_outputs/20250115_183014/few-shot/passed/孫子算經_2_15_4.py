"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a步 b尺 。
"""

"""
Suppose there is a rope, 5794 bu long. It is desired to make it into a square.
Question: what are the dimensions?

The procedure says: Place the length of 5794 bu, divide it by 4, obtaining 1448 bu with a remainder of 2 bu.
Multiply the remainder by 6, obtaining 1 zhang and 2 chi.
Divide it by 4, obtaining 3 chi.
Combine all parts to calculate the result.

Answer: *a* bu and *b* chi.
"""

# 索長五千七百九十四步
索長 = 5794

# 以四除之，得一千四百四十八步，餘二步
整步 = 索長 // 4
餘步 = 索長 % 4

# 以六因之，得一丈二尺
餘尺 = 餘步 * 6  # 1丈 = 10尺
丈 = 餘尺 // 10
尺 = 餘尺 % 10

# 以四除之，得三尺
尺 += 丈 * 10
尺 = 尺 // 4

# 通計即得
a = 整步
b = 尺
"""
"""
