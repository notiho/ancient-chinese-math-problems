"""
今有津不知其廣東岸髙一丈坐岸東去岸五十步遥望岸上及津西畔適與人目㕘合人目去地二尺四寸問津廣㡬何
術曰以岸髙乗人去岸為實以人目去地為法實如法而一
答曰 a步
"""

"""
Suppose there is a river crossing, but its width is unknown. The east bank is 1 zhang high.
A person sits on the east bank, 50 bu away from the edge of the bank, and looks at the top of the bank and the west edge of the river.
The line of sight aligns exactly with the person's eye level.
The person's eye is 2 chi and 4 cun above the ground.
Question: how wide is the river crossing?

The procedure says: Multiply the height of the bank by the distance of the person from the bank, obtaining the dividend.
Take the height of the person's eye above the ground as the divisor.
Divide the dividend by the divisor, obtaining the width of the river crossing.

Answer: *a* bu.
"""

# 東岸髙一丈
岸高 = 1 * 10  # Convert 丈 to 尺 (1 丈 = 10 尺)

# 坐岸東去岸五十步
去岸 = 50

# 人目去地二尺四寸
目高 = 2 + Fraction(4, 10)  # Convert 4 寸 to 尺 (1 尺 = 10 寸)

# 以岸髙乘人去岸為實
實 = 岸高 * 去岸

# 以人目去地為法
法 = 目高

# 實如法而一
a = Fraction(實, 法)  # Result in 步
"""
"""
