"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
The problem you provided is complex and involves calculating the unit price of silk based on the total cost and weight. However, the description of the procedure ("反其率術") is somewhat ambiguous and requires careful interpretation. Let me attempt to break it down and translate it into Python code.

### Problem Breakdown:
- Total money: 13,970 (錢)
- Total weight of silk: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- Goal: Calculate the unit price per 銖 (smallest unit of weight).

### Procedure ("反其率術"):
1. Use the total money as the divisor (法).
2. Use the total weight as the dividend (實).
3. Divide the total weight by the total money to get the unit price per 銖.
4. If the result is not an integer, adjust the calculation by subtracting the remainder from the divisor.

Let's now implement this in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total money (錢)
錢數 = 13970

# Total weight of silk: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
石_to_鈞 = 30
鈞_to_斤 = 4
斤_to_兩 = 16
兩_to_銖 = 24

# Convert total weight to 銖
總銖 = (石 * 石_to_鈞 * 鈞_to_斤 * 斤_to_兩 * 兩_to_銖 +
       鈞 * 鈞_to_斤 * 斤_to_兩 * 兩_to_銖 +
       斤 * 斤_to_兩 * 兩_to_銖 +
       兩 * 兩_to_銖 +
       銖)

# Use the total money as the divisor (法) and total weight as the dividend (實)
法 = 錢數
實 = 總銖

# Calculate the unit price per 銖
unit_price_per_銖 = Fraction(實, 法)

# Convert the unit price back to 鈞 and 銖
a = unit_price_per_銖.numerator // unit_price_per_銖.denominator  # 鈞
b = unit_price_per_銖.numerator % unit_price_per_銖.denominator   # 銖

# Convert the unit price back to 石 and 銖
c = a // 石_to_鈞  # 石
d = a % 石_to_鈞    # 銖

# Output the results
print(f"其 {a} 鈞, {b} 銖 一錢。其 {c} 石, {d} 銖 一錢。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into the smallest unit (銖) using the given conversion factors.
2. **Unit Price Calculation**: The total weight (實) is divided by the total money (法) to get the unit price per 銖.
3. **Result Conversion**: The unit price is converted back into larger units (鈞 and 石) for clarity.

### Output:
The output will provide the unit price in terms of 鈞 and 銖 per 錢, as well as 石 and 銖 per 錢.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 4
Variable 'b' has wrong value. Expected: 5, Actual: 4101
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 0
Variable 'd' has wrong value. Expected: 6, Actual: 4"""
