"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
- The big mouse digs 1 chi per day and doubles its progress daily.
- The small mouse also digs 1 chi per day but halves its progress daily.

Question: After how many days do they meet? How much has each mouse dug?

Answer: They meet after *a* days. The big mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# Wall thickness
wall_thickness = 5

# Initialize variables
big_mouse_progress = 0
small_mouse_progress = 0
day = 0

# Loop until they meet
while big_mouse_progress + small_mouse_progress < wall_thickness:
    day += 1
    # Big mouse doubles its progress daily
    big_mouse_progress += 1 * (2 ** (day - 1))
    # Small mouse halves its progress daily
    small_mouse_progress += 1 * (Fraction(1, 2) ** (day - 1))

# Results
a = day
b = big_mouse_progress
c = small_mouse_progress

a, b, c
"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 3
Variable 'b' has wrong value. Expected: 59/17, Actual: 7
Variable 'c' has wrong value. Expected: 26/17, Actual: 7/4"""
