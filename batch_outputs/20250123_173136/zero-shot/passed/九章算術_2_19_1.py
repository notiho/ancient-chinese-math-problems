"""
今有糲米十五斗五升、五分升之二，欲為粟。問︰得幾何？
術曰：以糲米求粟，五之，三而一。
荅曰：為粟 a斗 。
"""

"""
To solve this problem, we need to compute the amount of 粟 (a) that can be obtained from 糲米. The problem states that the conversion is done by multiplying the amount of 糲米 by 5 and then dividing by 3.

The given amount of 糲米 is 15斗 5升 2/5升. We need to convert this into a single unit (斗) and then apply the conversion formula.

Here is the Python code:


"""


from fractions import Fraction

# Given amount of 糲米
liangmi = 15 + Fraction(5, 10) + Fraction(2, 10 * 5)  # Convert 5升 and 2/5升 into fractions of 斗

# Conversion formula: multiply by 5 and divide by 3
a = liangmi * 5 / 3

# Result
a  # The amount of 粟 in 斗


"""


The variable `a` will contain the result in terms of 斗.
"""


"""
"""
