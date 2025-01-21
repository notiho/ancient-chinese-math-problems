"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a(=1448)步 b(=3)尺 。
"""

"""
Suppose there is a rope, 5794 bu in length. It is desired to make it into a square.
Question: what is the side length?

The procedure says: Place the length of 5794 bu, divide it by 4, obtaining 1448 bu with a remainder of 2 bu.
Multiply the remainder by 6, obtaining 1 zhang and 2 chi.
Divide it by 4, obtaining 3 chi.
Combine everything, and the result is obtained.

Answer: *a*(=1448) bu and *b*(=3) chi.
"""

# 索長五千七百九十四步
索長 = 5794

# 以四除之
商 = 索長 // 4
餘 = 索長 % 4

# 餘二步，以六因之
餘步 = 餘 * 6

# 得一丈二尺
丈 = 餘步 // 10
尺 = 餘步 % 10

# 以四除之
尺 = 尺 // 4

# 通計即得
a = 商  # 1448 步
b = 尺  # 3 尺
"""
Variable 'b' has wrong value. Expected: 3, Actual: 0"""
