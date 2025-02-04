"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

"""
To solve this problem, we need to compute the value of "a" (the length in 丈). Here's the Python code:


"""


from fractions import Fraction

# Given data
total_work = 33582  # Total 人功
remaining_work = Fraction(14, 10)  # Remaining work in 尺 (14尺4寸 = 14.4尺)
total_work_in_尺 = total_work - remaining_work  # Total work in 尺 after subtracting remaining work
depth = 3  # Depth in 尺
width_top = 300  # Top width in 尺
width_bottom = 0  # Bottom width in 尺
workers_first_arrival = 1000  # Number of workers who arrived first

# Calculate the average width
average_width = Fraction(width_top + width_bottom, 2)

# Calculate the work done by the first group of workers
work_done_by_first_group = total_work_in_尺 * workers_first_arrival

# Calculate the length (袤) in 尺
length_in_尺 = Fraction(work_done_by_first_group, average_width * depth)

# Convert length to 丈 (1 丈 = 10 尺)
a = length_in_尺 / 10

# Result
a


"""


The variable `a` will contain the length in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 335806/45"""
