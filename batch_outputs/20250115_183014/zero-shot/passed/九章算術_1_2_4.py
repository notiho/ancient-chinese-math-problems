"""
今有田廣一里，從一里。問：為田幾何？
里田術曰：廣從里數相乘得積里。以三百七十五乘之，即畝數。
荅曰： a頃 。
"""

"""
To solve this problem, we need to calculate the area of a field given its dimensions. The problem states that the field is 1 li (里) wide and 1 li (里) long. The area in li² is then converted to mu (畝) using the conversion factor provided: 1 li² = 375 mu.

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Dimensions of the field in li
width = Fraction(1)  # 1 li
length = Fraction(1)  # 1 li

# Area in li²
area_li_squared = width * length

# Conversion factor: 1 li² = 375 mu
area_mu = area_li_squared * 375

# Conversion from mu to qing: 1 qing = 100 mu
a = area_mu / 100  # Area in qing

# Result
a  # This is the answer in qing


"""


The variable `a` will contain the area of the field in qing (頃).
"""


"""
"""
