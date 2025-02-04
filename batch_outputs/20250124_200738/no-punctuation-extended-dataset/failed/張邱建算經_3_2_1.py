"""
今有垣髙一丈三尺五寸材長二丈二尺五寸倚之於垣末與垣齊問引材却行幾何材末至地
術曰垣髙自乘以減材長自乘餘以開方除之所得以減材餘即却行尺數
答曰 a尺
"""

#----- content starts here -----
"""
Suppose there is a wall with a height of 1 zhang, 3 chi, and 5 cun. A beam with a length of 2 zhang, 2 chi, and 5 cun leans against the wall, with its top end flush with the top of the wall.
Question: how far must the base of the beam be moved away from the wall (the horizontal distance to the wall)?

The procedure says: Multiply the height of the wall by itself. Subtract this from the square of the length of the beam.
Take the square root of the remainder and divide it. Subtract the result from the remaining length of the beam.
This gives the number of chi for the horizontal distance.

Answer: *a* chi.
"""

# 垣髙一丈三尺五寸
垣髙 = 1 * 10 + 3 + Fraction(5, 10)  # Convert to chi

# 材長二丈二尺五寸
材長 = 2 * 10 + 2 + Fraction(5, 10)  # Convert to chi

# 垣髙自乘
垣髙平方 = 垣髙 * 垣髙

# 材長自乘
材長平方 = 材長 * 材長

# 以減材長自乘
餘 = 材長平方 - 垣髙平方

# 餘以開方
引材 = Fraction(餘).sqrt()

# 所得以減材餘
a = 引材  # Horizontal distance in chi#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
