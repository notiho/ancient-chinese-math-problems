"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
術曰：置長女五日，中女四日，少女三日，于右方，各列一算于左方，維乘之，各得所到數。長女十二到，中女十五到，少女二十到，又各以歸日乘到數，即得。
答曰： a日 。
"""

"""
To solve this problem, we need to find the least common multiple (LCM) of the three periods: 5 days, 4 days, and 3 days. The LCM will represent the number of days after which all three daughters will meet again.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Periods for each daughter
longest_daughter = 5  # Longest daughter returns every 5 days
middle_daughter = 4   # Middle daughter returns every 4 days
youngest_daughter = 3 # Youngest daughter returns every 3 days

# Compute the LCM of the three periods
a = longest_daughter * middle_daughter * youngest_daughter // (
    Fraction(longest_daughter, Fraction(middle_daughter youngest_daughter#----- content ends here -----


"""

"""


"""
Code error: '(' was never closed (<string>, line 12)"""
