"""
今有麥一斗，欲為大䵂。問︰得幾何？
術曰：以麥求大䵂，六之，五而一。
荅曰：為大䵂 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that to convert one "斗" of wheat into "大䵂," you multiply by 6 and then divide by 5. Let's compute the value of "a" (the amount of "大䵂" obtained).


"""

#----- content starts here -----

from fractions import Fraction

# Given data
wheat = Fraction(1)  # 1 斗 of wheat

# Conversion formula: multiply by 6 and divide by 5
a = wheat * Fraction(6, 5)

# The result is stored in variable 'a'
a  # a斗 of 大䵂
#----- content ends here -----


"""


The variable `a` will hold the result as a fraction, representing the amount of "大䵂" obtained from 1 "斗" of wheat.
"""


"""
"""
