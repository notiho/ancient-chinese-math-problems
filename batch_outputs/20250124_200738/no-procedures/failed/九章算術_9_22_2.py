"""
有山居木西，不知其高。山去木五十三里，木高九丈五尺。人立木東三里，望木末適與山峰斜平。人目高七尺。問︰山高幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
There is a mountain west of a tree, but the height of the mountain is unknown. The distance between the mountain and the tree is 53 li. The tree is 9 zhang and 5 chi tall. A person stands 3 li east of the tree and observes the top of the tree aligning with the peak of the mountain in a straight line. The person's eye level is 7 chi above the ground.

Question: What is the height of the mountain?

Answer: The mountain is *a* zhang tall.
"""

# Given values
山去木 = 53  # Distance between the mountain and the tree in li
木高 = 9 * 10 + 5  # Tree height in chi (1 zhang = 10 chi)
人立木東 = 3  # Distance between the person and the tree in li
人目高 = 7  # Person's eye height in chi

# Total distance between the person and the mountain
總距離 = 山去木 + 人立木東  # in li

# Proportional height difference between the mountain and the tree
# Using similar triangles: (山高 - 木高) / 總距離 = (木高 - 人目高) / 人立木東
山高_差 = Fraction(木高 - 人目高, 人立木東) * 總距離

# Mountain height is the tree height plus the height difference
山高 = 木高 + 山高_差

# Convert mountain height to zhang (1 zhang = 10 chi)
a = Fraction(山高, 10)  # Mountain height in zhang

a  # Final answer#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4949/30, Actual: 5213/30"""
