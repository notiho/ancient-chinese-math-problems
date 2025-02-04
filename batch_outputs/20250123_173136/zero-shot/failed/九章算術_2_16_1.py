"""
今有粟五斗五升，欲為飧。問︰得幾何？
術曰：以粟求飧，九之，五而一。
荅曰：為飧 a斗 。
"""

"""
To solve this problem, we will follow the instructions provided in the text. The problem states that we have 5斗5升 of 粟 (grain) and we want to calculate how much 飧 (cooked food) can be made. The method ("術") says to multiply the amount of 粟 by 9 and then divide by 5.

### Assumptions:
1. 1斗 = 10升 (standard ancient Chinese volume units).
2. The total amount of 粟 is converted into 升 for calculation.

### Python Code:

"""


from fractions import Fraction

# Given data
grain_in_dou = 5  # 斗
grain_in_sheng = 5  # 升

# Convert everything to 升
total_grain_in_sheng = grain_in_dou * 10 + grain_in_sheng  # 1斗 = 10升

# Calculation: multiply by 9 and divide by 5
a = Fraction(total_grain_in_sheng * 9, 5)  # Result in 升

# Convert result back to 斗 and 升
a_dou = a // 10  # Whole number of 斗
a_sheng = a % 10  # Remaining 升

# Output the result
a = (a_dou, a_sheng)  # Representing the result as (斗, 升)


"""


### Explanation:
1. Convert the given 粟 (grain) into 升 for easier calculation.
2. Multiply the total grain by 9 and divide by 5 as per the method.
3. Convert the result back into 斗 and 升 for the final answer.

### Final Answer:
The variable `a` will contain the result as a tuple `(斗, 升)`.
"""


"""
Variable 'a' has wrong value. Expected: 99/10, Actual: (9, Fraction(9, 1))"""
