"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

"""
To solve this problem, we need to compute the length ("袤") in units of 丈 (zhang). Let's translate the problem into Python code step by step.

### Problem Breakdown:
1. The total work is given as 33,582 人功 (person-work).
2. The total work corresponds to a length of 300 尺 (chi).
3. A group of 1,000 people arrives first, and we need to calculate the length ("袤") they can complete.

### Assumptions:
- 1 丈 = 10 尺.
- The work done by 1 person for 1 尺 is constant.

### Solution:
We calculate the length based on the given formula:
- First, calculate the work done by 1,000 people.
- Then, determine the corresponding length in 尺.
- Finally, convert the length from 尺 to 丈.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_work = 33582  # Total person-work
total_length_chi = 300  # Total length in chi
people_first_group = 1000  # Number of people in the first group

# Step 1: Calculate work per chi
work_per_chi = Fraction(total_work, total_length_chi)

# Step 2: Calculate the work done by the first group
work_done_by_first_group = work_per_chi * people_first_group

# Step 3: Calculate the length in chi for the first group
length_chi = Fraction(work_done_by_first_group, work_per_chi)

# Step 4: Convert chi to zhang (1 zhang = 10 chi)
a = length_chi / 10  # Length in zhang

# Result
a  # This is the length in zhang


"""


The variable `a` will hold the solution in 丈 (zhang).
"""


"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 100"""
