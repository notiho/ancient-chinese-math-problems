"""
有山居木西，不知其高。山去木五十三里，木高九丈五尺。人立木東三里，望木末適與山峰斜平。人目高七尺。問︰山高幾何？
荅曰： a丈 。
"""

"""
There is a mountain and a tree to the west of it, but the height of the mountain is unknown. 
The distance from the mountain to the tree is 53 li, and the tree is 9 zhang 5 chi tall. 
A person stands 3 li to the east of the tree and observes that the top of the tree aligns perfectly with the peak of the mountain when viewed at an angle. 
The person's eye level is 7 chi above the ground. 

Question: What is the height of the mountain?

Answer: The mountain is *a* zhang tall.
"""

# Known values
山到木距離 = 53  # li
木高 = 9 * 10 + 5  # Convert tree height to chi (1 zhang = 10 chi)
人到木距離 = 3  # li
人目高 = 7  # chi

# Total distance from the person to the mountain
總距離 = 山到木距離 + 人到木距離  # li

# Proportional height calculation using similar triangles
山高 = (木高 - 人目高) * 總距離 / 人到木距離 + 人目高  # chi

# Convert mountain height to zhang (1 zhang = 10 chi)
a = Fraction(山高, 10)  # zhang

a  # The height of the mountain in zhang
"""
Code error: both arguments should be Rational instances"""
