"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

"""
To solve this problem, we need to calculate how many pears can be bought with the given amount of money (27貫833文), where 5文 buys 3 pears. The solution will consist of the number of pears (`a`) and the remaining money in 文 (`b`).

Here is the Python code:


"""


from fractions import Fraction

# Given values
total_money = 27 * 1000 + 833  # Convert 貫 to 文 (1貫 = 1000文)
pear_cost = 5  # 5文 buys 3 pears
pears_per_cost = 3

# Total pears that can be bought
total_pears = (total_money * pears_per_cost) // pear_cost
a = total_pears  # Number of pears

# Remaining money
remaining_money = (total_money * pears_per_cost) % pear_cost
b = remaining_money  # Remaining money in 文

# Results
a, b


"""


This code calculates the number of pears (`a`) and the remaining money in 文 (`b`).
"""


"""
"""
