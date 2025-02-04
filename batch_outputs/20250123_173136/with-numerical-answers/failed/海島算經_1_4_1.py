"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a(=8)丈 。
"""

"""
Suppose there is a mountain, and from the mountain, a tower on flat ground is observed. 
A carpenter's square is placed on the mountain, with the vertical leg (ju) being 6 chi high. 
From the top of the vertical leg, the diagonal sightline to the base of the tower intersects the horizontal leg (gu) at 1 zhang 2 chi. 
Another carpenter's square is placed higher up, with the two squares separated by 3 zhang. 
From the top of the vertical leg of the second square, the diagonal sightline to the base of the tower intersects the horizontal leg at 1 zhang 1 chi 4 cun. 
A small pole is erected at the intersection of the horizontal legs, and from the top of the vertical leg, the diagonal sightline to the top of the tower intersects the small pole at 8 cun. 
Question: How tall is the tower?

The procedure says: Subtract the upper horizontal leg from the lower horizontal leg; the remainder is the divisor. 
Place the distance between the squares, and multiply it by the lower horizontal leg. 
Divide by the height of the vertical leg, obtaining the result. 
Multiply this result by the intersection point on the small pole, obtaining the dividend. 
Divide the dividend by the divisor, obtaining the height of the tower.

Answer: *a*(=8) zhang.
"""

# 令句高六尺
句高 = 6

# 從句端斜望樓足，入下股一丈二尺
下股 = 1 * 10 + 2

# 令其間相去三丈
矩間 = 3 * 10

# 更從句端斜望樓足，入上股一丈一尺四寸
上股 = 1 * 10 + 1 + Fraction(4, 10)

# 復從句端斜望樓岑端，入小表八寸
入小表 = Fraction(8, 10)

# 上下股相減，餘為法
法 = 下股 - 上股

# 置矩閒，以下股乘之
實 = 矩間 * 下股

# 如句高而一
所得 = Fraction(實, 句高)

# 所得，以入小表乘之，為實
實 = 所得 * 入小表

# 實如法而一，即是樓高
a = Fraction(實, 法) # 8 zhang
"""
Variable 'a' has wrong value. Expected: 8, Actual: 80"""
