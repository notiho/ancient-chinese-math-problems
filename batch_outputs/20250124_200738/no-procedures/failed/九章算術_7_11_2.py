"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
- The large mouse digs 1 chi per day, and its daily digging doubles each day.
- The small mouse also digs 1 chi per day, but its daily digging halves each day.

Question: How many days will it take for them to meet? How much will each mouse dig?

Answer: It takes *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# Wall thickness
wall_thickness = 5

# Initialize variables
large_mouse_digging_rate = 1  # Large mouse starts with 1 chi/day
small_mouse_digging_rate = 1  # Small mouse starts with 1 chi/day
large_mouse_total = 0  # Total distance dug by the large mouse
small_mouse_total = 0  # Total distance dug by the small mouse
days = 0

# Loop until the total distance dug by both mice equals or exceeds the wall thickness
while large_mouse_total + small_mouse_total < wall_thickness:
    days += 1
    large_mouse_total += large_mouse_digging_rate
    small_mouse_total += small_mouse_digging_rate
    large_mouse_digging_rate *= 2  # Large mouse doubles its digging rate each day
    small_mouse_digging_rate /= 2  # Small mouse halves its digging rate each day

# Results
a = days
b = large_mouse_total
c = small_mouse_total

# Output results
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 3
Variable 'b' has wrong value. Expected: 59/17, Actual: 7
Variable 'c' has wrong value. Expected: 26/17, Actual: 1.75"""
