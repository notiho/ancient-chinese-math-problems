"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
術曰：列錢一百三十一貫八百一十文為實，并絲貴賤價得九十八文為法，以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得。
答曰：各 a鈞 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Let's break it down step by step:

1. **Understanding the problem**:
   - The price of expensive silk is 56 wen per liang.
   - The price of cheap silk is 42 wen per liang.
   - The total money available is 131,810 wen (since 1 guan = 1,000 wen, 131 guan = 131,000 wen, and adding 810 wen gives 131,810 wen).
   - We are tasked to find out how many jin (斤) of silk can be purchased in total.

2. **Key conversions**:
   - 1 jin = 16 liang.
   - The combined price of 1 liang of both types of silk is \( 56 + 42 = 98 \) wen.

3. **Steps to compute**:
   - Divide the total money by the combined price of 1 liang of silk to get the total number of liang of silk.
   - Convert the total number of liang into jin and liang.

4. **Python implementation**:


"""


from fractions import Fraction

# Given data
total_money = 131810  # in wen
expensive_silk_price = 56  # per liang in wen
cheap_silk_price = 42  # per liang in wen
combined_price_per_liang = expensive_silk_price + cheap_silk_price  # 98 wen per liang

# Step 1: Calculate total silk in liang
total_silk_liang = Fraction(total_money, combined_price_per_liang)

# Step 2: Convert liang to jin and liang
jin = total_silk_liang // 16  # Integer division to get full jin
remaining_liang = total_silk_liang % 16  # Remainder in liang

# Assign the result to variable 'a'
a = jin

# Output the result
a, remaining_liang


"""


5. **Explanation of the result**:
   - The variable `a` represents the total number of jin (斤) of silk that can be purchased.
   - The `remaining_liang` represents the leftover silk in liang after converting to jin.


"""


"""
Variable 'a' has wrong value. Expected: 269/96, Actual: 84"""
