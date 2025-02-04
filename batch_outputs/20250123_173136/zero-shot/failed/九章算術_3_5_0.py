"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 15斗 of 粟 among five people of different ranks (大夫, 不更, 簪裹, 上造, 公士) based on their respective shares, and then adjusting the distribution when an additional 大夫 arrives and also receives 5斗. The solution involves proportional distribution.

Here is the Python code:


"""


from fractions import Fraction

# Total 粟 to distribute
total_corn = 15  # in 斗

# Additional 大夫's share
additional_dafu_share = 5  # in 斗

# Number of people in each rank
ranks = {
    "大夫": 1,
    "不更": 1,
    "簪裹": 1,
    "上造": 1,
    "公士": 1
}

# Total number of people
total_people = sum(ranks.values())

# Adjusted total 粟 after including the additional 大夫
adjusted_total_corn = total_corn + additional_dafu_share

# Calculate the share for each rank
base_share = Fraction(adjusted_total_corn, total_people)

# Calculate the amount each rank contributes
a = base_share * ranks["大夫"] - Fraction(additional_dafu_share, total_people)
b = base_share * ranks["不更"]
c = base_share * ranks["簪裹"]
d = base_share * ranks["上造"]
e = base_share * ranks["公士"]

# Outputs
a, b, c, d, e


"""


This code calculates the amount of 粟 (斗) each rank contributes (`a`, `b`, `c`, `d`, `e`) using the proportional distribution method described in the problem. The results are stored in variables `a`, `b`, `c`, `d`, and `e`.
"""


"""
Variable 'a' has wrong value. Expected: 5/4, Actual: 3
Variable 'b' has wrong value. Expected: 1, Actual: 4
Variable 'c' has wrong value. Expected: 3/4, Actual: 4
Variable 'd' has wrong value. Expected: 1/2, Actual: 4
Variable 'e' has wrong value. Expected: 1/4, Actual: 4"""
