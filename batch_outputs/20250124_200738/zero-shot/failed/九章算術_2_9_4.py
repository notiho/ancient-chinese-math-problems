"""
今有粟九斗八升，欲為御飯。問︰得幾何？
術曰：以粟求御飯，二十一之，二十五而一。
荅曰：為御飯 a斗 。
"""

"""
To solve this problem, we need to calculate the amount of "御飯" (cooked rice) that can be made from 9斗8升 of raw rice (粟). The problem states that the ratio is 21:25, meaning 21 units of raw rice yield 25 units of cooked rice.

### Steps:
1. Convert 9斗8升 into a single unit (斗). Since 1斗 = 10升, 9斗8升 = 9 + 8/10 = 9.8斗.
2. Use the ratio 21:25 to compute the amount of cooked rice. Multiply the amount of raw rice by 25/21.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given raw rice in 斗
raw_rice = Fraction(9, 1) + Fraction(8, 10)  # 9斗8升 = 9.8斗

# Ratio of raw rice to cooked rice is 21:25
ratio = Fraction(25, 21)

# Calculate the amount of cooked rice
a = raw_rice * ratio  # a斗 of cooked rice
#----- content ends here -----


"""


### Final Answer:
The variable `a` will contain the amount of cooked rice in 斗, represented as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 1029/125, Actual: 35/3"""
