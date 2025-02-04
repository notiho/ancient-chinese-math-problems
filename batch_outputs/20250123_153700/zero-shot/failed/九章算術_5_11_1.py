"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
total_work = 33582  # Total person-work in 尺
remaining_work = 14 + Fraction(4, 10)  # Remaining work in 尺 (14尺4寸)
total_work -= remaining_work  # Adjust the total work

depth = 300  # Depth in 尺
width = Fraction(1, 2)  # Width in 尺 (half of the depth)
one_person_work = depth * width  # Work done by one person in 尺

# First 1000 people arrive
people = 1000

# Compute the length (袤) in 尺
a = (one_person_work * people) / depth

# Convert to 丈 (1 丈 = 10 尺)
a /= 10

# Result
a  # Length in 丈


"""


This code calculates the length (袤) in 丈 based on the given problem. The variable `a` will hold the solution.
"""


"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 50"""
