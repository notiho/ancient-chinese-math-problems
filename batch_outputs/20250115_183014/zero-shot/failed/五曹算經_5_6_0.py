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
total_money = 131 * 1000 + 810  # converting 貫 and 文 to total 文

# Step 1: Calculate the combined price per liang of silk
combined_price_per_liang = price_expensive_silk_per_liang + price_cheap_silk_per_liang  # in wen

# Step 2: Calculate the total amount of silk in liang
total_silk_liang = Fraction(total_money, combined_price_per_liang)

# Step 3: Convert liang to jin (1 jin = 16 liang)
total_silk_jin = total_silk_liang // 16  # integer division for whole jin
remaining_liang = total_silk_liang % 16  # remainder in liang

# Step 4: Assign the results to variables
a = total_silk_jin  # in jin
b = remaining_liang  # in liang

# Results
a, b


"""


### Explanation:
1. **Price per liang**: The combined price of expensive and cheap silk per liang is calculated as \( 56 + 42 = 98 \) wen.
2. **Total silk in liang**: Divide the total money (in wen) by the combined price per liang to get the total amount of silk in liang.
3. **Convert liang to jin**: Since 1 jin = 16 liang, divide the total silk in liang by 16 to get the number of jin and the remainder in liang.
4. **Assign results**: The results are stored in variables `a` (jin) and `b` (liang).

### Output:
The variables `a` and `b` will contain the solution:
- `a` = 84 (jin)
- `b` = 1 (liang)
"""


"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 84"""
