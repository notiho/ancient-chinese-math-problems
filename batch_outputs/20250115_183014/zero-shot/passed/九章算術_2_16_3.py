"""
今有粟五斗五升，欲為飧。問︰得幾何？
術曰：以粟求飧，九之，五而一。
荅曰：為飧 a斗 。
"""

"""
To solve this problem, we need to calculate the amount of "飧" (a type of food) that can be made from 5斗5升 of 粟 (grain). The method provided in the problem states that to convert 粟 to 飧, we multiply the amount of 粟 by 9 and then divide by 5.

### Units:
- 1斗 = 10升 (this is a standard conversion in ancient Chinese measurements).

### Steps:
1. Convert 5斗5升 into a single unit (升).
2. Apply the formula: multiply the total amount of 粟 by 9 and divide by 5.
3. Convert the result back into 斗.

Here is the Python code:


"""


from fractions import Fraction

# Step 1: Convert 5斗5升 into 升
total_grain_in_sheng = 5 * 10 + 5  # 1斗 = 10升

# Step 2: Calculate 飧 using the formula (粟 * 9) / 5
total_sun_in_sheng = Fraction(total_grain_in_sheng * 9, 5)

# Step 3: Convert the result back into 斗
a = total_sun_in_sheng / 10  # 1斗 = 10升

# The result is stored in variable 'a'


"""


### Final Answer:
The variable `a` contains the amount of 飧 in 斗, represented as a `Fraction`.
"""


"""
"""
