"""
今有望深谷偃矩岸上令句高六尺從句端望谷底入下股九尺一寸又設重矩于上其矩間相去三丈更從句端望谷底入上股八尺五寸問谷深幾何
術曰置矩間以上股乘之為實上下股相減餘為法除之所得以句高減之即得谷深
答曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a deep valley being observed. A horizontal carpenter's square is placed on the edge of the cliff. 
The vertical leg (ju) is 6 chi high. From the end of the vertical leg, the valley bottom is observed, and the lower diagonal leg (gu) is 9 chi and 1 cun.
Another carpenter's square is set above the first one, with the distance between the two squares being 3 zhang. 
From the end of the vertical leg of the upper square, the valley bottom is observed again, and the upper diagonal leg (gu) is 8 chi and 5 cun.
Question: How deep is the valley?

The procedure says: Place the distance between the squares. Multiply it by the upper diagonal leg, obtaining the dividend.
Subtract the lower diagonal leg from the upper diagonal leg, obtaining the divisor.
Divide the dividend by the divisor. Subtract the height of the vertical leg from the result, and the depth of the valley is obtained.

Answer: The depth of the valley is *a* zhang.
"""

# 句高六尺
句高 = 6  # in chi

# 下股九尺一寸
下股 = 9 + Fraction(1, 10)  # convert 1 cun to chi (1 cun = 1/10 chi)

# 矩間相去三丈
矩間 = 3 * 10  # convert zhang to chi (1 zhang = 10 chi)

# 上股八尺五寸
上股 = 8 + Fraction(5, 10)  # convert 5 cun to chi

# 置矩間以上股乘之，為實
實 = 矩間 * 上股

# 上下股相減，餘為法
法 = 上股 - 下股

# 除之所得
所得 = Fraction(實, 法)

# 以句高減之，即得谷深
谷深 = 所得 - 句高

# Convert the depth to zhang
a = Fraction(谷深, 10)  # convert chi to zhang (1 zhang = 10 chi)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 419/10, Actual: -431/10"""
