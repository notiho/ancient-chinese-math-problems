"""
今有登山望樓樓在平地偃矩山上令句高六尺從句端斜望樓足入下股一丈二尺又設重矩于上令其間相去三丈更從句端斜望樓足入上股一丈一尺四寸又立小表于入股之會復從句端斜望樓岑端入小表八寸問樓高幾何
術曰上下股相減餘為法置矩閒以下股乘之如句高而一所得以入小表乘之為實實如法而一即是樓高
答曰 a丈 
"""

"""
Suppose there is a mountain, and from the mountain, one looks at a tower. The tower is on flat ground.
A horizontal ruler is placed on the mountain, with the vertical leg of the ruler being 6 chi high.
From the top of the vertical leg, the diagonal is extended to the base of the tower, intersecting the lower horizontal leg at 1 zhang 2 chi.
Another horizontal ruler is placed above, with the distance between the two rulers being 3 zhang.
From the top of the vertical leg of the upper ruler, the diagonal is extended to the base of the tower, intersecting the upper horizontal leg at 1 zhang 1 chi 4 cun.
A small pole is erected at the intersection of the diagonal and the horizontal leg.
From the top of the vertical leg, the diagonal is extended to the top of the tower, intersecting the small pole at 8 cun.
Question: how high is the tower?

The procedure says: Subtract the upper horizontal leg from the lower horizontal leg, and the remainder is the divisor.
Place the distance between the two rulers and multiply it by the lower horizontal leg. Divide by the vertical leg, obtaining a result.
Multiply this result by the intersection of the small pole, obtaining the dividend.
Divide the dividend by the divisor, and the result is the height of the tower.

Answer: *a* zhang.
"""

# 句高六尺
句高 = 6  # in chi

# 下股一丈二尺
下股 = 1 * 10 + 2  # convert to chi

# 矩間三丈
矩間 = 3 * 10  # convert to chi

# 上股一丈一尺四寸
上股 = 1 * 10 + 1 + Fraction(4, 10)  # convert to chi

# 入小表八寸
入小表 = Fraction(8, 10)  # convert to chi

# 上下股相減，餘為法
法 = 下股 - 上股

# 置矩閒以下股乘之
實1 = 矩間 * 下股

# 如句高而一，所得
所得 = Fraction(實1, 句高)

# 以入小表乘之，為實
實2 = 所得 * 入小表

# 實如法而一，即是樓高
樓高 = Fraction(實2, 法)

# Convert to zhang
a = Fraction(樓高, 10)  # convert chi to zhang
"""
"""
