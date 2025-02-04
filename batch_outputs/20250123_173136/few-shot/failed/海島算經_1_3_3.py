"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
術曰：置矩間，以上股乘之，為實。上、下股相減，餘為法，除之。所得以句高減之，即得谷深。
答曰： a丈 。
"""

"""
Suppose there is a deep valley being observed. A carpenter's square is laid flat on the edge of the cliff, with the vertical leg (the "ju") set to a height of 6 chi. 
From the tip of the vertical leg, the bottom of the valley is observed, and the horizontal leg (the "gu") extends downward by 9 chi and 1 cun.
Another carpenter's square is set up above the first one, with the two squares separated by a distance of 3 zhang. 
From the tip of the vertical leg of the second square, the bottom of the valley is observed, and the horizontal leg extends downward by 8 chi and 5 cun.
Question: how deep is the valley?

The procedure says: Place the distance between the squares. Multiply it by the upper horizontal leg, obtaining the dividend. Subtract the lower horizontal leg from the upper horizontal leg, obtaining the divisor. Divide the dividend by the divisor. Subtract the height of the vertical leg from the result, obtaining the depth of the valley.

Answer: *a* zhang.
"""

# 句高六尺
句高 = 6

# 下股九尺一寸
下股 = 9 + Fraction(1, 10)

# 矩間相去三丈
矩間 = 3 * 10  # Convert zhang to chi

# 上股八尺五寸
上股 = 8 + Fraction(5, 10)

# 置矩間，以上股乘之，為實
實 = 矩間 * 上股

# 上、下股相減，餘為法
法 = 上股 - 下股

# 除之
所得 = Fraction(實, 法)

# 所得以句高減之，即得谷深
谷深 = 所得 - 句高

# Convert chi to zhang
a = Fraction(谷深, 10)  # Convert chi to zhang
"""
Variable 'a' has wrong value. Expected: 419/10, Actual: -431/10"""
