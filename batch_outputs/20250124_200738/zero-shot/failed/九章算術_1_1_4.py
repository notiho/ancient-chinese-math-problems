"""
又有田廣十二步，從十四步。問：為田幾何？
方田術曰：廣從步數相乘得積步。以畝法二百四十步除之，即畝數。百畝為一頃。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the area of a rectangular field given its length (廣) and width (從), and then convert the area into 畝 (a traditional Chinese unit of land measurement). The formula provided in the problem is:

1. Multiply the length (廣) and width (從) to get the area in square steps (積步).
2. Divide the area by 240 to convert it into 畝.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions of the field
廣 = 12  # length in steps
從 = 14  # width in steps

# Calculate the area in square steps
積步 = 廣 * 從

# Convert the area into 畝
a = Fraction(積步, 240)

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will represent the area of the field in 畝.
"""


"""
Variable 'a' has wrong value. Expected: 168, Actual: 7/10"""
