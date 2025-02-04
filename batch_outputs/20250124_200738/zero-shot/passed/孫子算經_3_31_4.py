"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
術曰：置九百里以三百步乘之，得二十七萬步，又以六尺乘之，得一百六十二萬尺，以車輪一丈八尺為法，除之，即得。
答曰： a 匝。
"""

"""
To solve this problem, we need to calculate how many revolutions ("匝") the wheel makes when traveling from 洛陽 (Luoyang) to 長安 (Chang'an). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
distance_in_li = 900  # Distance between 洛陽 and 長安 in li
li_to_bu = 300  # 1 li = 300 bu
bu_to_chi = 6  # 1 bu = 6 chi
wheel_circumference = Fraction(1, 1) * 18  # Wheel circumference in chi (1丈8尺 = 18尺)

# Convert distance to chi
distance_in_bu = distance_in_li * li_to_bu  # Convert li to bu
distance_in_chi = distance_in_bu * bu_to_chi  # Convert bu to chi

# Calculate the number of revolutions
a = distance_in_chi / wheel_circumference  # Number of revolutions

# Result
a
#----- content ends here -----


"""


The variable `a` will contain the number of revolutions the wheel makes.
"""


"""
"""
