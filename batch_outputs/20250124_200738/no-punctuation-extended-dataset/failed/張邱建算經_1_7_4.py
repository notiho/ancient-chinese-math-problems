"""
今有木不知逺近髙下立一表髙七尺人去表九步立望表頭適與木端邪平人目去地七尺二寸又去表三十步薄地遥望表頭亦與木端邪平問木去表及髙㡬何
術曰以表髙乗人立去表為實以表髙減人目去地為法而一得木去表以表髙乗木去表為實以人目薄地去表為法實如法而一所得加表髙即木髙
答曰去表 a步 木髙 b丈
"""

#----- content starts here -----
"""
Suppose there is a tree, the distance and height of which are unknown. A pole is erected with a height of 7 chi. 
A person stands 9 bu away from the pole and observes the top of the pole aligned with the top of the tree. 
The person's eye level is 7 chi 2 cun above the ground. 
The person then moves 30 bu further away from the pole (totaling 39 bu from the pole) and observes again, with the top of the pole still aligned with the top of the tree. 
Question: What is the distance from the tree to the pole, and what is the height of the tree?

The procedure says: Multiply the height of the pole by the initial distance of the person from the pole to obtain the dividend. 
Subtract the height of the person's eye level from the height of the pole to obtain the divisor. 
Divide the dividend by the divisor to obtain the distance from the tree to the pole. 
Then, multiply the height of the pole by the distance from the tree to the pole to obtain the dividend. 
Use the total distance of the person from the pole in the second observation as the divisor. 
Divide the dividend by the divisor, and add the height of the pole to obtain the height of the tree.

Answer: The distance from the tree to the pole is *a* bu, and the height of the tree is *b* zhang.
"""

# 表高 7 尺
表高 = 7

# 人目去地 7 尺 2 寸
人目去地 = 7 + Fraction(2, 10)

# 人去表 9 步
初距表 = 9

# 再去表 30 步
再距表 = 30 + 初距表

# 以表高乘人立去表為實
實_初 = 表高 * 初距表

# 以表高減人目去地為法
法_初 = 表高 - 人目去地

# 而一得木去表
木去表 = Fraction(實_初, 法_初)

# 以表高乘木去表為實
實_再 = 表高 * 木去表

# 以人目薄地去表為法
法_再 = 再距表

# 實如法而一所得
木高_不含表 = Fraction(實_再, 法_再)

# 加表高即木高
木高 = 木高_不含表 + 表高

# Convert 木高 to 丈 (1 丈 = 10 尺)
木高_丈 = Fraction(木高, 10)

# Final answers
a = 木去表  # Distance from tree to pole in bu
b = 木高_丈  # Height of the tree in zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 315, Actual: -315
Variable 'b' has wrong value. Expected: 161/20, Actual: -322/65"""
