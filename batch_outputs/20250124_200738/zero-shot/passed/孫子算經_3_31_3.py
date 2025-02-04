"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
術曰：置九百里以三百步乘之，得二十七萬步，又以六尺乘之，得一百六十二萬尺，以車輪一丈八尺為法，除之，即得。
答曰： a 匝。
"""

"""
To solve this problem, we need to calculate how many revolutions ("匝") the wheel makes when traveling from 洛陽 (Luoyang) to 長安 (Chang'an), which are 900 li apart. The wheel's circumference is given as 1丈8尺 (1 zhang 8 chi). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
distance_li = 900  # Distance in li
li_to_bu = 300  # 1 li = 300 bu
bu_to_chi = 6  # 1 bu = 6 chi
wheel_circumference_chi = 1 * 10 + 8  # 1 zhang = 10 chi, so 1 zhang 8 chi = 18 chi

# Convert distance to chi
distance_chi = distance_li * li_to_bu * bu_to_chi

# Calculate the number of revolutions
a = Fraction(distance_chi, wheel_circumference_chi)

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the number of revolutions (匝) as a `Fraction`.
"""


"""
"""
