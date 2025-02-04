"""
今有望深谷偃矩岸上令句高六尺從句端望谷底入下股九尺一寸又設重矩于上其矩間相去三丈更從句端望谷底入上股八尺五寸問谷深幾何
術曰置矩間以上股乘之為實上下股相減餘為法除之所得以句高減之即得谷深
答曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a deep valley being observed. A carpenter's square is placed horizontally on the edge of the cliff.
The vertical leg (the "ju") is 6 chi high. From the top of this vertical leg, the bottom of the valley is observed, and the line of sight enters the lower horizontal leg (the "gu") at 9 chi and 1 cun.
Another carpenter's square is set up above the first one, with the two squares separated by a distance of 3 zhang. From the top of the vertical leg of the second square, the bottom of the valley is observed, and the line of sight enters the upper horizontal leg at 8 chi and 5 cun.
Question: how deep is the valley?

The procedure says: Take the distance between the squares and multiply it by the upper horizontal leg, obtaining the dividend.
Subtract the lower horizontal leg from the upper horizontal leg, obtaining the divisor.
Divide the dividend by the divisor, and subtract the height of the vertical leg from the result. This gives the depth of the valley.

Answer: the depth of the valley is *a* zhang.
"""

# 句高 6 尺
句高 = 6

# 下股 9 尺 1 寸
下股 = 9 + Fraction(1, 10)

# 矩間相去 3 丈
矩間 = 3 * 10  # Convert zhang to chi

# 上股 8 尺 5 寸
上股 = 8 + Fraction(5, 10)

# 置矩間以上股乘之，為實
實 = 矩間 * 上股

# 上下股相減，餘為法
法 = 上股 - 下股

# 除之所得
所得 = Fraction(實, 法)

# 以句高減之，即得谷深
谷深 = 所得 - 句高

# Convert chi to zhang
a = Fraction(谷深, 10)  # Convert chi to zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 419/10, Actual: -431/10"""
