"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
術曰：置長女五日，中女四日，少女三日，于右方，各列一算于左方，維乘之，各得所到數。長女十二到，中女十五到，少女二十到，又各以歸日乘到數，即得。
答曰： a日 。
"""

#----- content starts here -----
"""
Suppose there are three daughters. 
The eldest daughter returns home every 5 days, the middle daughter every 4 days, and the youngest daughter every 3 days.
Question: after how many days will all three daughters meet at home?

The procedure says: Place the eldest daughter's 5 days, the middle daughter's 4 days, and the youngest daughter's 3 days on the right side.
For each, place a counter on the left side.
Take the product of the other two numbers for each daughter, obtaining their respective "arrival numbers."
The eldest daughter's arrival number is 12, the middle daughter's is 15, and the youngest daughter's is 20.
Then, multiply each arrival number by the respective return period, and sum them.
Finally, divide the sum by the least common multiple of the return periods to obtain the answer.

Answer: *a* days.
"""

from math import gcd
from fractions import Fraction

# 長女五日一歸，中女四日一歸，少女三日一歸
長女 = 5
中女 = 4
少女 = 3

# 計算三個數的最小公倍數 (LCM)
def lcm(x, y):
    return x * y // gcd(x, y)

# 三個數的最小公倍數
歸日_lcm = lcm(lcm(長女, 中女), 少女)

# 各自的到數
長女到數 = 中女 * 少女  # 4 * 3 = 12
中女到數 = 長女 * 少女  # 5 * 3 = 15
少女到數 = 長女 * 中女  # 5 * 4 = 20

# 各以歸日乘到數
長女貢獻 = 長女到數 * 長女  # 12 * 5
中女貢獻 = 中女到數 * 中女  # 15 * 4
少女貢獻 = 少女到數 * 少女  # 20 * 3

# 總和
總和 = 長女貢獻 + 中女貢獻 + 少女貢獻

# 最終答案
a = Fraction(總和, 歸日_lcm)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60, Actual: 3"""
