"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
- The large mouse digs 1 chi per day and doubles its digging speed every day.
- The small mouse also digs 1 chi per day but halves its digging speed every day.

Question: After how many days do they meet? How much has each mouse dug?

Answer: They meet after *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# Initialize variables
wall_thickness = 5  # Total thickness of the wall in chi
large_mouse_speed = 1  # Initial speed of the large mouse in chi/day
small_mouse_speed = 1  # Initial speed of the small mouse in chi/day
large_mouse_total = 0  # Total distance dug by the large mouse
small_mouse_total = 0  # Total distance dug by the small mouse
days = 0  # Counter for days

# Loop until the two mice meet
while large_mouse_total + small_mouse_total < wall_thickness:
    days += 1
    large_mouse_total += large_mouse_speed
    small_mouse_total += small_mouse_speed
    large_mouse_speed *= 2  # Large mouse doubles its speed
    small_mouse_speed /= 2  # Small mouse halves its speed

# Results
a = days
b = large_mouse_total
c = small_mouse_total

# Output the results
a, b, c
"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 3
Variable 'b' has wrong value. Expected: 59/17, Actual: 7
Variable 'c' has wrong value. Expected: 26/17, Actual: 1.75"""
