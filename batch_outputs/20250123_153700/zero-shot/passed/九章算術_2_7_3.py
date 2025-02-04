"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
術曰：以粟求粺飯，二十七之，二十五而一。
荅曰：為粺飯 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that to convert 粟 (grain) into 粺飯 (refined rice), we multiply the amount of 粟 by 27 and then divide by 25. The given amount of 粟 is 3斗6升. Since 1斗 = 10升, this is equivalent to 36升. 

Here is the Python code:


"""


from fractions import Fraction

# Given amount of 粟 in 升 (1斗 = 10升)
grain = 3 * 10 + 6  # 3斗6升 = 36升

# Formula to calculate 粺飯
a = Fraction(grain * 27, 25)

# Result in 斗
a = a / 10  # Convert 升 to 斗

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the amount of 粺飯 in 斗.
"""


"""
"""
