"""
有山居木西，不知其高。山去木五十三里，木高九丈五尺。人立木東三里，望木末適與山峰斜平。人目高七尺。問︰山高幾何？
術曰：置木高減人目高七尺，餘，以乘五十三里為實。以人去木三里為法。實如法而一，所得，加木高即山高。
荅曰： a丈 。
"""

#----- content starts here -----
"""
There is a mountain west of a tree, but its height is unknown.
The mountain is 53 li away from the tree, and the tree is 9 zhang 5 chi tall.
A person stands 3 li east of the tree and observes that the top of the tree aligns with the peak of the mountain in a straight diagonal line.
The person's eye level is 7 chi high.
Question: how tall is the mountain?

The procedure says: Take the height of the tree and subtract the person's eye height (7 chi). 
The remainder is multiplied by 53 li, giving the dividend.
Take the distance of the person from the tree (3 li) as the divisor.
Divide the dividend by the divisor, and add the height of the tree to the result to obtain the height of the mountain.

Answer: the mountain is *a* zhang tall.
"""

from fractions import Fraction

# 木高 9丈5尺
木高 = 9 * 10 + 5  # Convert to chi (1丈 = 10尺)

# 人目高 7尺
人目高 = 7  # In chi

# 山去木 53里
山去木 = 53  # In li

# 人去木 3里
人去木 = 3  # In li

# 術曰：置木高減人目高七尺
餘高 = 木高 - 人目高  # Remaining height in chi

# 餘，以乘五十三里為實
實 = 餘高 * 山去木  # Dividend in chi * li

# 以人去木三里為法
法 = 人去木  # Divisor in li

# 實如法而一
山高增量 = Fraction(實, 法)  # Height increment in chi

# 所得，加木高即山高
山高 = 山高增量 + 木高  # Total height in chi

# Convert back to zhang
a = Fraction(山高, 10)  # Convert chi to zhang (1丈 = 10尺)

a  # Mountain height in zhang#----- content ends here -----

"""
"""
