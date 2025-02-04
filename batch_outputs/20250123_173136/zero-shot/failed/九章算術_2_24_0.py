"""
今有糲米一十九斗二升、七分升之一，欲為粺米。問︰得幾何？
術曰：以糲米求粺米，九之，十而一。
荅曰：為粺米 a斗 。
"""

"""
To solve this problem, we need to convert 糲米 (coarse rice) into 粺米 (polished rice). The rule provided states that for every 10 units of 糲米, 9 units of 粺米 are obtained. The given amount of 糲米 is 19斗 (dou), 2升 (sheng), and 1/7升.

### Conversion:
1 斗 = 10 升.

Thus, the total amount of 糲米 in 升 is:
\[ \text{Total 糲米 in 升} = 19 \times 10 + 2 + \frac{1}{7} \]

The conversion rule is:
\[ \text{粺米 in 升} = \text{糲米 in 升} \times \frac{9}{10} \]

Finally, convert the result back into 斗 and 升.

Here is the Python code:


"""


from fractions import Fraction

# 糲米 in 斗, 升, and fraction of 升
liangmi_dou = 19
liangmi_sheng = 2
liangmi_fraction_sheng = Fraction(1, 7)

# Convert 糲米 to total 升
liangmi_total_sheng = liangmi_dou * 10 + liangmi_sheng + liangmi_fraction_sheng

# Conversion ratio from 糲米 to 粺米
conversion_ratio = Fraction(9, 10)

# Calculate 粺米 in 升
baimi_total_sheng = liangmi_total_sheng * conversion_ratio

# Convert 粺米 back to 斗 and 升
a_dou = baimi_total_sheng // 10  # Whole 斗
a_sheng = baimi_total_sheng % 10  # Remaining 升

# Final result
a = (a_dou, a_sheng)  # a is represented as (斗, 升)


"""


### Explanation:
- `liangmi_total_sheng` computes the total amount of 糲米 in 升.
- `baimi_total_sheng` calculates the equivalent amount of 粺米 in 升 using the conversion ratio.
- The result is then split into 斗 and 升 for the final answer.

### Output:
The variable `a` contains the result as a tuple `(斗, 升)`.
"""


"""
Variable 'a' has wrong value. Expected: 2421/140, Actual: (17, Fraction(41, 14))"""
