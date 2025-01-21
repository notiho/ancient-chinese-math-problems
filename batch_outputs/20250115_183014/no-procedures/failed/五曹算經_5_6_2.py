"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
答曰：各 a鈞 b 两。
"""

"""
This problem involves dividing a total amount of money between two types of silk (expensive and cheap) and determining how much of each type can be purchased. Let's solve it step by step.

---

### Problem:
- Expensive silk costs **56 wen per liang**.
- Cheap silk costs **42 wen per liang**.
- Total money available: **131,810 wen** (since 1 guan = 1,000 wen, 131 guan = 131,000 wen, and adding 810 wen gives 131,810 wen).
- Question: How much of each type of silk can be purchased, expressed in **jin** (1 jin = 16 liang) and **liang**?

---

### Solution:


"""


from fractions import Fraction

# Prices per liang
expensive_silk_price = 56  # wen per liang
cheap_silk_price = 42      # wen per liang

# Total money available
total_money = 131 * 1000 + 810  # Convert guan to wen

# Let x be the amount of expensive silk (in liang)
# Let y be the amount of cheap silk (in liang)
# We know:
# 56x + 42y = 131810
# To maximize the amount of silk, we prioritize cheaper silk.

# First, calculate the maximum amount of cheap silk we can buy
max_cheap_silk = total_money // cheap_silk_price  # Maximum liang of cheap silk
remaining_money = total_money % cheap_silk_price  # Remaining money after buying cheap silk

# Check if the remaining money can buy expensive silk
if remaining_money % expensive_silk_price == 0:
    expensive_silk = remaining_money // expensive_silk_price
    cheap_silk = max_cheap_silk
else:
    # Adjust to ensure the total money is spent exactly
    while max_cheap_silk >= 0:
        remaining_money = total_money - (max_cheap_silk * cheap_silk_price)
        if remaining_money % expensive_silk_price == 0:
            expensive_silk = remaining_money // expensive_silk_price
            cheap_silk = max_cheap_silk
            break
        max_cheap_silk -= 1

# Convert liang to jin and liang
expensive_silk_jin = expensive_silk // 16
expensive_silk_liang = expensive_silk % 16

cheap_silk_jin = cheap_silk // 16
cheap_silk_liang = cheap_silk % 16

# Output the results
print(f"Expensive silk: {expensive_silk_jin} jin {expensive_silk_liang} liang")
print(f"Cheap silk: {cheap_silk_jin} jin {cheap_silk_liang} liang")


"""


---

### Explanation:
1. Start by calculating the maximum amount of cheap silk that can be purchased with the total money.
2. Check if the remaining money can be used to buy expensive silk.
3. If not, adjust the amount of cheap silk downward until the remaining money can be spent exactly on expensive silk.
4. Convert the final amounts of silk from **liang** to **jin** and **liang** for the answer.

---

### Final Answer:
The program will calculate the exact amounts of expensive and cheap silk in **jin** and **liang**.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
