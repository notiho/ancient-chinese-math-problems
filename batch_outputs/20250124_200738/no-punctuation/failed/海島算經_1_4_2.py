"""
今有登山望樓樓在平地偃矩山上令句高六尺從句端斜望樓足入下股一丈二尺又設重矩于上令其間相去三丈更從句端斜望樓足入上股一丈一尺四寸又立小表于入股之會復從句端斜望樓岑端入小表八寸問樓高幾何
術曰上下股相減餘為法置矩閒以下股乘之如句高而一所得以入小表乘之為實實如法而一即是樓高
答曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a mountain, and from the mountain, one looks at a tower. The tower is on flat ground.
A right triangle is set up on the mountain, with the vertical leg (ju) being 6 chi high.
From the top of the vertical leg, the hypotenuse (xie) is used to observe the base of the tower, intersecting the horizontal leg (gu) at 1 zhang 2 chi.
Another right triangle is set up above the first, with the distance between the two triangles being 3 zhang.
From the top of the second vertical leg, the hypotenuse intersects the horizontal leg at 1 zhang 1 chi 4 cun.
A small pole is erected at the intersection point of the horizontal leg, and from the top of the second vertical leg, the hypotenuse intersects the top of the small pole at 8 cun.
Question: how tall is the tower?

The procedure says: Subtract the upper horizontal leg from the lower horizontal leg, and the remainder is the divisor.
Place the distance between the two triangles, and multiply it by the lower horizontal leg. Treat it as the vertical leg (ju).
Divide the result by the remainder, and multiply it by the height of the small pole. The result is the dividend.
Divide the dividend by the divisor, and the result is the height of the tower.

Answer: *a* zhang.
"""

# 設定已知數據
句高 = 6  # 句高六尺
下股 = 1 * 10 + 2  # 下股一丈二尺 (轉換為尺)
矩間 = 3 * 10  # 矩間三丈 (轉換為尺)
上股 = 1 * 10 + 1 + Fraction(4, 10)  # 上股一丈一尺四寸 (轉換為尺)
小表 = Fraction(8, 10)  # 小表八寸 (轉換為尺)

# 上下股相減，餘為法
法 = 下股 - 上股

# 置矩閒以下股乘之，如句高而一
實1 = 矩間 * 下股 / 法

# 所得以入小表乘之，為實
實2 = 實1 * 小表

# 實如法而一，即是樓高
樓高 = 實2 / 法

# 轉換為丈
a = Fraction(樓高, 10)  # 樓高以丈為單位#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 8, Actual: 80"""
