"""
今有登山望樓樓在平地偃矩山上令句高六尺從句端斜望樓足入下股一丈二尺又設重矩于上令其間相去三丈更從句端斜望樓足入上股一丈一尺四寸又立小表于入股之會復從句端斜望樓岑端入小表八寸問樓高幾何
術曰上下股相減餘為法置矩閒以下股乘之如句高而一所得以入小表乘之為實實如法而一即是樓高
答曰 a丈 
"""

"""
Suppose there is a mountain, and from the mountain, one looks at a tower standing on flat ground.
A right triangle is formed on the mountain, with the vertical leg (the "upright") being 6 chi tall.
From the top of the vertical leg, the diagonal line of sight to the base of the tower intersects the horizontal leg (the "base") at 1 zhang and 2 chi.
Another right triangle is formed above the first one, with the two triangles separated by a horizontal distance of 3 zhang.
From the top of this second vertical leg, the diagonal line of sight to the base of the tower intersects the horizontal leg at 1 zhang, 1 chi, and 4 cun.
Finally, a small pole is erected at the intersection of the horizontal leg and the diagonal line of sight, and from the top of the vertical leg, the diagonal line of sight to the top of the tower intersects the small pole at 8 cun.
Question: How tall is the tower?

The procedure says: Subtract the upper horizontal leg from the lower horizontal leg, and the remainder is the divisor.
Place the horizontal distance between the two triangles, and multiply it by the lower horizontal leg.
Divide by the height of the vertical leg, and multiply the result by the small pole's height.
This gives the dividend.
Divide the dividend by the divisor, and the result is the height of the tower.

Answer: The tower is *a* zhang tall.
"""

# Given values
句高 = 6  # Vertical leg (upright) in chi
下股 = 1 * 10 + 2  # Lower horizontal leg (base) in chi (1 zhang 2 chi = 12 chi)
矩間 = 3 * 10  # Horizontal distance between the two triangles in chi (3 zhang = 30 chi)
上股 = 1 * 10 + 1 * 1 + 4 / 10  # Upper horizontal leg (base) in chi (1 zhang 1 chi 4 cun = 11.4 chi)
小表 = 8 / 10  # Small pole height in chi (8 cun = 0.8 chi)

# Subtract the upper horizontal leg from the lower horizontal leg
法 = 下股 - 上股

# Multiply the horizontal distance by the lower horizontal leg
實 = 矩間 * 下股

# Divide by the height of the vertical leg
實 = 實 / 句高

# Multiply by the small pole's height
實 = 實 * 小表

# Divide the result by the divisor
樓高 = 實 / 法

# Convert the result to zhang
a = Fraction(樓高, 10)  # Convert chi to zhang (10 chi = 1 zhang)
"""
Code error: both arguments should be Rational instances"""
