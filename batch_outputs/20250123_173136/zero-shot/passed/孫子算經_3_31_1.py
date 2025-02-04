"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
術曰：置九百里以三百步乘之，得二十七萬步，又以六尺乘之，得一百六十二萬尺，以車輪一丈八尺為法，除之，即得。
答曰： a 匝。
"""

"""
To solve this problem, we need to calculate how many revolutions ("匝") the wheel makes when traveling from 洛陽 (Luoyang) to 長安 (Chang'an). Here's the Python code:


"""


from fractions import Fraction

# Given data
distance_in_li = 900  # 900 li
steps_per_li = 300  # 1 li = 300 steps
feet_per_step = 6  # 1 step = 6 feet
wheel_circumference = Fraction(1, 1) * 18  # 1丈8尺 = 18 feet

# Convert the distance to feet
total_steps = distance_in_li * steps_per_li  # Total steps
total_feet = total_steps * feet_per_step  # Total feet

# Calculate the number of revolutions
a = total_feet / wheel_circumference  # Number of revolutions

# The result
a


"""


The variable `a` will contain the number of revolutions (匝).
"""


"""
"""
