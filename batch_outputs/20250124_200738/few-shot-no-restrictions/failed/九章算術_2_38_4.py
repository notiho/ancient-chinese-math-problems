"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. Here's the solution encoded in Python:

### Problem Breakdown:
- Total money spent: 1120 (錢)
- Total weight of silk: 1 石, 2 鈞, and 18 斤
- 1 石 = 4 鈞, 1 鈞 = 30 斤
- The goal is to calculate the price per 鈞 and the price per 斤.

### Procedure:
1. Convert the total weight into a single unit (斤).
2. Calculate the price per 斤 by dividing the total money by the total weight in 斤.
3. Calculate the price per 鈞 by multiplying the price per 斤 by the number of 斤 in 1 鈞 (30 斤).

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
錢 = 1120

# Total weight: 1 石, 2 鈞, 18 斤
石 = 1
鈞 = 2
斤 = 18

# Conversion factors
石_to_鈞 = 4
鈞_to_斤 = 30

# Convert total weight to 斤
total_斤 = (石 * 石_to_鈞 * 鈞_to_斤) + (鈞 * 鈞_to_斤) + 斤

# Calculate price per 斤
price_per_斤 = Fraction(錢, total_斤)

# Calculate price per 鈞
price_per_鈞 = price_per_斤 * 鈞_to_斤

# Output results
a = price_per_鈞  # Price per 鈞
b = price_per_斤  # Price per 斤

# Print results
print(f"Price per 鈞: {a} 錢")
print(f"Price per 斤: {b} 錢")
#----- content ends here -----


"""


### Explanation of Variables:
- `total_斤`: The total weight in 斤.
- `price_per_斤`: The price per 斤, calculated as total money divided by total weight in 斤.
- `price_per_鈞`: The price per 鈞, calculated as the price per 斤 multiplied by 30 (斤 in 1 鈞).

### Answer:
- `a`: Price per 鈞 in 錢.
- `b`: Price per 斤 in 錢.


"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 5600/33
Variable 'b' has wrong value. Expected: 5, Actual: 560/99
Missing variable in output: 'c'
Missing variable in output: 'd'"""
