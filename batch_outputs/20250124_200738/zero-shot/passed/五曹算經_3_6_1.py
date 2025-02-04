"""
今有錢二十七貫八百三十三文，凡五文買棃三枚。問：得棃㡬何？
術曰：列錢二十七貫八百三十三文，以三乘之得八萬三千四百九十九，以五除之即得。
答曰： a枚 奇 b文 。
"""

"""
To solve this problem, we need to determine how many pears can be bought with the given amount of money, and how much money will remain after buying as many pears as possible.

### Problem Breakdown:
1. Total money: 27貫833文. (1貫 = 1000文, so total money in 文 is \( 27 \times 1000 + 833 = 27833 \) 文).
2. Cost of 3 pears: 5文.
3. To find the number of pears, we calculate how many groups of 3 pears can be bought with the total money.
4. The remainder will be the leftover money after buying as many pears as possible.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Total money in 文
total_money = 27 * 1000 + 833

# Cost of 3 pears in 文
cost_per_3_pears = 5

# Total pears that can be bought
total_pears = total_money * 3 // cost_per_3_pears

# Remaining money
remaining_money = total_money * 3 % cost_per_3_pears

# Assigning to variables
a = total_pears  # Total pears
b = remaining_money  # Remaining money in 文
#----- content ends here -----


"""


### Final Answer:
The solution is:
- `a`枚 (total pears)
- `b`文 (remaining money).
"""


"""
"""
