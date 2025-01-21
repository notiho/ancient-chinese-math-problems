"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
答曰：各 a鈞 b 两。
"""

"""
This problem involves dividing a total amount of money between two types of silk (expensive and cheap) and determining how much of each type can be purchased. Let's solve it step by step.

---

### Problem Breakdown:
- **Expensive silk**: 1 liang costs 56 wen.
- **Cheap silk**: 1 liang costs 42 wen.
- **Total money**: 131,810 wen (since 1 guan = 1,000 wen, 131 guan = 131,000 wen, and adding 810 wen gives 131,810 wen).
- We need to determine how much of each type of silk (in **jin** and **liang**) can be purchased.

---

### Solution:

1 **Define variables**:
- Let `x` be the amount of expensive silk in **liang**.
- Let `y` be the amount of cheap silk in **liang**.

2 **Set up equations**:
- The total cost equation:  
  \( 56x + 42y = 131810 \)
- The total weight equation (since we are dividing the money between the two types of silk):  
  \( x + y = \text{total weight in liang} \)

3 **Solve for x and y**:
We will calculate the maximum amount of silk that can be purchased with the given money.

---

### Python Code:


"""


from fractions import Fraction

# Prices per liang
expensive_silk_price = 56  # wen per liang
cheap_silk_price = 42      # wen per liang

# Total money in wen
total_money = 131 * 1000 + 810  # 131,810 wen

# Let x be the amount of expensive silk in liang
# Let y be the amount of cheap silk in liang
# Solve the equation: 56x + 42y = 131810

# Simplify the ratio of prices
ratio_expensive = expensive_silk_price
ratio_cheap = cheap_silk_price

# Total weight in liang (x + y)
total_weight = Fraction(total_money, (ratio_expensive + ratio_cheap))

# Amount of expensive silk (x)
x = total_weight * ratio_cheap / (ratio_expensive + ratio_cheap)

# Amount of cheap silk (y)
y = total_weight - x

# Convert to jin and liang (1 jin = 16 liang)
a_expensive_jin = x // 16
b_expensive_liang = x % 16

a_cheap_jin = y // 16
b_cheap_liang = y % 16

# Output results
print(f"Expensive silk: {a_expensive_jin} jin {b_expensive_liang} liang")
print(f"Cheap silk: {a_cheap_jin} jin {b_cheap_liang} liang")


"""


---

### Explanation of the Code:
1. We calculate the total weight of silk that can be purchased by dividing the total money by the combined price of 1 liang of both types of silk.
2. Using the ratio of the prices, we split the total weight into the amounts of expensive and cheap silk.
3. Finally, we convert the weights from **liang** into **jin** and **liang** (since 1 jin = 16 liang).

---

### Final Answer:
After running the code, you will get the amounts of expensive and cheap silk in **jin** and **liang**.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
