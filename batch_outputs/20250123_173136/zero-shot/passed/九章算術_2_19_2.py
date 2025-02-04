"""
今有糲米十五斗五升、五分升之二，欲為粟。問︰得幾何？
術曰：以糲米求粟，五之，三而一。
荅曰：為粟 a斗 。
"""

"""
To solve this problem, we need to convert the given amount of 糲米 (hulled rice) into 粟 (millet). The rule provided is: "五之，三而一," which means multiply by 5 and then divide by 3.

The given amount of 糲米 is **15斗 5升 2/5升**. Let's first convert everything into a single unit (升, or sheng), then perform the calculation.

1 斗 = 10 升.

### Python Code:

"""


from fractions import Fraction

# Given 糲米 in terms of 斗, 升, and 分升
斗 = 15
升 = 5
分升 = Fraction(2, 5)

# Convert everything to 升
total_升 = 斗 * 10 + 升 + 分升

# Conversion rule: multiply by 5, then divide by 3
a = total_升 * 5 / 3

# Result in terms of 斗
a = Fraction(a) / 10  # Convert back to 斗

# a is the amount of 粟 in 斗
a斗 = a


"""


### Explanation:
1. Convert the given 糲米 into a single unit (升).
2. Apply the conversion rule: multiply by 5 and divide by 3.
3. Convert the result back into 斗.

The variable `a斗` will contain the amount of 粟 in 斗 as a `Fraction`.
"""


"""
"""
