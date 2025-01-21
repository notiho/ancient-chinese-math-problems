"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
術曰：列錢一百三十一貫八百一十文為實，并絲貴賤價得九十八文為法，以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得。
答曰：各 a鈞 b 两。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
price_expensive_silk_per_liang = 56  # in wen
price_cheap_silk_per_liang = 42  # in wen
total_money = 131 * 1000 + 810  # converting 131貫810文 to wen

# Step 1: Calculate the combined price of 1 liang of expensive and cheap silk
combined_price_per_liang = price_expensive_silk_per_liang + price_cheap_silk_per_liang

# Step 2: Calculate the total amount of silk in liangs
total_silk_liangs = Fraction(total_money, combined_price_per_liang)

# Step 3: Convert liangs to jin (1 jin = 16 liangs)
total_silk_jin = total_silk_liangs // 16
remaining_liangs = total_silk_liangs % 16

# Step 4: Assign the results to variables
a = total_silk_jin  # in jin
b = remaining_liangs  # in liangs

# Results
a, b


"""


### Explanation:
1. **Price of 1 liang of silk**: The combined price of 1 liang of expensive and cheap silk is \( 56 + 42 = 98 \) wen.
2. **Total silk in liangs**: Divide the total money (converted to wen) by the combined price per liang.
3. **Convert to jin and liang**: Since 1 jin = 16 liangs, divide the total liangs by 16 to get the number of jin and the remainder as liangs.
4. **Output**: The result is stored in variables `a` (in jin) and `b` (in liangs).

### Final Answer:
The variables `a` and `b` will contain the solution:
- `a` = 84 (jin)
- `b` = 1 (liang)
"""


"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 84"""
