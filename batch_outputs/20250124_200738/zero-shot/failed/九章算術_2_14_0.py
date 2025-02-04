"""
今有粟七斗五升、七分升之四，欲為稻。問︰得幾何？
術曰：以粟求稻，六之，五而一。
荅曰：為稻 a斗 。
"""

"""
To solve this problem, we need to convert the given amount of 粟 (millet) into 稻 (rice) using the given ratio. The ratio provided is "六之，五而一," which means for every 6 units of 粟, we get 5 units of 稻.

The given amount of 粟 is 7斗5升4/7升. Let's compute the equivalent amount of 稻.


"""

#----- content starts here -----

from fractions import Fraction

# Given amount of 粟
粟 = 7 + Fraction(5, 10) + Fraction(4, 70)  # 7斗5升4/7升

# Conversion ratio: 6 units of 粟 -> 5 units of 稻
稻 = 粟 * Fraction(5, 6)

# Assign the result to variable 'a'
a = 稻

# Output the result
a
#----- content ends here -----


"""


The variable `a` will contain the amount of 稻 in terms of 斗.
"""


"""
Variable 'a' has wrong value. Expected: 1587/175, Actual: 529/84"""
