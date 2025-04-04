"""
有山居木西，不知其高。山去木五十三里，木高九丈五尺。人立木東三里，望木末適與山峰斜平。人目高七尺。問︰山高幾何？
術曰：置木高減人目高七尺，餘，以乘五十三里為實。以人去木三里為法。實如法而一，所得，加木高即山高。
荅曰： a丈 。
"""

#----- content starts here -----
"""
There is a mountain west of a tree, but its height is unknown. 
The mountain is 53 li away from the tree, and the tree is 9 zhang 5 chi tall.
A person stands 3 li east of the tree and observes that the top of the tree aligns perfectly with the peak of the mountain in a straight line.
The person's eye level is 7 chi above the ground.
Question: How tall is the mountain?

The procedure says: Take the height of the tree and subtract the height of the person's eye (7 chi). 
The remainder is multiplied by the distance between the mountain and the tree (53 li), giving the dividend.
The distance between the person and the tree (3 li) is the divisor.
Divide the dividend by the divisor, and add the height of the tree to the result to obtain the height of the mountain.

Answer: The mountain is *a* zhang tall.
"""

from fractions import Fraction

# 木高 9丈5尺
木高 = 9 + Fraction(5, 10)  # Convert to zhang (1丈 = 10尺)

# 人目高 7尺
人目高 = Fraction(7, 10)  # Convert to zhang

# 山去木 53里
山木距離 = 53

# 人去木 3里
人木距離 = 3

# 木高減人目高
有效木高 = 木高 - 人目高

# 以乘五十三里為實
實 = 有效木高 * 山木距離

# 以人去木三里為法
法 = 人木距離

# 實如法而一
山高增量 = 實 / 法

# 所得，加木高即山高
山高 = 山高增量 + 木高

a = 山高
a#----- content ends here -----

"""
"""
