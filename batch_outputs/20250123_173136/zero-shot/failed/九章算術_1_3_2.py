"""
又有田廣二里，從三里。問：為田幾何？
里田術曰：廣從里數相乘得積里。以三百七十五乘之，即畝數。
荅曰： a頃 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a field given its width (廣) and length (從), both measured in "里" (Chinese miles). The area is then converted into "畝" (a traditional Chinese unit of area) by multiplying the result by 375.

Here is the Python code:


"""


from fractions import Fraction

# Given data
width = Fraction(2)  # 廣二里 (2 里)
length = Fraction(3)  # 從三里 (3 里)

# Calculate the area in square 里
area_in_li = width * length  # 廣從里數相乘得積里

# Convert the area into 畝 (1 square 里 = 375 畝)
a = area_in_li * 375  # 以三百七十五乘之，即畝數

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the area of the field in 畝.
"""


"""
Variable 'a' has wrong value. Expected: 45/2, Actual: 2250"""
