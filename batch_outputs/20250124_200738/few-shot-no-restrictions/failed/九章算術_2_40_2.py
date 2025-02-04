"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This is a problem involving proportional distribution of money based on the weight of silk purchased. The goal is to calculate the price per unit weight (jin, and then per shi and per jun) based on the total money spent and the total weight of silk.

### Problem Breakdown:
- Total money spent: **13,970 qian**.
- Total weight of silk: **1 shi, 2 jun, 28 jin, 3 liang, 5 zhu**.
- The task is to calculate:
  - The price per jin (qian per jin).
  - The price per shi and per jun (qian per shi and qian per jun).

---

### Procedure:
1. Convert the total weight into a single unit (jin):
   - 1 shi = 120 jin.
   - 1 jun = 30 jin.
   - 1 liang = 1/16 jin.
   - 1 zhu = 1/384 jin.
   - Total weight in jin = \( 1 \times 120 + 2 \times 30 + 28 + \frac{3}{16} + \frac{5}{384} \).

2. Calculate the price per jin:
   - Price per jin = Total money / Total weight in jin.

3. Calculate the price per shi and per jun:
   - Price per shi = Price per jin × 120.
   - Price per jun = Price per jin × 30.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent (qian)
total_money = 13970

# Total weight in various units
shi = 1
jun = 2
jin = 28
liang = Fraction(3, 16)  # 1 liang = 1/16 jin
zhu = Fraction(5, 384)   # 1 zhu = 1/384 jin

# Convert total weight to jin
total_weight_jin = (shi * 120) + (jun * 30) + jin + liang + zhu

# Calculate price per jin
price_per_jin = Fraction(total_money, total_weight_jin)

# Calculate price per shi and per jun
price_per_shi = price_per_jin * 120
price_per_jun = price_per_jin * 30

# Results
a = price_per_jin  # Price per jin
b = price_per_jun  # Price per jun
c = price_per_shi  # Price per shi
d = price_per_jun  # Price per jun (repeated for clarity)

# Output results
print(f"Price per jin: {a} qian")
print(f"Price per jun: {b} qian")
print(f"Price per shi: {c} qian")
print(f"Price per jun (again): {d} qian")
#----- content ends here -----


"""


---

### Explanation of Results:
- **a (price per jin)**: The cost of 1 jin of silk in qian.
- **b (price per jun)**: The cost of 1 jun (30 jin) of silk in qian.
- **c (price per shi)**: The cost of 1 shi (120 jin) of silk in qian.
- **d (price per jun)**: Repeated for clarity.

This code will calculate the proportional prices based on the total money spent and the total weight of silk purchased.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 2013, Actual: 160934400/79949"""
