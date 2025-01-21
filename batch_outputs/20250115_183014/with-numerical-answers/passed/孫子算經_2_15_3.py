"""
今有索，長五千七百九十四步。欲使作方。問：幾何？
術曰：置長五千七百九十四步，以四除之，得一千四百四十八步，餘二步，以六因之，得一丈二尺，以四除之，得三尺，通計即得。
答曰： a(=1448)步 b(=3)尺 。
"""

"""
Suppose there is a rope, 5794 bu long. It is desired to make it into a square.
Question: what are the dimensions?

The procedure says: Place the length of 5794 bu, divide it by 4, obtaining 1448 bu, with a remainder of 2 bu.
Multiply the remainder by 6, obtaining 1 zhang and 2 chi.
Divide this by 4, obtaining 3 chi.
Combine the results, and the total is obtained.

Answer: *a*(=1448) bu and *b*(=3) chi.
"""

# 索長五千七百九十四步
索長 = 5794

# 以四除之，得一千四百四十八步，餘二步
a = 索長 // 4  # 1448 步
餘步 = 索長 % 4  # 2 步

# 以六因之，得一丈二尺
餘尺 = 餘步 * 6  # 12 尺 = 1 丈 2 尺

# 以四除之，得三尺
b = 餘尺 // 4  # 3 尺
"""
"""
