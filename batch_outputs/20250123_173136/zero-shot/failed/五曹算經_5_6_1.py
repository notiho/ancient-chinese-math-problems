"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
術曰：列錢一百三十一貫八百一十文為實，并絲貴賤價得九十八文為法，以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得。
答曰：各 a鈞 。
"""

"""
To solve this problem, we need to compute the amount of silk obtained for the given amount of money. Here's the Python code that translates the ancient Chinese math problem into a solution:


"""


from fractions import Fraction

# Given values
price_expensive_silk_per_liang = 56  # in wen
price_cheap_silk_per_liang = 42  # in wen
total_money = 131 * 1000 + 810  # converting 131貫810文 to wen

# Step 1: Compute the combined price per liang of silk
combined_price_per_liang = price_expensive_silk_per_liang + price_cheap_silk_per_liang

# Step 2: Compute the total amount of silk in liangs
total_silk_liangs = Fraction(total_money, combined_price_per_liang)

# Step 3: Convert liangs to jin (1 jin = 16 liangs)
total_silk_jin = total_silk_liangs // 16
remaining_liangs = total_silk_liangs % 16

# Step 4: Compute the number of 30-jin units
a = total_silk_jin // 30

# Output the result
a  # This is the answer in units of 30 jin


"""


Explanation:
1. The combined price per liang of silk is the sum of the prices of expensive and cheap silk (56 + 42 = 98 wen).
2. The total amount of silk in liangs is calculated by dividing the total money (converted to wen) by the combined price per liang.
3. Convert the total silk from liangs to jin (1 jin = 16 liangs).
4. Finally, compute how many 30-jin units can be obtained from the total silk.

The variable `a` contains the answer in units of 30 jin.
"""


"""
Variable 'a' has wrong value. Expected: 269/96, Actual: 2"""
