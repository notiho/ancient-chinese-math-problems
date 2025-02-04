"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a(=8)丈 。
"""

#----- content starts here -----
"""
Suppose there is a mountain, and a tower is visible from the mountain. The tower is on flat ground.
A carpenter's square is placed on the mountain such that the vertical leg (the "ju") is 6 chi high.
From the top of the vertical leg, a diagonal line is drawn to the base of the tower, intersecting the horizontal leg (the "gu") at 1 zhang 2 chi.
Another carpenter's square is placed above the first, with a distance of 3 zhang between them.
From the top of the second vertical leg, a diagonal line is drawn to the base of the tower, intersecting the horizontal leg at 1 zhang 1 chi 4 cun.
A small pole is erected at the intersection of the horizontal legs, and from the top of the second vertical leg, a diagonal line is drawn to the top of the tower, intersecting the small pole at 8 cun.
Question: how tall is the tower?

The procedure says: Subtract the upper horizontal leg from the lower horizontal leg, and the remainder is the divisor.
Place the distance between the carpenter's squares, and multiply it by the lower horizontal leg. Divide by the height of the vertical leg to get the result.
Take the result and multiply it by the intersection with the small pole to get the dividend.
Divide the dividend by the divisor to get the height of the tower.

Answer: *a*(=8) zhang.
"""

# 令句高六尺
句高 = 6

# 從句端斜望樓足，入下股一丈二尺
下股 = 1 * 10 + 2

# 又設重矩于上，令其間相去三丈
矩間 = 3 * 10

# 更從句端斜望樓足，入上股一丈一尺四寸
上股 = 1 * 10 + 1 + Fraction(4, 10)

# 又立小表于入股之會，復從句端斜望樓岑端，入小表八寸
小表 = Fraction(8, 10)

# 上下股相減，餘為法
法 = 下股 - 上股

# 置矩閒，以下股乘之
實1 = 矩間 * 下股

# 如句高而一
實1 = Fraction(實1, 句高)

# 所得，以入小表乘之，為實
實2 = 實1 * 小表

# 實如法而一，即是樓高
a = Fraction(實2, 法) # 8 zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 8, Actual: 80"""
