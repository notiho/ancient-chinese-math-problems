"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
術曰：置角至桑一百四十七步，倍之，得二百九十四步，以五乘之，得一千四百七十步，以七除之，得二百一十步，自相乘，得四萬四千一百步，以二百四十步除之，即得。
答曰： a頃 ，奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a square field with a central mulberry tree, given the distance from a corner to the tree. The solution involves a series of operations described in the problem.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
corner_to_tree = 147  # in steps

# Step-by-step calculations
doubled_distance = corner_to_tree * 2  # 294 steps
multiplied_by_five = doubled_distance * 5  # 1470 steps
divided_by_seven = Fraction(multiplied_by_five, 7)  # 210 steps
area_in_steps = divided_by_seven ** 2  # 44100 steps^2
area_in_qing = Fraction(area_in_steps, 240)  # 44100 / 240

# Extracting the integer part (a) and the remainder (b)
a = area_in_qing.numerator // area_in_qing.denominator  # integer part in qing
b = area_in_qing.numerator % area_in_qing.denominator  # remainder in steps

# Results
a  # in qing
b  # in steps
#----- content ends here -----


"""


### Explanation:
1. The distance from the corner to the tree is doubled.
2. The result is multiplied by 5.
3. The result is divided by 7.
4. The square of the result gives the area in steps squared.
5. The area is converted to qing by dividing by 240 (since 1 qing = 240 steps squared).
6. The integer part of the result is the number of qing (`a`), and the remainder is the number of steps (`b`).

### Final Answer:
- `a` is the area in qing.
- `b` is the remainder in steps.
"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 183
Variable 'b' has wrong value. Expected: 180, Actual: 3"""
