"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
術曰：置矩間，以上股乘之，為實。上、下股相減，餘為法，除之。所得以句高減之，即得谷深。
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a deep valley being observed. A carpenter's square is placed horizontally on the edge of the cliff, with the vertical leg (the "ju") set to 6 chi in height.
From the top of the vertical leg, the bottom of the valley is observed, and the horizontal leg (the "gu") extends downward by 9 chi and 1 cun.
Another carpenter's square is placed above the first one, with the distance between the two squares being 3 zhang.
From the top of the vertical leg of the second square, the bottom of the valley is observed, and the horizontal leg extends downward by 8 chi and 5 cun.
Question: How deep is the valley?

The procedure says: Place the distance between the two squares, and multiply it by the upper horizontal leg, obtaining the dividend.
Subtract the lower horizontal leg from the upper horizontal leg, and the remainder becomes the divisor.
Divide the dividend by the divisor. Subtract the height of the vertical leg from the result, and the depth of the valley is obtained.

Answer: The valley is *a* zhang deep.
"""

from fractions import Fraction

# Known values
句高 = 6  # chi
矩間 = 3  # zhang
矩間_in_chi = 矩間 * 10  # Convert zhang to chi (1 zhang = 10 chi)

下股 = 9 + Fraction(1, 10)  # 9 chi 1 cun (1 chi = 10 cun)
上股 = 8 + Fraction(5, 10)  # 8 chi 5 cun (1 chi = 10 cun)

# Procedure
# 置矩間，以上股乘之，為實
實 = 矩間_in_chi * 上股

# 上、下股相減，餘為法
法 = 下股 - 上股

# 除之
谷深_in_chi = Fraction(實, 法)

# 所得以句高減之，即得谷深
谷深 = 谷深_in_chi - 句高

# Convert the depth to zhang
a = Fraction(谷深, 10)  # Convert chi to zhang (1 zhang = 10 chi)

# Final answer
a  # The valley depth in zhang#----- content ends here -----

"""
"""
