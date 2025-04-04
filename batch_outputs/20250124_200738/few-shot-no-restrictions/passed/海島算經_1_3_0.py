"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
術曰：置矩間，以上股乘之，為實。上、下股相減，餘為法，除之。所得以句高減之，即得谷深。
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a deep valley being observed. A carpenter's square is placed horizontally at the edge of the cliff, with the vertical leg (the "ju") set to a height of 6 chi.
From the tip of the vertical leg, the valley bottom is observed, and the horizontal leg (the "gu") extends downward by 9 chi and 1 cun.
Another carpenter's square is placed above the first one, with the two squares separated by a distance of 3 zhang.
From the tip of the vertical leg of the second square, the valley bottom is observed, and the horizontal leg extends downward by 8 chi and 5 cun.
Question: How deep is the valley?

The procedure says: Place the distance between the squares as the divisor.
Multiply it by the upper horizontal leg to get the dividend.
Subtract the lower horizontal leg from the upper horizontal leg to get the divisor.
Divide the dividend by the divisor.
Subtract the height of the vertical leg from the result to get the depth of the valley.

Answer: The depth of the valley is *a* zhang.
"""

from fractions import Fraction

# Known values
句高 = 6  # chi
矩間 = 3  # zhang
下股 = 9 + Fraction(1, 10)  # 9 chi 1 cun (1 cun = 1/10 chi)
上股 = 8 + Fraction(5, 10)  # 8 chi 5 cun (1 cun = 1/10 chi)

# Convert 矩間 to chi (1 zhang = 10 chi)
矩間_in_chi = 矩間 * 10

# Calculate the dividend (實)
實 = 矩間_in_chi * 上股

# Calculate the divisor (法)
法 = 下股 - 上股

# Divide to find the intermediate result
intermediate_result = Fraction(實, 法)

# Subtract the height of the vertical leg (句高) to find the depth of the valley
谷深 = intermediate_result - 句高

# Convert the result to zhang (1 zhang = 10 chi)
a = 谷深 / 10

# Output the depth of the valley in zhang
a#----- content ends here -----

"""
"""
