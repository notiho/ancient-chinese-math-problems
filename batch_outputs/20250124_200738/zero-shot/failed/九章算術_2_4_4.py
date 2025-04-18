"""
今有粟一斗，欲為小䵂。問︰得幾何？
術曰：以粟求小䵂，二十七之，百而一。
荅曰：為小䵂 a升 。
"""

"""
To solve this problem, we need to calculate how many "升" (shēng) of "小䵂" (xiǎo lǔ) can be obtained from 1 "斗" (dǒu) of "粟" (sù). The method provided states that we multiply the amount of "粟" by 27 and then divide by 100.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
粟 = 1  # 1 斗

# Calculation
a = Fraction(粟 * 27, 100)  # Convert 粟 to 小䵂

# Result
a  # a is the amount of 小䵂 in 升
#----- content ends here -----


"""


The variable `a` will contain the result in terms of "升".
"""


"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 27/100"""
