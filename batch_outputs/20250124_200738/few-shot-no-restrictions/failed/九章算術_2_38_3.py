"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight purchased. The weight is given in traditional Chinese units: **shi** (石), **jun** (鈞), and **jin** (斤). Here's the solution:

---

### Problem Breakdown:
- **Total money spent:** 1120 (錢)
- **Total weight purchased:** 1 石, 2 鈞, 18 斤
- **Goal:** Determine the price per **jin** (斤) for each **shi** (石) and **jun** (鈞).

---

### Procedure:
1. **Convert the total weight into a single unit (斤):**
   - 1 石 = 120 斤
   - 1 鈞 = 30 斤
   - Total weight = \( 1 \times 120 + 2 \times 30 + 18 = 198 \) 斤.

2. **Calculate the price per 斤:**
   - Total cost = 1120 錢
   - Price per 斤 = \( \frac{\text{Total cost}}{\text{Total weight}} = \frac{1120}{198} \).

3. **Calculate the price per 鈞 (30 斤):**
   - Price per 鈞 = \( 30 \times \text{Price per 斤} \).

4. **Calculate the price per 石 (120 斤):**
   - Price per 石 = \( 120 \times \text{Price per 斤} \).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in 錢
total_cost = 1120

# Total weight in 石, 鈞, and 斤
shi = 1
jun = 2
jin = 18

# Conversion factors
shi_to_jin = 120
jun_to_jin = 30

# Convert total weight to 斤
total_weight_jin = shi * shi_to_jin + jun * jun_to_jin + jin

# Calculate price per 斤
price_per_jin = Fraction(total_cost, total_weight_jin)

# Calculate price per 鈞 (30 斤)
price_per_jun = price_per_jin * jun_to_jin

# Calculate price per 石 (120 斤)
price_per_shi = price_per_jin * shi_to_jin

# Results
a = price_per_jun  # Price per 鈞
b = price_per_jin  # Price per 斤
c = price_per_shi  # Price per 石
d = price_per_jin  # Price per 斤 (same as b)

# Output the results
print(f"Price per 鈞: {a} 錢")
print(f"Price per 斤: {b} 錢")
print(f"Price per 石: {c} 錢")
print(f"Price per 斤 (again): {d} 錢")
#----- content ends here -----


"""


---

### Explanation of Results:
- **a 鈞, b 錢:** The price per **jun** (30 斤) and per **jin** (1 斤).
- **c 石, d 錢:** The price per **shi** (120 斤) and per **jin** (1 斤, same as above).

This code calculates the price per unit weight for each level of measurement.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 5600/33
Variable 'b' has wrong value. Expected: 5, Actual: 560/99
Variable 'c' has wrong value. Expected: 13/12, Actual: 22400/33
Variable 'd' has wrong value. Expected: 6, Actual: 560/99"""
