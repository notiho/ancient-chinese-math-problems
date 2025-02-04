"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
術曰：置矩間，以上股乘之，為實。上、下股相減，餘為法，除之。所得以句高減之，即得谷深。
答曰： a(=419/10)丈 。
"""

#----- content starts here -----
"""
Suppose there is a deep valley being observed. A carpenter's square is placed horizontally at the edge of the cliff, with the vertical leg (the "ju") set at a height of 6 chi. 
From the top of the vertical leg, the valley bottom is observed, and the horizontal leg (the "gu") extends downward by 9 chi and 1 cun.
Another carpenter's square is placed above the first, with the two squares separated by a distance of 3 zhang. 
From the top of the vertical leg of the second square, the valley bottom is observed again, and the horizontal leg extends downward by 8 chi and 5 cun.
Question: How deep is the valley?

The procedure says: Place the distance between the squares. Multiply it by the upper horizontal leg, obtaining the dividend. Subtract the lower horizontal leg from the upper horizontal leg, obtaining the divisor. Divide the dividend by the divisor. Subtract the result from the height of the vertical leg, obtaining the valley's depth.

Answer: *a*(=419/10) zhang.
"""

# 句高六尺
句高 = 6

# 入下股九尺一寸
下股 = 9 + Fraction(1, 10)

# 矩間相去三丈
矩間 = 3

# 入上股八尺五寸
上股 = 8 + Fraction(5, 10)

# 上股乘矩間，為實
實 = 上股 * 矩間

# 上、下股相減，餘為法
法 = 上股 - 下股

# 實如法除之
商 = Fraction(實, 法)

# 所得以句高減之，即得谷深
a = 商 - 句高 # 419/10 zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 419/10, Actual: -97/2"""
