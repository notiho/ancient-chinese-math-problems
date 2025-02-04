"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. Here's how we can solve it step by step:

### Problem Breakdown:
- **Total cost**: 1120 (in money units)
- **Total weight**: 1 石 (shi), 2 鈞 (jun), and 18 斤 (jin)
- We need to calculate the price per 鈞 and per 斤.

### Procedure:
1. Convert the total weight into a single unit (斤).
   - 1 石 = 120 斤
   - 1 鈞 = 30 斤
   - Total weight = \( 1 \times 120 + 2 \times 30 + 18 = 198 \) 斤.

2. Calculate the price per 斤:
   - Price per 斤 = \( \frac{\text{Total cost}}{\text{Total weight}} \)
   - \( \text{Price per 斤} = \frac{1120}{198} \).

3. Calculate the price per 鈞:
   - 1 鈞 = 30 斤.
   - Price per 鈞 = \( 30 \times \text{Price per 斤} \).

4. Express the results in terms of fractions or decimals as needed.

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_cost = 1120  # Total money spent
total_weight_stone = 1  # 石
total_weight_jun = 2  # 鈞
total_weight_jin = 18  # 斤

# Conversion factors
stone_to_jin = 120  # 1 石 = 120 斤
jun_to_jin = 30     # 1 鈞 = 30 斤

# Step 1: Convert total weight to 斤
total_weight_jin = (total_weight_stone * stone_to_jin) + (total_weight_jun * jun_to_jin) + total_weight_jin

# Step 2: Calculate price per 斤
price_per_jin = Fraction(total_cost, total_weight_jin)

# Step 3: Calculate price per 鈞
price_per_jun = price_per_jin * jun_to_jin

# Results
a = price_per_jun  # Price per 鈞
b = price_per_jin  # Price per 斤

# Output results
print(f"Price per 鈞: {a} (money units)")
print(f"Price per 斤: {b} (money units)")
#----- content ends here -----


"""


### Explanation of Results:
- `a` represents the price per 鈞.
- `b` represents the price per 斤.

By running the code, you can calculate the exact values for the price per 鈞 and per 斤.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 5600/33
Variable 'b' has wrong value. Expected: 5, Actual: 560/99
Missing variable in output: 'c'
Missing variable in output: 'd'"""
