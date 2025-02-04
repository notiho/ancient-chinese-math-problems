"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
術曰：置長女五日，中女四日，少女三日，于右方，各列一算于左方，維乘之，各得所到數。長女十二到，中女十五到，少女二十到，又各以歸日乘到數，即得。
答曰： a日 。
"""

"""
To solve this problem, we need to find the least common multiple (LCM) of the three periods: 5 days for the eldest daughter, 4 days for the middle daughter, and 3 days for the youngest daughter. The LCM will give us the number of days after which all three daughters will meet again.

Here is the Python code to compute the answer:


"""


from fractions import Fraction

# Periods for each daughter
longest_daughter_period = 5
middle_daughter_period = 4
youngest_daughter_period = 3

# Compute the LCM of the three periods
def lcm(x, y):
    return x * y // gcd(x, y)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a = lcm(lcm(longest_daughter_period, middle_daughter_period), youngest_daughter_period)

# The answer is stored in variable 'a'
a  # a is the number of days when all three daughters meet


"""


The variable `a` will contain the number of days after which all three daughters will meet again.
"""


"""
"""
