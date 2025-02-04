"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight purchased. The weight is given in units of **shi**, **jun**, and **jin**, and the total cost is provided. The goal is to determine the price per **jin** for each unit of **shi** and **jun**.

---

### Problem Breakdown:
- **Total money spent**: 1120 (錢)
- **Total weight purchased**: 1 **shi**, 2 **jun**, 18 **jin**.
- **Goal**: Determine the price per **jin** for each **shi** and **jun**.

---

### Procedure:
1. Convert the total weight into a single unit (**jin**):
   - 1 **shi** = 120 **jin**.
   - 1 **jun** = 20 **jin**.
   - Total weight = \( 1 \times 120 + 2 \times 20 + 18 = 178 \, \text{jin} \).

2. Calculate the price per **jin**:
   - Price per **jin** = \( \frac{\text{Total money}}{\text{Total weight}} = \frac{1120}{178} \).

3. Determine the price per **jin** for each **shi** and **jun**:
   - For 1 **shi** (120 **jin**): Multiply the price per **jin** by 120.
   - For 1 **jun** (20 **jin**): Multiply the price per **jin** by 20.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 1120

# Total weight purchased
shi_to_jin = 120  # 1 石 = 120 斤
jun_to_jin = 20   # 1 鈞 = 20 斤
total_weight = 1 * shi_to_jin + 2 * jun_to_jin + 18  # Total weight in 斤

# Price per 斤
price_per_jin = Fraction(total_money, total_weight)

# Price for 1 石 (120 斤)
price_per_shi = price_per_jin * shi_to_jin

# Price for 1 鈞 (20 斤)
price_per_jun = price_per_jin * jun_to_jin

# Results
a = price_per_jun  # Price per 鈞 in 錢
b = price_per_jin  # Price per 斤 in 錢
c = price_per_shi  # Price per 石 in 錢
d = price_per_jin  # Price per 斤 in 錢

# Output results
print(f"其 1 鈞 ，斤 {a} 錢 。")
print(f"其 1 石 ，斤 {c} 錢 。")
#----- content ends here -----


"""


---

### Explanation of Results:
- **a**: The price per **jin** for 1 **jun**.
- **b**: The price per **jin**.
- **c**: The price per **jin** for 1 **shi**.
- **d**: The price per **jin**.

This code calculates the price per unit weight for both **shi** and **jun**, as well as the price per **jin**, based on the total cost and weight.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 11200/89
Variable 'b' has wrong value. Expected: 5, Actual: 560/89
Variable 'c' has wrong value. Expected: 13/12, Actual: 67200/89
Variable 'd' has wrong value. Expected: 6, Actual: 560/89"""
