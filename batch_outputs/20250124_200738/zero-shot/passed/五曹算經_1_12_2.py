"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
術曰：并二廣得一百二十六步半之得六十三步以從九十步乘之得五千六百七十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a trapezoidal field (箕田) with one side 86 steps wide, the other side 40 steps wide, and the height (distance between the two parallel sides) 90 steps. The area is then converted into a combination of "畝" (mu) and "步" (steps).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
wide1 = 86  # one side of the trapezoid in steps
wide2 = 40  # the other side of the trapezoid in steps
height = 90  # the height of the trapezoid in steps

# Step 1: Calculate the average width
average_width = Fraction(wide1 + wide2, 2)

# Step 2: Calculate the area in square steps
area_steps = average_width * height

# Step 3: Convert the area into 畝 and 步
# 1 畝 = 240 步
mu = area_steps // 240  # integer part (畝)
bu = area_steps % 240  # remainder (步)

# Assign the results to variables
a = mu
b = bu

# Output the results
a, b
#----- content ends here -----


"""


### Explanation:
1. **Average Width**: The average width of the trapezoid is calculated as the sum of the two parallel sides divided by 2.
2. **Area in Square Steps**: The area of the trapezoid is calculated as the average width multiplied by the height.
3. **Conversion to 畝 and 步**: Since 1 畝 equals 240 square steps, the total area is divided by 240 to get the number of 畝 (integer part), and the remainder gives the number of 步.

### Solution:
The variables `a` and `b` will contain the number of 畝 and 步, respectively.
"""


"""
"""
