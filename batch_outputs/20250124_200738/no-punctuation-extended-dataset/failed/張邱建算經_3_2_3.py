"""
今有垣髙一丈三尺五寸材長二丈二尺五寸倚之於垣末與垣齊問引材却行幾何材末至地
術曰垣髙自乘以減材長自乘餘以開方除之所得以減材餘即却行尺數
答曰 a尺
"""

#----- content starts here -----
"""
Suppose there is a wall with a height of 1 zhang, 3 chi, and 5 cun. A beam with a length of 2 zhang, 2 chi, and 5 cun is leaned against the wall, with the top of the beam flush with the top of the wall.
Question: how far must the base of the beam be pulled back from the wall (horizontal distance)?

The procedure says: Multiply the height of the wall by itself. Subtract this from the square of the length of the beam. Take the square root of the remainder and divide it. Subtract the result from the remainder of the beam. This gives the number of chi for the horizontal distance.

Answer: *a* chi.
"""

# 垣髙一丈三尺五寸
垣髙 = 1 * 10 + 3 + Fraction(5, 10)

# 材長二丈二尺五寸
材長 = 2 * 10 + 2 + Fraction(5, 10)

# 垣髙自乘
垣髙平方 = 垣髙 * 垣髙

# 材長自乘
材長平方 = 材長 * 材長

# 以減材長自乘
餘 = 材長平方 - 垣髙平方

# 開方 (平方根)
# Since Python does not have a built-in square root for fractions, we approximate it manually.
# This is a simplified manual square root approximation for the sake of the problem.
def 開方(數):
    x = 數
    guess = x / 2
    while abs(guess * guess - x) > Fraction(1, 1000):  # Precision threshold
        guess = (guess + x / guess) / 2
    return guess

水平距離 = 開方(餘)

# 即却行尺數
a = 水平距離
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/2, Actual: 1084202853050238275884379727619156574962204162/60233416217820588451695881895595935993853241"""
