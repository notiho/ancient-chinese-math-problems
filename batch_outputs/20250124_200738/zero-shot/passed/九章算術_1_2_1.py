"""
今有田廣一里，從一里。問：為田幾何？
里田術曰：廣從里數相乘得積里。以三百七十五乘之，即畝數。
荅曰： a頃 。
"""

"""
To solve this problem, we need to calculate the area of the field in terms of "頃" (a traditional Chinese unit of area). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
廣 = Fraction(1)  # 1 里
從 = Fraction(1)  # 1 里

# Calculate the area in square 里
積里 = 廣 * 從  # Area in square 里

# Convert square 里 to 畝
畝數 = 積里 * Fraction(375)

# Convert 畝 to 頃 (1 頃 = 100 畝)
a = 畝數 / Fraction(100)

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` now contains the area of the field in terms of "頃".
"""


"""
"""
