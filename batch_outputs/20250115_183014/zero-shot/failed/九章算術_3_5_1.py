"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 15斗 of 粟 among five ranks of people (大夫, 不更, 簪裹, 上造, 公士) in a proportional manner. Additionally, one more 大夫 arrives later and receives 5斗, making the total 20斗. The solution involves calculating the proportional contributions of each rank.

Here is the Python code:


"""


from fractions import Fraction

# Total 粟 to be distributed
total_corn = 15
additional_corn = 5
total_with_additional = total_corn + additional_corn

# Proportional weights for each rank
weights = [5, 4, 3, 2, 1]  # 大夫, 不更, 簪裹, 上造, 公士

# Calculate the total weight
total_weight = sum(weights)

# Calculate the contribution of each rank
a = Fraction(weights[0] * total_corn, total_weight)  # 大夫
b = Fraction(weights[1] * total_corn, total_weight)  # 不更
c = Fraction(weights[2] * total_corn, total_weight)  # 簪裹
d = Fraction(weights[3] * total_corn, total_weight)  # 上造
e = Fraction(weights[4] * total_corn, total_weight)  # 公士

# Output the results
a, b, c, d, e


"""


### Explanation:
1. The weights `[5, 4, 3, 2, 1]` represent the proportional distribution for each rank.
2. The total weight is the sum of these weights: `5 + 4 + 3 + 2 + 1 = 15`.
3. Each rank's contribution is calculated as `(rank's weight * total 粟) / total weight`.
4. The additional 大夫 receiving 5斗 is already accounted for in the total of 20斗.

### Results:
The variables `a`, `b`, `c`, `d`, and `e` represent the contributions of 大夫, 不更, 簪裹, 上造, and 公士, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 5/4, Actual: 5
Variable 'b' has wrong value. Expected: 1, Actual: 4
Variable 'c' has wrong value. Expected: 3/4, Actual: 3
Variable 'd' has wrong value. Expected: 1/2, Actual: 2
Variable 'e' has wrong value. Expected: 1/4, Actual: 1"""
