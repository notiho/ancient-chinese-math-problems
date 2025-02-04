"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 15斗 of 粟 among five ranks of people (大夫, 不更, 簪裹, 上造, 公士) in a proportional manner, and then adjusting for an additional 大夫 who also receives 5斗. The solution involves calculating the amount of 粟 each rank contributes.

Here is the Python code:


"""


from fractions import Fraction

# Total 粟 to be distributed
total_corn = 15  # in 斗

# Additional 大夫 receiving 5斗
additional_corn = 5  # in 斗

# Number of ranks
ranks = 5

# Calculate the proportional distribution
# Each rank contributes equally to the adjustment
adjustment_factor = total_corn + additional_corn  # 15 + 5 = 20
unit_contribution = Fraction(1, adjustment_factor)  # Each unit contributes 1/20 of the total

# Calculate the contribution of each rank
a = unit_contribution * 5  # 大夫
b = unit_contribution * 4  # 不更
c = unit_contribution * 3  # 簪裹
d = unit_contribution * 2  # 上造
e = unit_contribution * 1  # 公士

# Print the results
a, b, c, d, e


"""


### Explanation:
1. **Total 粟**: The total 粟 to be distributed is 15斗.
2. **Adjustment Factor**: The additional 大夫 receiving 5斗 increases the total to 20斗.
3. **Unit Contribution**: Each rank contributes proportionally based on their rank (5 for 大夫, 4 for 不更, etc.).
4. **Fraction Representation**: The `Fraction` class ensures accurate representation of non-integer values.

### Results:
The variables `a`, `b`, `c`, `d`, and `e` represent the contributions of 大夫, 不更, 簪裹, 上造, and 公士, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 5/4, Actual: 1/4
Variable 'b' has wrong value. Expected: 1, Actual: 1/5
Variable 'c' has wrong value. Expected: 3/4, Actual: 3/20
Variable 'd' has wrong value. Expected: 1/2, Actual: 1/10
Variable 'e' has wrong value. Expected: 1/4, Actual: 1/20"""
