"""
今有粺米二斗，欲為粟。問︰得幾何？
術曰：以粺米求粟，五十之，二十七而一。
荅曰：為粟 a斗 。
"""

"""
To solve this problem, we need to convert 粺米 (refined rice) into 粟 (unrefined rice). The rule provided is: multiply the amount of 粺米 by 50 and then divide by 27 to get the equivalent amount of 粟.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

粺米 = Fraction(2)  # 粺米 is given as 2 斗
a = 粺米 * 50 / 27  # Multiply by 50 and divide by 27 to get 粟
#----- content ends here -----


"""


The value of `a` will represent the amount of 粟 in 斗.
"""


"""
"""
