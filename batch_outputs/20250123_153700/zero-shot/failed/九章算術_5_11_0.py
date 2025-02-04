"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a丈 。
"""

"""
To solve this problem, we need to translate the ancient Chinese math problem into Python code. Let's break it down step by step.

### Problem Analysis:
1. The total work is 33,582 "人功" (person-work units), with a shortfall of 14尺4寸 (14 feet and 4 tenths of a foot).
2. 1,000 people arrive first, and we need to calculate how much length (袤) they can complete.
3. The formula provided is:
   - Multiply the work done by one person per foot by the number of people who arrived first.
   - Add the upper and lower widths, divide by 2 to get the average width, and multiply by the depth to calculate the length.

### Assumptions:
- The units are consistent, and we will convert everything into "尺" (feet) for calculation.
- The shortfall of 14尺4寸 is equivalent to \( 14 + \frac{4}{10} = 14.4 \) feet.

### Python Code:

"""


from fractions import Fraction

# Given data
total_work = 33582  # Total person-work units
shortfall = Fraction(14, 1) + Fraction(4, 10)  # Shortfall in feet
work_done_per_person_per_foot = Fraction(1, 1)  # Work done by one person per foot
people_arrived_first = 1000  # Number of people who arrived first
upper_width = Fraction(1, 1)  # Upper width (assumed to be 1 foot)
lower_width = Fraction(1, 1)  # Lower width (assumed to be 1 foot)
depth = Fraction(1, 1)  # Depth (assumed to be 1 foot)

# Calculate the average width
average_width = (upper_width + lower_width) / 2

# Calculate the work done by the first group of people
work_done_by_first_group = work_done_per_person_per_foot * people_arrived_first

# Calculate the length (袤) in feet
a = work_done_by_first_group / (average_width * depth)

# Convert the result to 丈 (1 丈 = 10 尺)
a = a / 10

# Output the result
a


"""


### Explanation:
1. We use the `Fraction` class to ensure precise calculations, especially for non-integer values.
2. The formula for the length (袤) is derived from the problem statement:
   \[
   \text{Length (袤)} = \frac{\text{Work done by the first group}}{\text{Average width} \times \text{Depth}}
   \]
3. The result is converted into 丈 by dividing by 10, as 1 丈 = 10 尺.

### Output:
The variable `a` will contain the length in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 100"""
