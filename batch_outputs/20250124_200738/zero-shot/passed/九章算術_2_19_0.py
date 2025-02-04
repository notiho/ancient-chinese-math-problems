"""
今有糲米十五斗五升、五分升之二，欲為粟。問︰得幾何？
術曰：以糲米求粟，五之，三而一。
荅曰：為粟 a斗 。
"""

"""
To solve this problem, we need to convert 糲米 (hulled rice) into 粟 (millet). The rule provided states: "以糲米求粟，五之，三而一," which means multiply the amount of 糲米 by 5 and then divide by 3.

The given amount of 糲米 is 15斗5升2/5升. Let's calculate the equivalent amount of 粟.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# 糲米 amount in terms of 斗, 升, and 分升
liangmi = 15 + Fraction(5, 10) + Fraction(2, 10 * 5)  # 15斗5升2/5升

# Conversion rule: multiply by 5 and divide by 3
a = liangmi * 5 / 3  # 粟 in 斗

# Result
a  # 粟 in 斗
#----- content ends here -----


"""


The variable `a` will contain the amount of 粟 in 斗.
"""


"""
"""
