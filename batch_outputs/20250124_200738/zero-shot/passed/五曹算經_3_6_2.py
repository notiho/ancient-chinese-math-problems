"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

"""
To solve this problem, we need to calculate how many pears can be bought with the given amount of money (27貫833文). Each pear costs 5文 for 3 pears. Here's the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_money = 27 * 1000 + 833  # Convert 貫 to 文 (1貫 = 1000文)
cost_per_3_pears = 5  # 5文 for 3 pears

# Total pears that can be bought
total_pears = total_money * 3 // cost_per_3_pears  # Integer division for full pears
remaining_money = total_money * 3 % cost_per_3_pears  # Remaining money in 文

# Assigning the results to variables
a = total_pears
b = remaining_money

# Results
print(f"a = {a}枚, b = {b}文")
#----- content ends here -----


"""


This code calculates the total number of pears (`a`) and the remaining money in 文 (`b`).
"""


"""
"""
