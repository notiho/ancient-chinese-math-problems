"""
今有木不知逺近髙下立一表髙七尺人去表九步立望表頭適與木端邪平人目去地七尺二寸又去表三十步薄地遥望表頭亦與木端邪平問木去表及髙㡬何
術曰以表髙乗人立去表為實以表髙減人目去地為法而一得木去表以表髙乗木去表為實以人目薄地去表為法實如法而一所得加表髙即木髙
答曰去表 a步 木髙 b丈
"""

#----- content starts here -----
"""
Suppose there is a tree whose distance and height are unknown. A pole is erected with a height of 7 chi. 
A person stands 9 bu away from the pole and observes the top of the pole aligned with the top of the tree. 
The person's eye level is 7 chi and 2 cun above the ground. 
The person then moves 30 bu further away from the pole (totaling 39 bu from the pole) and observes again, 
noting that the top of the pole still aligns with the top of the tree. 
Question: What is the distance from the tree to the pole, and what is the height of the tree?

The procedure says: Multiply the height of the pole by the distance the person initially stands from the pole, obtaining the dividend. 
Subtract the height of the person's eye level from the height of the pole, obtaining the divisor. 
Divide the dividend by the divisor to get the distance from the tree to the pole. 
Then, multiply the height of the pole by the distance from the tree to the pole, obtaining the dividend. 
Use the total distance the person moved away from the pole as the divisor. 
Divide the dividend by the divisor, and add the height of the pole to get the height of the tree.

Answer: The distance from the tree to the pole is *a* bu, and the height of the tree is *b* zhang.
"""

# 表髙七尺
表高 = 7

# 人目去地七尺二寸 (convert to chi: 2 cun = 0.2 chi)
人目高 = 7 + Fraction(2, 10)

# 人去表九步
初距表 = 9

# 又去表三十步 (total distance from pole is 39 bu)
總距表 = 初距表 + 30

# Step 1: Calculate 木去表 (distance from tree to pole)
# 以表髙乘人立去表為實
實1 = 表高 * 初距表

# 以表髙減人目去地為法
法1 = 表高 - 人目高

# 而一得木去表
木去表 = Fraction(實1, 法1)

# Step 2: Calculate 木髙 (height of the tree)
# 以表髙乘木去表為實
實2 = 表高 * 木去表

# 以人目薄地去表為法
法2 = 總距表

# 實如法而一所得
木高 = Fraction(實2, 法2)

# 加表髙即木髙
木高 += 表高

# Final answers
a = 木去表  # Distance from tree to pole in bu
b = Fraction(木高, 10)  # Height of the tree in zhang (1 zhang = 10 chi)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 315, Actual: -315
Variable 'b' has wrong value. Expected: 161/20, Actual: -322/65"""
