"""
今有望深谷偃矩岸上令句高六尺從句端望谷底入下股九尺一寸又設重矩于上其矩間相去三丈更從句端望谷底入上股八尺五寸問谷深幾何
術曰置矩間以上股乘之為實上下股相減餘為法除之所得以句高減之即得谷深
答曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a deep valley being observed. A carpenter's square is placed on the edge of the cliff.
The vertical leg (ju) of the square is 6 chi high. From the top of the vertical leg, the bottom of the valley is observed, and the lower horizontal leg (gu) is found to be 9 chi and 1 cun.
Another carpenter's square is placed above the first, with the distance between the two squares being 3 zhang. From the top of the second vertical leg, the bottom of the valley is observed, and the upper horizontal leg (gu) is found to be 8 chi and 5 cun.
Question: How deep is the valley?

The procedure says: Place the distance between the squares. Multiply it by the difference of the upper horizontal leg and the lower horizontal leg, obtaining the dividend.
Subtract the two horizontal legs, obtaining the divisor.
Divide the dividend by the divisor. Subtract this result from the height of the vertical leg, obtaining the depth of the valley.

The answer says: *a* zhang.
"""

# 句高六尺
句高 = 6  # chi

# 下股九尺一寸
下股 = 9 + Fraction(1, 10)  # chi

# 矩間相去三丈
矩間 = 3 * 10  # Convert zhang to chi

# 上股八尺五寸
上股 = 8 + Fraction(5, 10)  # chi

# 上下股相減，餘為法
法 = 下股 - 上股

# 置矩間以上股乘之，為實
實 = 矩間 * 法

# 除之所得
所得 = Fraction(實, 法)

# 以句高減之，即得谷深
谷深 = 句高 - 所得

# Convert chi to zhang
a = Fraction(谷深, 10)  # Convert chi to zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 419/10, Actual: -12/5"""
