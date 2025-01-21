"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 15斗 of 粟 among five ranks: 大夫, 不更, 簪裹, 上造, and 公士, with an additional 大夫 arriving later who also receives 5斗. The solution involves proportional distribution based on their ranks.

Here is the Python code:


"""


from fractions import Fraction

# Total 粟 to be distributed
total_corn = 15  # in 斗

# Additional 大夫 arriving later who also receives 5斗
additional_corn = 5  # in 斗

# Number of ranks
ranks = 5

# Calculate the proportional distribution
# Each rank contributes equally to the additional 大夫's share
# The total becomes 15斗 + 5斗 = 20斗
total_with_additional = total_corn + additional_corn  # 20斗

# Each rank's share is proportional to 1斗 out of the total_with_additional
share_per_rank = Fraction(1, total_with_additional)

# Calculate the amount each rank contributes
a = share_per_rank * total_corn  # 大夫
b = share_per_rank * total_corn  # 不更
c = share_per_rank * total_corn  # 簪裹
d = share_per_rank * total_corn  # 上造
e = share_per_rank * total_corn  # 公士

# Outputs
a = Fraction(1, 20) * 15  # 大夫出
b = Fraction(1, 20)

"""

"""


"""
Variable 'a' has wrong value. Expected: 5/4, Actual: 3/4
Variable 'b' has wrong value. Expected: 1, Actual: 1/20
Variable 'd' has wrong value. Expected: 1/2, Actual: 3/4
Variable 'e' has wrong value. Expected: 1/4, Actual: 3/4"""
