"""
有山居木西，不知其高。山去木五十三里，木高九丈五尺。人立木東三里，望木末適與山峰斜平。人目高七尺。問︰山高幾何？
術曰：置木高減人目高七尺，餘，以乘五十三里為實。以人去木三里為法。實如法而一，所得，加木高即山高。
荅曰： a丈 。
"""

#----- content starts here -----
"""
There is a mountain west of a tree, but its height is unknown.
The mountain is 53 li away from the tree, and the tree is 9 zhang 5 chi tall.
A person stands 3 li east of the tree and observes that the top of the tree aligns with the mountain peak in a straight line.
The person's eye level is 7 chi high.
Question: how tall is the mountain?

The procedure says: Take the tree's height and subtract the person's eye height of 7 chi.
The remainder is multiplied by 53 li, giving the dividend.
Take the person's distance from the tree, 3 li, as the divisor.
Divide the dividend by the divisor, and add the tree's height to the result to obtain the mountain's height.

Answer: the mountain is *a* zhang tall.
"""

# 木高九丈五尺
木高 = 9 + Fraction(5, 10)  # Convert 9丈5尺 to 丈

# 人目高七尺
人目高 = Fraction(7, 10)  # Convert 7尺 to 丈

# 山去木五十三里
山去木 = 53

# 人去木三里
人去木 = 3

# 置木高減人目高七尺，餘
餘高 = 木高 - 人目高

# 以乘五十三里為實
實 = 餘高 * 山去木

# 以人去木三里為法
法 = 人去木

# 實如法而一
山增高 = Fraction(實, 法)

# 所得，加木高即山高
山高 = 山增高 + 木高

a = 山高  # 山高 in 丈#----- content ends here -----

"""
"""
