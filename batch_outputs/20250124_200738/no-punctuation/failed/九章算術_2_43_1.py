"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤銖率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a鈞  b銖 一錢 其 c石  d銖 一錢
"""

"""
This problem is quite intricate, involving the calculation of the price per unit weight (銖 rate) and then determining the distribution of the cost across different units of weight. Let's break it down step by step and encode the procedure in Python.

### Problem Breakdown:
- You have **13,970 coins** spent to buy **1 石, 2 鈞, 28 斤, 3 兩, and 5 銖** of silk.
- The goal is to calculate the price per 銖 (銖 rate) and then distribute the cost across the different units of weight.

### Procedure:
1. **Convert the total weight into 銖**:
   - 1 石 = 4 鈞
   - 1 鈞 = 30 斤
   - 1 斤 = 16 兩
   - 1 兩 = 24 銖
   - Total weight in 銖 = (1 石 × 4 鈞 × 30 斤 × 16 兩 × 24 銖) + (2 鈞 × 30 斤 × 16 兩 × 24 銖) + (28 斤 × 16 兩 × 24 銖) + (3 兩 × 24 銖) + 5 銖.

2. **Calculate the price per 銖 (銖 rate)**:
   - 銖 rate = Total money / Total weight in 銖.

3. **Distribute the cost across different units of weight**:
   - Use the 銖 rate to calculate the cost for each unit (石, 鈞, 斤, 兩, 銖).

4. **Reverse the calculation to verify the distribution**:
   - Ensure the total cost matches the original amount of money.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_money = 13970  # Total money spent
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Step 1: Convert total weight into 銖
銖_per_兩 = 24
兩_per_斤 = 16
斤_per_鈞 = 30
鈞_per_石 = 4

total_銖 = (
    石 * 鈞_per_石 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩 +
    鈞 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩 +
    斤 * 兩_per_斤 * 銖_per_兩 +
    兩 * 銖_per_兩 +
    銖
)

# Step 2: Calculate the price per 銖
銖_rate = Fraction(total_money, total_銖)

# Step 3: Distribute the cost across units
# Cost for 石
石_cost = 銖_rate * (石 * 鈞_per_石 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩)

# Cost for 鈞
鈞_cost = 銖_rate * (鈞 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩)

# Cost for 斤
斤_cost = 銖_rate * (斤 * 兩_per_斤 * 銖_per_兩)

# Cost for 兩
兩_cost = 銖_rate * (兩 * 銖_per_兩)

# Cost for 銖
銖_cost = 銖_rate * 銖

# Step 4: Reverse calculation to verify
total_calculated_money = 石_cost + 鈞_cost + 斤_cost + 兩_cost + 銖_cost

# Outputs
a = 鈞_cost
b = 銖_cost
c = 石_cost
d = total_calculated_money - total_money  # Verification adjustment

print(f"其 {a} 鈞 {b} 銖 一錢")
print(f"其 {c} 石 {d} 銖 一錢")
#----- content ends here -----


"""


### Explanation of Variables:
- `total_銖`: Total weight converted into 銖.
- `銖_rate`: Price per 銖, calculated as total money divided by total weight in 銖.
- `石_cost`, `鈞_cost`, `斤_cost`, `兩_cost`, `銖_cost`: Costs distributed across the respective units of weight.

### Outputs:
- `a`: Cost in 鈞.
- `b`: Cost in 銖.
- `c`: Cost in 石.
- `d`: Verification adjustment (should be close to zero if calculations are correct).
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 321868800/79949
Variable 'b' has wrong value. Expected: 5, Actual: 69850/79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 6, Actual: 0"""
