"""
今有糲飯七斗六升、七分升之四，欲為飧。問︰得幾何？
術曰：以糲飯求飧，六之，五而一。
荅曰：為飧 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting 糲飯 (coarse rice) into 飧 (cooked rice). The rule provided is "六之，五而一," which means for every 6 parts of 糲飯, you get 5 parts of 飧.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# 糲飯 (coarse rice) given in the problem
糲飯 = Fraction(7, 1) + Fraction(6, 10) + Fraction(4, 70)  # 7斗6升4/7升

# Conversion rule: for every 6 parts of 糲飯, you get 5 parts of 飧
a = 糲飯 * Fraction(5, 6)  # Calculate 飧 (cooked rice)

# The answer is stored in variable 'a'
a  # This represents the amount of 飧 in 斗
#----- content ends here -----


"""


### Explanation:
1. The given amount of 糲飯 is 7斗6升4/7升. Since 1斗 = 10升, we convert everything into a fraction of 斗:
   - 7斗 = 7
   - 6升 = 6/10斗
   - 4/7升 = 4/(7*10)斗
   - Total 糲飯 = 7 + 6/10 + 4/(7*10)

2. The conversion rule "六之，五而一" means for every 6 parts of 糲飯, you get 5 parts of 飧. This is represented as multiplying by the fraction 5/6.

3. The result is stored in the variable `a`, which represents the amount of 飧 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 1608/175, Actual: 134/21"""
