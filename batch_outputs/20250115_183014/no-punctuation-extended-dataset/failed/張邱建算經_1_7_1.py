"""
今有木不知逺近髙下立一表髙七尺人去表九步立望表頭適與木端邪平人目去地七尺二寸又去表三十步薄地遥望表頭亦與木端邪平問木去表及髙㡬何
術曰以表髙乗人立去表為實以表髙減人目去地為法而一得木去表以表髙乗木去表為實以人目薄地去表為法實如法而一所得加表髙即木髙
答曰去表 a步 木髙 b丈
"""

"""
Suppose there is a tree, but its distance and height are unknown.
A pole is erected with a height of 7 chi. A person stands 9 bu away from the pole and observes the top of the pole aligned with the top of the tree. The person's eye level is 7 chi and 2 cun above the ground.
The person then moves 30 bu further away from the pole (total 39 bu from the pole) and observes the top of the pole aligned with the top of the tree again.
Question: What is the distance of the tree from the pole, and what is the height of the tree?

The procedure says:
1. Multiply the height of the pole by the distance the person initially stands from the pole. This is the dividend.
2. Subtract the height of the person's eye level from the height of the pole. This is the divisor.
3. Divide the dividend by the divisor to obtain the distance of the tree from the pole.
4. Multiply the height of the pole by the distance of the tree from the pole. This is the dividend.
5. Use the distance from the person's eye level to the pole (when they are further away) as the divisor.
6. Divide the dividend by the divisor, then add the height of the pole to obtain the height of the tree.

Answer: The tree is *a* bu away from the pole, and its height is *b* zhang.
"""

# 表髙七尺
表髙 = 7

# 人目去地七尺二寸 (convert to chi: 1 chi = 10 cun)
人目去地 = 7 + Fraction(2, 10)

# 人去表九步
初距表 = 9

# 薄地又去表三十步 (total distance from pole = 9 + 30 = 39 bu)
薄地距表 = 初距表 + 30

# Step 1: 以表髙乘人立去表為實
實1 = 表髙 * 初距表

# Step 2: 以表髙減人目去地為法
法1 = 表髙 - 人目去地

# Step 3: 實如法而一得木去表
木去表 = Fraction(實1, 法1)

# Step 4: 以表髙乘木去表為實
實2 = 表髙 * 木去表

# Step 5: 以人目薄地去表為法
法2 = 薄地距表

# Step 6: 實如法而一所得，加表髙即木髙
木髙 = Fraction(實2, 法2) + 表髙

# Final answers
a = 木去表  # Distance of the tree from the pole in bu
b = Fraction(木髙, 10)  # Convert tree height from chi to zhang (1 zhang = 10 chi)
"""
Variable 'a' has wrong value. Expected: 315, Actual: -315
Variable 'b' has wrong value. Expected: 161/20, Actual: -322/65"""
