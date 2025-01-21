"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
Suppose there is a wall 5 chi thick. Two mice are digging toward each other from opposite sides.
- The large mouse digs 1 chi per day and doubles its progress each day.
- The small mouse also digs 1 chi per day but halves its progress each day.

Question: After how many days do they meet? How much does each mouse dig?

Answer: They meet after *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# Initialize variables
wall_thickness = 5  # Total thickness of the wall in chi
large_mouse_progress = 0  # Distance dug by the large mouse
small_mouse_progress = 0  # Distance dug by the small mouse
large_mouse_daily = 1  # Initial daily progress of the large mouse
small_mouse_daily = 1  # Initial daily progress of the small mouse
days = 0  # Counter for the number of days

# Loop until the two mice meet
while large_mouse_progress + small_mouse_progress < wall_thickness:
    days += 1
    large_mouse_progress += large_mouse_daily
    small_mouse_progress += small_mouse_daily
    large_mouse_daily *= 2  # Large mouse doubles its daily progress
    small_mouse_daily /= 2  # Small mouse halves its daily progress

# Results
a = days
b = large_mouse_progress
c = small_mouse_progress
"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 3
Variable 'b' has wrong value. Expected: 59/17, Actual: 7
Variable 'c' has wrong value. Expected: 26/17, Actual: 1.75"""
