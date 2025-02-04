"""
又有田廣二里，從三里。問：為田幾何？
里田術曰：廣從里數相乘得積里。以三百七十五乘之，即畝數。
荅曰： a頃 。
"""

"""
To solve this problem, we need to calculate the area of the field in terms of "頃" (a unit of area). The problem states that the field is 2 里 wide and 3 里 long. The area in square 里 is calculated by multiplying the width and the length. Then, to convert the area into 畝, we multiply the result by 375 (since 1 square 里 equals 375 畝). Finally, to convert 畝 into 頃, we divide by 100 (since 1 頃 equals 100 畝).

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions of the field
width = Fraction(2)  # 2 里
length = Fraction(3)  # 3 里

# Calculate the area in square 里
area_square_li = width * length

# Convert square 里 to 畝
area_mu = area_square_li * 375

# Convert 畝 to 頃
a = area_mu / 100

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the area of the field in 頃.
"""


"""
"""
