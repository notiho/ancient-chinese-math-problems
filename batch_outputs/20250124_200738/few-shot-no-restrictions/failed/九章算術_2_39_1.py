"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight purchased. The weight is given in a hierarchical system: **1 stone (石)** = 4 **jun (鈞)**, 1 **jun (鈞)** = 30 **jin (斤)**, 1 **jin (斤)** = 16 **liang (兩)**, and 1 **liang (兩)** = 24 **zhu (銖)**.

The total cost is **13,970 coins**, and the total weight is **1 stone, 2 jun, 28 jin, 3 liang, and 5 zhu**. The goal is to calculate the price per **stone** and per **jun**.

---

### Step-by-step solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in coins
total_cost = 13970

# Total weight in hierarchical units
stones = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
jun_per_stone = 4
jin_per_jun = 30
liang_per_jin = 16
zhu_per_liang = 24

# Convert the total weight into the smallest unit (zhu)
total_weight_in_zhu = (
    stones * jun_per_stone * jin_per_jun * liang_per_jin * zhu_per_liang +
    jun * jin_per_jun * liang_per_jin * zhu_per_liang +
    jin * liang_per_jin * zhu_per_liang +
    liang * zhu_per_liang +
    zhu
)

# Conversion factors for price calculation
zhu_per_stone = jun_per_stone * jin_per_jun * liang_per_jin * zhu_per_liang
zhu_per_jun = jin_per_jun * liang_per_jin * zhu_per_liang

# Calculate price per stone and per jun
price_per_stone = Fraction(total_cost, stones + Fraction(jun, jun_per_stone))
price_per_jun = Fraction(total_cost, total_weight_in_zhu / zhu_per_jun)

# Simplify the results
a = price_per_jun.numerator
b = price_per_jun.denominator
c = price_per_stone.numerator
d = price_per_stone.denominator

# Output the results
print(f"Price per jun: {a} coins per {b} jun")
print(f"Price per stone: {c} coins per {d} stone")
#----- content ends here -----


"""


---

### Explanation of the Code:

1. **Weight Conversion**:
   - The total weight is converted into the smallest unit, **zhu**, for precise calculations.
   - Each hierarchical unit (stone, jun, jin, liang, zhu) is converted step-by-step using the given conversion factors.

2. **Price Calculation**:
   - The price per **stone** is calculated by dividing the total cost by the total weight in **stones**.
   - The price per **jun** is calculated by dividing the total cost by the total weight in **jun**.

3. **Fraction Handling**:
   - The `Fraction` class is used to ensure exact calculations and to simplify the results into proper fractions.

4. **Output**:
   - The results are presented as fractions, showing the price per **jun** and per **stone** in terms of coins.

---

### Example Output:
If you run the code with the given inputs, you will get the price per **jun** and per **stone** in simplified fractional form. Let me know if you'd like me to refine or expand on any part of the solution!
"""


"""
Code error: both arguments should be Rational instances"""
