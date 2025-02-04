"""
今有登山望樓樓在平地偃矩山上令句高六尺從句端斜望樓足入下股一丈二尺又設重矩于上令其間相去三丈更從句端斜望樓足入上股一丈一尺四寸又立小表于入股之會復從句端斜望樓岑端入小表八寸問樓高幾何
術曰上下股相減餘為法置矩閒以下股乘之如句高而一所得以入小表乘之為實實如法而一即是樓高
答曰 a丈 
"""

"""
Suppose there is a mountain, and from the mountain, one looks at a tower that is on flat ground.
A right triangle is formed on the mountain, with the vertical leg (the "ju") being 6 chi tall.
From the top of the vertical leg, the hypotenuse is extended to the base of the tower, intersecting the horizontal leg (the "gu") at 1 zhang and 2 chi.
Another right triangle is constructed above the first, with the distance between the two triangles being 3 zhang.
From the top of the second vertical leg, the hypotenuse intersects the horizontal leg at 1 zhang, 1 chi, and 4 cun.
A small pole is erected at the intersection of the horizontal legs, and from the top of the second vertical leg, the hypotenuse intersects the top of the small pole at 8 cun.
Question: how tall is the tower?

The procedure says: Subtract the upper horizontal leg from the lower horizontal leg. The remainder is the divisor.
Place the distance between the two triangles and multiply it by the lower horizontal leg. Treat it as the vertical leg.
Divide the result by the small pole's height to obtain the dividend.
Divide the dividend by the divisor to obtain the tower's height.

Answer: the tower is *a* zhang tall.
"""

# 句高六尺
句高 = 6  # in chi

# 下股一丈二尺
下股 = 1 * 10 + 2  # convert to chi

# 矩間三丈
矩間 = 3 * 10  # convert to chi

# 上股一丈一尺四寸
上股 = 1 * 10 + 1 + Fraction(4, 10)  # convert to chi

# 小表八寸
小表 = Fraction(8, 10)  # convert to chi

# 上下股相減，餘為法
法 = 下股 - 上股

# 置矩閒以下股乘之，如句高而一
實1 = 矩間 * 下股 / 句高

# 所得以入小表乘之，為實
實2 = 實1 * 小表

# 實如法而一，即是樓高
樓高 = 實2 / 法

# Convert the result to zhang
a = Fraction(樓高, 10)  # convert chi to zhang
"""
Code error: both arguments should be Rational instances"""
