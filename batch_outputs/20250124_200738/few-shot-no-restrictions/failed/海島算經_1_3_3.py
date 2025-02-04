"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
術曰：置矩間，以上股乘之，為實。上、下股相減，餘為法，除之。所得以句高減之，即得谷深。
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a deep valley being observed. A carpenter's square is placed horizontally on the edge of the cliff. 
The vertical leg (the "ju") of the square is 6 chi high. 
From the tip of the vertical leg, the valley bottom is observed, and the lower horizontal leg (the "gu") extends 9 chi and 1 cun downward.
Another carpenter's square is placed above the first one, with the distance between the two squares being 3 zhang. 
From the tip of the vertical leg of the second square, the valley bottom is observed again, and the upper horizontal leg extends 8 chi and 5 cun downward.
Question: How deep is the valley?

The procedure says: Place the distance between the two squares. Multiply it by the upper horizontal leg, obtaining the dividend.
Subtract the upper horizontal leg from the lower horizontal leg, obtaining the divisor.
Divide the dividend by the divisor. Subtract the height of the vertical leg from the result, obtaining the depth of the valley.

Answer: *a* zhang.
"""

from fractions import Fraction

# Known values
句高 = 6  # chi
矩間 = 3  # zhang
下股 = 9 + Fraction(1, 10)  # 9 chi 1 cun = 9.1 chi
上股 = 8 + Fraction(5, 10)  # 8 chi 5 cun = 8.5 chi

# Procedure
# 置矩間，以上股乘之，為實
實 = 矩間 * 上股

# 上、下股相減，餘為法
法 = 下股 - 上股

# 除之
所得 = Fraction(實, 法)

# 所得以句高減之，即得谷深
谷深 = 所得 - 句高

# Convert 谷深 to zhang
a = 谷深  # Depth in zhang

谷深#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 419/10, Actual: 73/2"""
