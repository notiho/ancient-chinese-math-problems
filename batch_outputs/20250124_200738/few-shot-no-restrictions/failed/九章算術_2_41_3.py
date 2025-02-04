"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. The weight is given in a traditional Chinese system of units: 石 (shi), 鈞 (jun), 斤 (jin), 兩 (liang), and 銖 (zhu). The procedure involves converting the total weight into a single unit (jin), then dividing the total cost by the total weight to find the price per jin.

### Problem Breakdown:
- Total cost: 13,970 錢
- Total weight: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- Conversion factors:
  - 1 石 = 4 鈞
  - 1 鈞 = 30 斤
  - 1 斤 = 16 兩
  - 1 兩 = 24 銖

The goal is to calculate the price per 石 and the price per 斤.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in 錢
total_cost = 13970

# Total weight in 石, 鈞, 斤, 兩, 銖
weight_shi = 1
weight_jun = 2
weight_jin = 28
weight_liang = 3
weight_zhu = 5

# Conversion factors
shi_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Convert total weight to 斤 (jin)
total_weight_jin = (
    weight_shi * shi_to_jun * jun_to_jin +
    weight_jun * jun_to_jin +
    weight_jin +
    Fraction(weight_liang, jin_to_liang) +
    Fraction(weight_zhu, jin_to_liang * liang_to_zhu)
)

# Calculate price per 斤 (jin)
price_per_jin = Fraction(total_cost, total_weight_jin)

# Convert price per 斤 to price per 石
price_per_shi = price_per_jin * shi_to_jun * jun_to_jin

# Results
a = price_per_shi  # Price per 石 in 錢
b = price_per_jin  # Price per 斤 in 錢

# Output results
print(f"其 {a} 石 ，斤 {b} 錢 。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Convert Total Weight to Jin**:
   - The total weight is converted into the smallest unit (jin) using the given conversion factors.
   - Fractions are used to ensure precision when dealing with smaller units like liang and zhu.

2. **Calculate Price per Jin**:
   - The total cost is divided by the total weight in jin to find the price per jin.

3. **Calculate Price per Shi**:
   - The price per jin is multiplied by the number of jin in one shi to find the price per shi.

4. **Output Results**:
   - The results are displayed as the price per shi (`a`) and the price per jin (`b`).

---

### Example Output:
If you run the code, it will calculate the price per 石 and per 斤 based on the given inputs. The results will be displayed in terms of 錢.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
