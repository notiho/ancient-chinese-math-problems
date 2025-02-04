"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (斤) based on the total cost and the total weight. Let's break it down step by step according to the procedure provided.

---

### Problem Breakdown:
- **Total cost**: 1120 (錢)
- **Total weight**: 1 石, 2 鈞, 18 斤
  - 1 石 = 4 鈞
  - 1 鈞 = 30 斤
  - Total weight in 斤 = \( 1 \times 4 \times 30 + 2 \times 30 + 18 = 168 \) 斤

---

### Procedure:
1. **法 (denominator)**: Total weight in 斤.
2. **實 (numerator)**: Total cost (1120 錢).
3. **Rate per 斤**: Divide the total cost by the total weight.

---

### Python Code:


"""


from fractions import Fraction

# Total cost
錢數 = 1120

# Total weight in 斤
石 = 1
鈞 = 2
斤 = 18
總斤 = 石 * 4 * 30 + 鈞 * 30 + 斤

# 法: Total weight in 斤
法 = 總斤

# 實: Total cost
實 = 錢數

# Rate per 斤
rate_per_斤 = Fraction(實, 法)

# Convert to 鈞 and 石 rates
rate_per_鈞 = rate_per_斤 * 30
rate_per_石 = rate_per_鈞 * 4

# Outputs
a = rate_per_鈞  # 鈞 rate
b = rate_per_斤  # 斤 rate
c = rate_per_石  # 石 rate
d = rate_per_斤  # 斤 rate (same as b)

# Results
a, b, c, d


"""


---

### Explanation of Results:
- `a`: Price per 鈞.
- `b`: Price per 斤.
- `c`: Price per 石.
- `d`: Price per 斤 (same as `b`).

This code calculates the price per unit weight (斤) and converts it to the rates for 鈞 and 石 as well.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 5600/33
Variable 'b' has wrong value. Expected: 5, Actual: 560/99
Variable 'c' has wrong value. Expected: 13/12, Actual: 22400/33
Variable 'd' has wrong value. Expected: 6, Actual: 560/99"""
