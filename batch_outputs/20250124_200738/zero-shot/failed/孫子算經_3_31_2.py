"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
術曰：置九百里以三百步乘之，得二十七萬步，又以六尺乘之，得一百六十二萬尺，以車輪一丈八尺為法，除之，即得。
答曰： a 匝。
"""

"""
To solve this problem, we need to calculate the number of wheel revolutions (匝) required for a journey of 900 li, given that one revolution of the wheel covers a distance of 1丈8尺. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
distance_li = 900  # in li
li_to_bu = 300  # 1 li = 300 bu
bu_to_chi = 6  # 1 bu = 6 chi
wheel_circumference = Fraction(1, 1) * 10 + Fraction(8, 10)  # 1丈8尺 = 1.8丈

# Convert the distance to chi
distance_chi = distance_li * li_to_bu * bu_to_chi

# Calculate the number of revolutions
a = distance_chi / wheel_circumference

# Result
a
#----- content ends here -----


"""


The variable `a` will contain the number of revolutions (匝).
"""


"""
Variable 'a' has wrong value. Expected: 90000, Actual: 150000"""
