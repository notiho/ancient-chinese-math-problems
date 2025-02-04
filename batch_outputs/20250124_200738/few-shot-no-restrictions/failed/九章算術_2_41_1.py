"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. The weight is given in a traditional Chinese system of units: 石 (shi), 鈞 (jun), 斤 (jin), 兩 (liang), and 銖 (zhu). The solution involves converting the weight into a single unit (jin) and then dividing the total cost by the total weight to find the price per jin.

---

### Problem Breakdown:
- **Total cost**: 13,970 (錢)
- **Total weight**: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- Conversion factors:
  - 1 石 = 4 鈞
  - 1 鈞 = 30 斤
  - 1 斤 = 16 兩
  - 1 兩 = 24 銖

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in 錢
total_cost = 13970

# Total weight in traditional units
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
石_to_斤 = 4 * 30  # 1 石 = 4 鈞, 1 鈞 = 30 斤
鈞_to_斤 = 30       # 1 鈞 = 30 斤
斤_to_兩 = 16       # 1 斤 = 16 兩
兩_to_銖 = 24       # 1 兩 = 24 銖

# Convert all weights to 斤
total_weight_in_斤 = (
    石 * 石_to_斤 +
    鈞 * 鈞_to_斤 +
    斤 +
    Fraction(兩, 斤_to_兩) +  # Convert 兩 to 斤
    Fraction(銖, 斤_to_兩 * 兩_to_銖)  # Convert 銖 to 斤
)

# Calculate price per 斤
price_per_斤 = Fraction(total_cost, total_weight_in_斤)

# Convert price per 斤 to 錢
a = 石
b = price_per_斤
c = 1  # For 1 斤
d = price_per_斤

# Output the results
print(f"其 {a} 石，斤 {b} 錢。其 {c} 斤，斤 {d} 錢。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Weight Conversion**:
   - Convert all the given weights (石, 鈞, 斤, 兩, 銖) into a single unit (斤) using the provided conversion factors.
   - Use the `Fraction` class to ensure precision in calculations, especially for non-integer values.

2. **Price Calculation**:
   - Divide the total cost (in 錢) by the total weight (in 斤) to get the price per 斤.

3. **Output**:
   - The results are presented in the format specified in the problem: the price per 石 and the price per 斤.

---

### Example Output:
If you run the code, it will calculate the price per 石 and per 斤 based on the given inputs. The result will be in terms of 錢.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 1
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/79949
Variable 'c' has wrong value. Expected: 7897/384, Actual: 1
Variable 'd' has wrong value. Expected: 68, Actual: 5364480/79949"""
