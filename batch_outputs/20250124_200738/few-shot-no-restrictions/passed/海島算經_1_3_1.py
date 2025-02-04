"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
術曰：置矩間，以上股乘之，為實。上、下股相減，餘為法，除之。所得以句高減之，即得谷深。
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a deep valley being observed. A carpenter's square is placed horizontally on the edge of the cliff, with the vertical leg (the "ju") set to a height of 6 chi. 
From the top of the vertical leg, the valley bottom is observed, and the horizontal leg (the "gu") extends downward by 9 chi and 1 cun.
Another carpenter's square is set above the first, with the two squares separated by a distance of 3 zhang. 
From the top of the vertical leg of the second square, the valley bottom is observed, and the horizontal leg extends downward by 8 chi and 5 cun.
Question: How deep is the valley?

The procedure says: Place the distance between the two squares as the base. Multiply it by the upper horizontal leg, obtaining the dividend. Subtract the lower horizontal leg from the upper horizontal leg, and the remainder is the divisor. Divide the dividend by the divisor. Subtract the height of the vertical leg from the result, and the remainder is the depth of the valley.

Answer: The valley is *a* zhang deep.
"""

from fractions import Fraction

# Known values
句高 = 6  # chi
矩間 = 3  # zhang
矩間_in_chi = 矩間 * 10  # Convert zhang to chi

下股 = 9 + Fraction(1, 10)  # 9 chi 1 cun
上股 = 8 + Fraction(5, 10)  # 8 chi 5 cun

# Procedure
# 置矩間，以上股乘之，為實
實 = 矩間_in_chi * 上股

# 上、下股相減，餘為法
法 = 下股 - 上股

# 除之
商 = Fraction(實, 法)

# 所得以句高減之，即得谷深
谷深 = 商 - 句高

# Convert chi to zhang
a = Fraction(谷深, 10)  # Convert chi to zhang

a  # The depth of the valley in zhang#----- content ends here -----

"""
"""
