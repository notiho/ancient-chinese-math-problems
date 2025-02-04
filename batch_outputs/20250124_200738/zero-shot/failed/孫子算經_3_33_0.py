"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
術曰：置長女五日，中女四日，少女三日，于右方，各列一算于左方，維乘之，各得所到數。長女十二到，中女十五到，少女二十到，又各以歸日乘到數，即得。
答曰： a日 。
"""

"""
To solve this problem, we need to find the least common multiple (LCM) of the three periods: 5 days, 4 days, and 3 days. The LCM represents the number of days after which all three women will meet again.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Periods for each woman
longest_daughter_period = 5  # Longest daughter's period in days
middle_daughter_period = 4   # Middle daughter's period in days
youngest_daughter_period = 3 # Youngest daughter's period in days

# Compute the LCM of the three periods
a = longest_daughter_period * middle_daughter_period * youngest_daughter_period // (
    Fraction(longest_daughter_period * middle_daughter_period, 
             Fraction(longest_daughter_period, youngest_daughter_period))
)

# The answer is stored in variable 'a'
a  # a is the number of days after which all three women will meet again
#----- content ends here -----


"""


The variable `a` will contain the number of days after which all three women will meet again.
"""


"""
Variable 'a' has wrong value. Expected: 60, Actual: 5"""
