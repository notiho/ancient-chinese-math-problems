"""
今有粟七斗八升，欲為豉。問︰得幾何？
術曰：以粟求豉，六十三之，五十而一。
荅曰：為豉 a斗 。
"""

"""
To solve this problem, we are given 7斗8升 of 粟 (grain) and want to determine how much 豉 (fermented beans) can be made. The rule is that for every 63 units of 粟, we get 50 units of 豉.

### Conversion:
1斗 = 10升, so 7斗8升 = \( 7 \times 10 + 8 = 78 \) 升.

### Formula:
The ratio is \( \frac{50}{63} \), meaning for every 63 units of 粟, we get 50 units of 豉.

### Calculation:
Let \( a \) represent the amount of 豉 in 斗. First, calculate the total 豉 in 升, then convert it back to 斗.


"""


from fractions import Fraction

# Given 粟 in 升
粟 = 7 * 10 + 8  # 7斗8升 = 78升

# Ratio of 粟 to 豉
ratio = Fraction(50, 63)

# Calculate 豉 in 升
豉_in_升 = 粟 * ratio

# Convert 豉 to 斗 (1斗 = 10升)
a = 豉_in_升 / 10

# Result
a  # 豉 in 斗


"""


### Final Answer:
The value of \( a \) will be the amount of 豉 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 2457/250, Actual: 130/21"""
