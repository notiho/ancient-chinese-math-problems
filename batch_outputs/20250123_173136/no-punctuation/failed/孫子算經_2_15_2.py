"""
今有索長五千七百九十四步欲使作方問幾何
術曰置長五千七百九十四步以四除之得一千四百四十八步餘二步以六因之得一丈二尺以四除之得三尺通計即得
答曰 a步 
"""

"""
Suppose there is a rope 5794 bu long. It is desired to make it into a square.
Question: what is the side length of the square?

The procedure says: Place the length of 5794 bu. Divide it by 4, obtaining 1448 bu with a remainder of 2 bu.
Multiply the remainder by 6, obtaining 1 zhang and 2 chi.
Divide the 2 chi by 4, obtaining 3 cun.
Combine all parts, and the total is the side length.

Answer: *a* bu.
"""

# 置長五千七百九十四步
長 = 5794

# 以四除之，得一千四百四十八步餘二步
步 = 長 // 4
餘步 = 長 % 4

# 以六因之，得一丈二尺
餘尺 = 餘步 * 6
丈 = 餘尺 // 10
尺 = 餘尺 % 10

# 以四除之，得三尺
寸 = 尺 * 10 // 4

# 通計即得
a = Fraction(步) + Fraction(丈, 10) + Fraction(尺, 10) + Fraction(寸, 100)
"""
Variable 'a' has wrong value. Expected: 2897/2, Actual: 28967/20"""
