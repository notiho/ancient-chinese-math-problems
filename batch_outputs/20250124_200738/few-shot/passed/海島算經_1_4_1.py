"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a mountain, and from the mountain one observes a tower that is on flat ground. 
A horizontal carpenter's square is placed on the mountain, with the vertical leg (the "ju") being 6 chi high.
From the top of the vertical leg, one looks diagonally at the base of the tower, and the horizontal leg (the "gu") extends 1 zhang 2 chi inward.
Another carpenter's square is placed above, with a distance of 3 zhang between the two squares.
From the top of the second square's vertical leg, one looks diagonally at the base of the tower, and the horizontal leg extends 1 zhang 1 chi 4 cun inward.
A small pole is erected at the intersection of the inward horizontal legs, and from the top of the vertical leg of the second square, one looks diagonally at the top of the tower, with the horizontal leg extending 8 cun inward along the small pole.
Question: how tall is the tower?

The procedure says: Subtract the upper horizontal leg from the lower horizontal leg. The remainder is the divisor.
Place the distance between the two carpenter's squares, and multiply it by the lower horizontal leg. Divide by the height of the vertical leg to get the result.
Multiply the result by the inward extension of the small pole to get the dividend.
Divide the dividend by the divisor to get the height of the tower.

Answer: *a* zhang.
"""

# 令句高六尺
句高 = 6  # chi

# 下股一丈二尺
下股 = 1 * 10 + 2  # Convert to chi

# 矩間三丈
矩間 = 3 * 10  # Convert to chi

# 上股一丈一尺四寸
上股 = 1 * 10 + 1 + Fraction(4, 10)  # Convert to chi

# 入小表八寸
入小表 = Fraction(8, 10)  # Convert to chi

# 上下股相減，餘為法
法 = 下股 - 上股

# 置矩閒，以下股乘之
實1 = 矩間 * 下股

# 如句高而一
實2 = Fraction(實1, 句高)

# 所得，以入小表乘之，為實
實3 = 實2 * 入小表

# 實如法而一，即是樓高
樓高 = Fraction(實3, 法)

# Convert to zhang
a = Fraction(樓高, 10)  # Convert chi to zhang#----- content ends here -----

"""
"""
