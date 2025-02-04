"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
術曰：置長女五日，中女四日，少女三日，于右方，各列一算于左方，維乘之，各得所到數。長女十二到，中女十五到，少女二十到，又各以歸日乘到數，即得。
答曰： a日 。
"""

"""
To solve this problem, we need to find the least common multiple (LCM) of the three periods: 5 days, 4 days, and 3 days. This will give us the number of days after which all three daughters will meet again.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Periods for the three daughters
long_daughter = 5  # Long daughter's period in days
middle_daughter = 4  # Middle daughter's period in days
young_daughter = 3  # Young daughter's period in days

# Compute the LCM of the three periods
a = long_daughter * middle_daughter * young_daughter // (
    Fraction(long_daughter * middle_daughter, long_daughter).denominator
    * Fraction(long_daughter * young_daughter, long_daughter).denominator
    * Fraction(middle_daughter * young_daughter, middle_daughter).denominator
)

# The answer is stored in variable 'a'
a  # a is the number of days after which all three daughters meet
#----- content ends here -----


"""


The value of `a` will be the number of days after which all three daughters meet.
"""


"""
"""
