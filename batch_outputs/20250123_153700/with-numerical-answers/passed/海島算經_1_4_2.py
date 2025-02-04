"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a(=8)丈 。
"""

"""
Suppose there is a person climbing a mountain and looking at a tower, which is on flat ground.
A right triangle is set up on the mountain, with the vertical leg (ju) being 6 chi high.
From the top of the vertical leg, looking diagonally at the base of the tower, the horizontal leg (gu) extends 1 zhang and 2 chi inward.
Another right triangle is set up above the first, with the distance between the two triangles being 3 zhang.
From the top of the second vertical leg, looking diagonally at the base of the tower, the horizontal leg extends 1 zhang, 1 chi, and 4 cun inward.
A small pole is erected at the intersection of the horizontal legs, and from the top of the second vertical leg, looking diagonally at the top of the tower, the small pole is entered by 8 cun.
Question: how tall is the tower?

The procedure says: Subtract the upper horizontal leg from the lower horizontal leg, and the remainder is the divisor.
Place the distance between the two triangles, and multiply it by the lower horizontal leg.
Divide by the height of the vertical leg, obtaining the result.
Multiply the result by the entry into the small pole, obtaining the dividend.
Divide the dividend by the divisor, and the result is the height of the tower.

Answer: *a*(=8) zhang.
"""

# 令句高六尺
句高 = 6  # chi

# 從句端斜望樓足，入下股一丈二尺
下股 = 1 * 10 + 2  # Convert to chi (1 zhang = 10 chi)

# 令其間相去三丈
矩間 = 3 * 10  # Convert to chi (3 zhang = 30 chi)

# 更從句端斜望樓足，入上股一丈一尺四寸
上股 = 1 * 10 + 1 + Fraction(4, 10)  # Convert to chi (1 zhang, 1 chi, 4 cun = 11.4 chi)

# 復從句端斜望樓岑端，入小表八寸
小表入 = Fraction(8, 10)  # Convert to chi (8 cun = 0.8 chi)

# 上下股相減，餘為法
法 = 下股 - 上股

# 置矩閒，以下股乘之
實 = 矩間 * 下股

# 如句高而一
實 = Fraction(實, 句高)

# 所得，以入小表乘之，為實
實 = 實 * 小表入

# 實如法而一，即是樓高
樓高 = Fraction(實, 法)

# Convert to zhang
a = Fraction(樓高, 10)  # 8 zhang
"""
"""
