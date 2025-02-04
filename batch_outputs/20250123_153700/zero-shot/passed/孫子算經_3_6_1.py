"""
今有丁九萬八千七百六十六，凡二十五丁出一兵。問：兵幾何？
術曰：置丁九萬八千七百六十六為實，以二十五為法。實如法，即得。
答曰： a人 奇 b 丁。
"""

"""
To solve this problem, we need to determine how many soldiers ("兵") can be formed from a total of 98,766 people ("丁") if 25 people are required to form one soldier. The remainder will be the leftover people ("丁"). Let's translate this into Python code:


"""


from fractions import Fraction

# Given values
total_people = 98766  # Total 丁
people_per_soldier = 25  # 丁 required for one soldier

# Calculate the number of soldiers and the remainder 丁
a = total_people // people_per_soldier  # Number of soldiers
b = total_people % people_per_soldier  # Remaining 丁

# Results
a, b


"""


Here:
- `a` represents the number of soldiers ("兵").
- `b` represents the leftover people ("丁").
"""


"""
"""
