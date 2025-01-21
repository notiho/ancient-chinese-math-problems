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
- Total money available is **131,810 wen** (since 1 guan = 1,000 wen, 131 guan and 810 wen = 131,810 wen).
- Question: How much of each type of silk can be purchased (in **jin** and **liang**, where 1 jin = 16 liang)?

---

### Solution:


"""


from fractions import Fraction

# Prices per liang
expensive_price = 56  # wen per liang
cheap_price = 42      # wen per liang

# Total money available
total_money = 131810  # wen

# Let x be the amount of expensive silk (in liang), and y be the amount of cheap silk (in liang).
# The total cost equation is:
# 56x + 42y = 131810
# Simplify by dividing through by 14:
# 4x + 3y = 9415

# To maximize the amount of silk purchased, we solve for integer solutions of x and y.
# Rearrange for y:
# y = (9415 - 4x) / 3

# Find the maximum x such that y is a whole number and both x and y are non-negative.
for x in range(0, 9415 // 4 + 1):  # x must be less than or equal to 9415 // 4
    if (9415 - 4 * x) % 3 == 0:
        y = (9415 - 4 * x) // 3
        if y >= 0:
            expensive_silk_liang = x
            cheap_silk_liang = y
            break

# Convert liang to jin and liang (1 jin = 16 liang)
expensive_silk_jin = expensive_silk_liang // 16
expensive_silk_remaining_liang = expensive_silk_liang % 16

cheap_silk_jin = cheap_silk_liang // 16
cheap_silk_remaining_liang = cheap_silk_liang % 16

# Results
a_expensive_jin = expensive_silk_jin
b_expensive_liang = expensive_silk_remaining_liang

c_cheap_jin = cheap_silk_jin
d_cheap_liang = cheap_silk_remaining_liang

print(f"Expensive silk: {a_expensive_jin} jin {b_expensive_liang} liang")
print(f"Cheap silk: {c_cheap_jin} jin {d_cheap_liang} liang")


"""


---

### Explanation:
1. The total cost equation is derived from the prices of the two types of silk and the total money available.
2. We simplify the equation and solve for integer solutions of `x` (expensive silk in liang) and `y` (cheap silk in liang).
3. Once we find the solution, we convert the amounts from **liang** to **jin** and **liang** for the final answer.

---

### Final Answer:
After running the code, the output will be:

```
Expensive silk: a jin b liang
Cheap silk: c jin d liang
```

Where `a`, `b`, `c`, and `d` are the respective amounts of expensive and cheap silk.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
