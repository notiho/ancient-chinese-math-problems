"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

"""
To solve this problem, we need to calculate how many pears can be bought with the given amount of money and determine the remaining money. Here's the Python code:


"""


from fractions import Fraction

# Given data
total_money = 27 * 1000 + 833  # Convert 貫 and 文 into total 文
price_per_pear = 5  # 5 文 for 3 pears
pears_per_unit = 3  # 3 pears per unit

# Calculate total pears and remaining money
total_pears = (total_money * pears_per_unit) // price_per_pear
remaining_money = (total_money * pears_per_unit) % price_per_pear

# Assign the results to variables
a = total_pears  # Total pears
b = remaining_money  # Remaining money in 文

# Results
a, b


"""


This code calculates the total number of pears (`a`) and the remaining money in 文 (`b`).
"""


"""
"""
