"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 5 chi thick, and two mice are digging toward each other from opposite sides.
- The large mouse digs 1 chi per day and doubles its digging speed every day.
- The small mouse also digs 1 chi per day but halves its digging speed every day.

Question: How many days will it take for them to meet? How much will each mouse dig?

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# Wall thickness
wall_thickness = 5

# Initialize variables
large_mouse_speed = 1  # Large mouse starts at 1 chi/day
small_mouse_speed = 1  # Small mouse starts at 1 chi/day
large_mouse_total = 0  # Total distance dug by the large mouse
small_mouse_total = 0  # Total distance dug by the small mouse
days = 0

# Loop until they meet
while large_mouse_total + small_mouse_total < wall_thickness:
    days += 1
    # Add the current day's digging to the total
    large_mouse_total += large_mouse_speed
    small_mouse_total += small_mouse_speed
    # Update speeds for the next day
    large_mouse_speed *= 2  # Large mouse doubles its speed
    small_mouse_speed /= 2  # Small mouse halves its speed

# Results
a = days
b = large_mouse_total
c = small_mouse_total

a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 3
Variable 'b' has wrong value. Expected: 59/17, Actual: 7
Variable 'c' has wrong value. Expected: 26/17, Actual: 1.75"""
