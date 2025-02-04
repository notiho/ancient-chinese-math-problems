"""
今有粟五斗五升，欲為飧。問︰得幾何？
術曰：以粟求飧，九之，五而一。
荅曰：為飧 a斗 。
"""

"""
To solve this problem, we need to translate the ancient Chinese math problem into Python code. The problem states that we have 5斗5升 of 粟 (grain), and we want to calculate how much 飧 (cooked grain) we can get. The method provided is to multiply the amount of 粟 by 9 and then divide by 5.

In ancient Chinese units:
- 1斗 = 10升.

Thus, 5斗5升 = 5 * 10 + 5 = 55升.

The formula is:
飧 = 粟 * 9 / 5.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given 粟 (grain) in 斗 and 升
粟_in_斗 = 5
粟_in_升 = 5

# Convert 粟 to total 升
total_粟_in_升 = 粟_in_斗 * 10 + 粟_in_升

# Calculate 飧 (cooked grain) in 斗
a = Fraction(total_粟_in_升 * 9, 5) / 10  # Convert back to 斗

# Output the result
a  # This is the amount of 飧 in 斗
#----- content ends here -----


"""


The variable `a` will contain the solution in 斗 as a `Fraction`.
"""


"""
"""
