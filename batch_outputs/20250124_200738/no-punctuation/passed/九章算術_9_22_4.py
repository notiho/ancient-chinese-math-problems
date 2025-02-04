"""
有山居木西不知其高山去木五十三里木高九丈五尺人立木東三里望木末適與山峰斜平人目高七尺問山高幾何
術曰置木高減人目高七尺餘以乘五十三里為實以人去木三里為法實如法而一所得加木高即山高
荅曰 a丈 
"""

#----- content starts here -----
"""
There is a mountain and a tree to its west, but the height of the mountain is unknown.
The distance from the mountain to the tree is 53 li. The tree is 9 zhang and 5 chi tall.
A person stands 3 li east of the tree and observes the top of the tree aligning with the mountain peak in a straight line.
The person's eye level is 7 chi above the ground.
Question: What is the height of the mountain?

The procedure says: Take the height of the tree and subtract the person's eye level (7 chi). 
Multiply the remainder by the distance from the mountain to the tree (53 li), obtaining the dividend.
Take the distance from the person to the tree (3 li) as the divisor.
Divide the dividend by the divisor, and add the height of the tree to the result. This gives the height of the mountain.

The answer says: *a* zhang.
"""

# 木高九丈五尺
木高 = 9 + Fraction(5, 10)  # Convert 9丈5尺 to zhang

# 人目高七尺
人目高 = Fraction(7, 10)  # Convert 7尺 to zhang

# 山去木五十三里
山去木 = 53

# 人去木三里
人去木 = 3

# 置木高減人目高七尺
餘高 = 木高 - 人目高

# 餘以乘五十三里為實
實 = 餘高 * 山去木

# 以人去木三里為法
法 = 人去木

# 實如法而一所得
所得 = Fraction(實, 法)

# 所得加木高即山高
山高 = 所得 + 木高

a = 山高  # 山高 in zhang#----- content ends here -----

"""
"""
