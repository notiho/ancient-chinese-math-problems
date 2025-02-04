"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (石, 鈞, 斤, 兩, 銖) of silk based on the total cost and the total weight. Here's the step-by-step procedure encoded in Python:

### Problem Breakdown:
- Total money spent: 13,970 (錢)
- Total weight of silk: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- The goal is to calculate the price per 石 (石率) and per 鈞 (鈞率).

### Conversion Factors:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

### Procedure:
1. Convert the total weight into 銖 (the smallest unit).
2. Calculate the price per 銖 by dividing the total money by the total weight in 銖.
3. Convert the price per 銖 back into the price per 鈞 and per 石.

Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970  # 錢

# Total weight: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
銖_per_兩 = 24
兩_per_斤 = 16
斤_per_鈞 = 30
鈞_per_石 = 4

# Step 1: Convert total weight to 銖
total_銖 = (
    銖 +
    兩 * 銖_per_兩 +
    斤 * 銖_per_兩 * 兩_per_斤 +
    鈞 * 銖_per_兩 * 兩_per_斤 * 斤_per_鈞 +
    石 * 銖_per_兩 * 兩_per_斤 * 斤_per_鈞 * 鈞_per_石
)

# Step 2: Calculate price per 銖
price_per_銖 = Fraction(total_money, total_銖)

# Step 3: Convert price per 銖 to price per 鈞 and per 石
price_per_鈞 = price_per_銖 * 銖_per_兩 * 兩_per_斤 * 斤_per_鈞
price_per_石 = price_per_鈞 * 鈞_per_石

# Results
a = price_per_鈞  # Price per 鈞
b = price_per_石  # Price per 石

print(f"Price per 鈞: {a} 錢")
print(f"Price per 石: {b} 錢")
#----- content ends here -----


"""


### Explanation of Results:
- `a` represents the price per 鈞 (in 錢).
- `b` represents the price per 石 (in 錢).

This code calculates the price rates based on the given total cost and weight, following the ancient Chinese method described in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 160934400/79949
Variable 'b' has wrong value. Expected: 8051, Actual: 643737600/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
