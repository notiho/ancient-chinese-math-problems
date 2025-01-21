"""
今有粟二斗一升，欲為粺米。問︰得幾何？
術曰：以粟求粺米，二十七之，五十而一。
荅曰：為粺米 a斗 。
"""

"""
To solve this problem, we will calculate the amount of 粺米 (refined rice) obtained from 粟 (unrefined grain). The problem states that for every 50 units of 粟, 27 units of 粺米 are produced. The given amount of 粟 is 2斗1升, where 1斗 = 10升. 

### Steps:
1. Convert the given amount of 粟 (2斗1升) entirely into 升.
2. Use the ratio 27:50 (粺米:粟) to calculate the amount of 粺米.
3. Convert the result back into 斗 and 升.

Here is the Python code:


"""


from fractions import Fraction

# Given data
粟_in_斗 = 2
粟_in_升 = 1
total_粟_in_升 = 粟_in_斗 * 10 + 粟_in_升  # Convert 粟 to 升

# Ratio of 粺米 to 粟
ratio_粺米_to_粟 = Fraction(27, 50)

# Calculate 粺米 in 升
粺米_in_升 = total_粟_in_升 * ratio_粺米_to_粟

# Convert 粺米 back to 斗 and 升
a斗 = 粺米_in_升 // 10  # Whole number of 斗
remaining_升 = 粺米_in_升 % 10  # Remaining 升

# Final result
a = (a斗, remaining_升)  # a is represented as (斗, 升)


"""


### Explanation of the result:
- `a斗` gives the whole number of 斗 of 粺米.
- `remaining_升` gives the leftover 升 of 粺米.
- The final result `a` is expressed as a tuple `(斗, 升)`.


"""


"""
Variable 'a' has wrong value. Expected: 567/500, Actual: (1, Fraction(67, 50))"""
