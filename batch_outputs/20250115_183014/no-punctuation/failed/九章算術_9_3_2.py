"""
今有圓材徑二尺五寸欲為方版令厚七寸問廣幾何
術曰令徑二尺五寸自乘以七寸自乘減之其餘開方除之即廣
荅曰 a尺 
"""

"""
Suppose there is a cylindrical log with a diameter of 2 chi and 5 cun. It is desired to make square planks with a thickness of 7 cun.
Question: how wide should the planks be?

The procedure says: Take the diameter of 2 chi and 5 cun, square it. Take the thickness of 7 cun, square it, and subtract it from the previous result. Take the square root of the remainder and divide it, obtaining the width.

The answer says: *a* chi.
"""

# 圓材徑二尺五寸
徑 = 2 + Fraction(5, 10)  # 2 chi and 5 cun (1 chi = 10 cun)

# 厚七寸
厚 = Fraction(7, 10)  # 7 cun (converted to chi)

# 令徑二尺五寸自乘
徑平方 = 徑 * 徑

# 以七寸自乘
厚平方 = 厚 * 厚

# 減之
餘 = 徑平方 - 厚平方

# 其餘開方
廣 = Fraction(餘).sqrt()

# 即廣
a = 廣
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
