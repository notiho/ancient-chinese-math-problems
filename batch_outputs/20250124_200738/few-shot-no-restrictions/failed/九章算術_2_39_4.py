"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
This problem involves calculating the unit price of silk based on the total cost and the weight of the silk purchased. The weight is given in traditional Chinese units: 石 (shi), 鈞 (jun), 斤 (jin), 兩 (liang), and 銖 (zhu). The goal is to determine the price per shi and the price per jun.

### Problem Breakdown:
- Total cost: **13,970** (in unspecified currency).
- Total weight: **1 shi, 2 jun, 28 jin, 3 liang, 5 zhu**.
- The procedure involves calculating the price per shi and per jun.

### Conversion of Units:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

### Procedure:
1. Convert the total weight into a single unit (e.g., 銖 for precision).
2. Calculate the price per shi and per jun using the total cost and the converted weight.
3. Use the given procedure to determine the rates.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost
total_cost = 13970

# Total weight in traditional units
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
shi_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Step 1: Convert total weight to zhu
total_weight_in_zhu = (
    shi * shi_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jin * jin_to_liang * liang_to_zhu +
    liang * liang_to_zhu +
    zhu
)

# Step 2: Calculate price per shi and per jun
# Convert 1 shi to zhu
one_shi_in_zhu = shi_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu

# Price per shi
price_per_shi = Fraction(total_cost, shi + Fraction(jun, shi_to_jun))

# Convert 1 jun to zhu
one_jun_in_zhu = jun_to_jin * jin_to_liang * liang_to_zhu

# Price per jun
price_per_jun = Fraction(total_cost, total_weight_in_zhu // one_jun_in_zhu)

# Results
a = price_per_jun  # Price per jun
b = price_per_shi  # Price per shi

# Output
print(f"Price per jun: {a} (in currency)")
print(f"Price per shi: {b} (in currency)")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into the smallest unit (銖) for precision.
2. **Price Calculation**: The price per shi and per jun is calculated using the total cost and the converted weight.
3. **Fraction Handling**: The `Fraction` class is used to ensure precise calculations without rounding errors.

---

### Final Answer:
- **a 鈞**: Price per jun.
- **b 錢**: Price per shi.
"""


"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 6985/3
Variable 'b' has wrong value. Expected: 8051, Actual: 27940/3
Missing variable in output: 'c'
Missing variable in output: 'd'"""
