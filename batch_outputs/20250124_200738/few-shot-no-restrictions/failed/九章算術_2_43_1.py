"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the price per unit weight (in this case, per "銖") based on the total cost and the total weight of silk purchased. Let's break it down and encode the solution in Python.

---

### Problem Breakdown:
- Total money spent: **13,970 (錢)**
- Total weight of silk: **1 石, 2 鈞, 28 斤, 3 兩, 5 銖**
- We need to calculate the price per unit weight (銖 rate).

---

### Conversion of weights:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

Thus, we first convert the total weight into the smallest unit, **銖**.

---

### Procedure:
1. Convert the total weight into 銖.
2. Divide the total money by the total weight in 銖 to get the price per 銖.
3. Express the price per 銖 in terms of 鈞 and 錢, and also in terms of 石 and 錢.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970  # in 錢

# Total weight of silk
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
鈞_per_石 = 4
斤_per_鈞 = 30
兩_per_斤 = 16
銖_per_兩 = 24

# Convert total weight to 銖
total_weight_in_銖 = (
    石 * 鈞_per_石 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩 +
    鈞 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩 +
    斤 * 兩_per_斤 * 銖_per_兩 +
    兩 * 銖_per_兩 +
    銖
)

# Calculate price per 銖
price_per_銖 = Fraction(total_money, total_weight_in_銖)

# Convert price per 銖 into 鈞 and 錢
price_per_鈞 = price_per_銖 * 銖_per_兩 * 兩_per_斤 * 斤_per_鈞
price_per_石 = price_per_鈞 * 鈞_per_石

# Extract integer and fractional parts for 鈞 and 錢
a = price_per_鈞.numerator // price_per_鈞.denominator  # Integer part (鈞)
b = price_per_鈞 - a  # Fractional part (in 錢)

# Extract integer and fractional parts for 石 and 錢
c = price_per_石.numerator // price_per_石.denominator  # Integer part (石)
d = price_per_石 - c  # Fractional part (in 錢)

# Output the results
print(f"其 {a} 鈞, {b} 錢 一銖。")
print(f"其 {c} 石, {d} 錢 一銖。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into the smallest unit, 銖, using the given conversion factors.
2. **Price Calculation**: The total money is divided by the total weight in 銖 to get the price per 銖.
3. **Unit Conversion**: The price per 銖 is converted into larger units (鈞 and 石) for better readability.
4. **Output**: The results are expressed in terms of 鈞 and 錢, and 石 and 錢.

---

### Example Output:
If you run the code with the given inputs, it will calculate the price per 銖 and express it in the required units.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 2012
Variable 'b' has wrong value. Expected: 5, Actual: 77012/79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 8051
Variable 'd' has wrong value. Expected: 6, Actual: 68201/79949"""
