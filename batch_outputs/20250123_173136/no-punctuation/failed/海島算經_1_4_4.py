"""
今有登山望樓樓在平地偃矩山上令句高六尺從句端斜望樓足入下股一丈二尺又設重矩于上令其間相去三丈更從句端斜望樓足入上股一丈一尺四寸又立小表于入股之會復從句端斜望樓岑端入小表八寸問樓高幾何
術曰上下股相減餘為法置矩閒以下股乘之如句高而一所得以入小表乘之為實實如法而一即是樓高
答曰 a丈 
"""

"""
Suppose there is a mountain, and from the mountain, one observes a tower. The tower is on flat ground, and the observer uses a horizontal measuring instrument ("偃矩") on the mountain. The height of the instrument's vertical leg ("句") is 6 chi. From the top of the vertical leg, the observer looks diagonally at the base of the tower, and the diagonal line intersects the lower horizontal leg ("股") at 1 zhang and 2 chi. Then, another horizontal measuring instrument is set up 3 zhang away from the first, and from the top of its vertical leg, the observer again looks diagonally at the base of the tower, intersecting the upper horizontal leg at 1 zhang, 1 chi, and 4 cun. A small pole ("小表") is erected at the intersection point of the horizontal leg, and from the top of the vertical leg, the observer looks diagonally at the top of the tower, intersecting the small pole at 8 cun. Question: What is the height of the tower?

The procedure says: Subtract the upper horizontal leg from the lower horizontal leg; the remainder is the divisor. Place the distance between the two measuring instruments and multiply it by the lower horizontal leg. Treat it as the vertical leg's height. Multiply the result by the small pole's intersection point to get the dividend. Divide the dividend by the divisor to get the height of the tower.

Answer: *a* zhang.
"""

# 句高六尺
句高 = 6

# 下股一丈二尺
下股 = 1 * 10 + 2

# 矩間相去三丈
矩間 = 3 * 10

# 上股一丈一尺四寸
上股 = 1 * 10 + 1 + Fraction(4, 10)

# 入小表八寸
入小表 = Fraction(8, 10)

# 上下股相減，餘為法
法 = 下股 - 上股

# 置矩閒以下股乘之，如句高而一
實1 = 矩間 * 下股 / 句高

# 所得以入小表乘之，為實
實2 = 實1 * 入小表

# 實如法而一，即是樓高
樓高 = Fraction(實2, 法)

# Convert to zhang
a = Fraction(樓高, 10)  # Convert chi to zhang
"""
Code error: both arguments should be Rational instances"""
