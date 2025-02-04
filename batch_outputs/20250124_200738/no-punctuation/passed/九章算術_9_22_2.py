"""
有山居木西不知其高山去木五十三里木高九丈五尺人立木東三里望木末適與山峰斜平人目高七尺問山高幾何
術曰置木高減人目高七尺餘以乘五十三里為實以人去木三里為法實如法而一所得加木高即山高
荅曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a mountain and a tree to its west, but the height of the mountain is unknown.
The mountain is 53 li away from the tree. The tree is 9 zhang and 5 chi tall.
A person stands 3 li to the east of the tree and observes the top of the tree aligning with the mountain peak in a straight line.
The person's eye level is 7 chi above the ground.
Question: What is the height of the mountain?

The procedure says: Place the height of the tree and subtract the height of the person's eye (7 chi).
Take the remainder and multiply it by 53 li, obtaining the dividend.
Take the distance of the person from the tree (3 li) as the divisor.
Divide the dividend by the divisor, and add the height of the tree to the result. This gives the height of the mountain.

Answer: The mountain is *a* zhang tall.
"""

# 木高九丈五尺
木高 = 9 * 10 + 5  # Convert to chi (1 zhang = 10 chi)

# 人目高七尺
人目高 = 7  # In chi

# 山去木五十三里
山去木 = 53  # In li

# 人立木東三里
人去木 = 3  # In li

# 置木高減人目高七尺
餘高 = 木高 - 人目高  # Remaining height in chi

# 餘以乘五十三里，為實
實 = 餘高 * 山去木  # Dividend in chi·li

# 以人去木三里，為法
法 = 人去木  # Divisor in li

# 實如法而一所得
所得 = Fraction(實, 法)  # Result in chi

# 所得加木高，即山高
山高 = 所得 + 木高  # Total height in chi

# Convert to zhang (1 zhang = 10 chi)
a = Fraction(山高, 10)  # Mountain height in zhang#----- content ends here -----

"""
"""
