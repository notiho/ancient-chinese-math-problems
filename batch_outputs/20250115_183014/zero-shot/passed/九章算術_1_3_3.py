"""
又有田廣二里，從三里。問：為田幾何？
里田術曰：廣從里數相乘得積里。以三百七十五乘之，即畝數。
荅曰： a頃 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
width = Fraction(2)  # 2 里
length = Fraction(3)  # 3 里

# Calculate the area in 里^2
area_li2 = width * length

# Convert the area to 畝 using the conversion factor (1 里^2 = 375 畝)
area_mu = area_li2 * 375

# Convert 畝 to 頃 (1 頃 = 100 畝)
a = area_mu / 100

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the area of the field in 頃.
"""


"""
"""
