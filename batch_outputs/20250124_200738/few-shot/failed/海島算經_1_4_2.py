"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a mountain climb with a view of a tower, where the tower is on flat ground.
A horizontal ruler is placed on the mountain, with the vertical leg (height) being 6 chi.
From the end of the vertical leg, looking diagonally at the base of the tower, the horizontal leg (distance) is 1 zhang and 2 chi.
Another horizontal ruler is set up higher, with the distance between the two rulers being 3 zhang.
From the end of the vertical leg of the second ruler, looking diagonally at the base of the tower, the horizontal leg (distance) is 1 zhang, 1 chi, and 4 cun.
A small pole is placed at the intersection of the horizontal legs, and from the end of the vertical leg of the second ruler, looking diagonally at the top of the tower, the small pole is 8 cun away.
Question: how tall is the tower?

The procedure says:
Subtract the upper horizontal leg from the lower horizontal leg, and the remainder is the divisor.
Place the distance between the rulers, and multiply it by the lower horizontal leg. Divide by the vertical leg, obtaining the result.
Multiply the result by the distance to the small pole, giving the dividend.
Divide the dividend by the divisor, and the result is the height of the tower.

Answer: *a* zhang.
"""

# 令句高六尺
句高 = 6  # chi

# 下股一丈二尺
下股 = 1 * 10 + 2  # Convert to chi

# 矩間三丈
矩間 = 3 * 10  # Convert to chi

# 上股一丈一尺四寸
上股 = 1 * 10 + 1 + 4 / 10  # Convert to chi

# 入小表八寸
入小表 = 8 / 10  # Convert to chi

# 上下股相減，餘為法
法 = 下股 - 上股

# 置矩閒，以下股乘之
實 = 矩間 * 下股

# 如句高而一
實 = 實 / 句高

# 所得，以入小表乘之，為實
實 = 實 * 入小表

# 實如法而一，即是樓高
樓高 = 實 / 法

# Convert to zhang
a = Fraction(樓高, 10)  # Convert chi to zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
