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
total_work = 33582  # Total work in "人功"
work_per_person = Fraction(300, 1)  # Work per person in "尺"
remaining_work = Fraction(14, 10)  # Remaining work in "尺" (14尺4寸 = 14.4尺)
initial_people = 1000  # Number of people who arrived first

# Calculate the total length of work in 尺
total_length = total_work * work_per_person - remaining_work

# Calculate the length of work done by the initial people
a = total_length / initial_people

# Convert the result to 丈 (1丈 = 10尺)
a = a / 10

# Output the result
a


"""


This code calculates the value of `a` in 丈 based on the given problem. The result will be stored in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 50372993/50000"""
