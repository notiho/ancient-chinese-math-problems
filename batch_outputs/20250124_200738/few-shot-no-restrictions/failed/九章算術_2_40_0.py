"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This is a classic ancient Chinese problem involving proportional distribution of money to calculate the price per unit weight of silk. Let's break it down and encode the solution in Python.

### Problem Breakdown:
- Total money spent: **13,970 (錢)**
- Total weight of silk purchased: **1 石, 2 鈞, 28 斤, 3 兩, 5 銖**
- We need to calculate the price per **斤** (jin) and per **鈞** (jun).

### Conversion Factors:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

### Procedure:
1. Convert the total weight into a single unit (e.g., 銖).
2. Calculate the total number of 銖 in the given weight.
3. Divide the total money by the total weight in 銖 to get the price per 銖.
4. Convert the price per 銖 into the price per **斤** and **鈞**.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970  # 錢

# Total weight purchased
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

# Convert total weight to 銖
total_銖 = (
    石 * 鈞_per_石 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩 +
    鈞 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩 +
    斤 * 兩_per_斤 * 銖_per_兩 +
    兩 * 銖_per_兩 +
    銖
)

# Calculate price per 銖
price_per_銖 = Fraction(total_money, total_銖)

# Convert price per 銖 to price per 斤 and 鈞
price_per_斤 = price_per_銖 * 銖_per_兩 * 兩_per_斤
price_per_鈞 = price_per_斤 * 斤_per_鈞

# Results
a = price_per_斤  # Price per 斤
b = price_per_鈞  # Price per 鈞

# Output
print(f"其 {a} 錢/斤 ，鈞 {b} 錢/鈞。")
#----- content ends here -----


"""


### Explanation:
1. **Weight Conversion**: The total weight is converted into the smallest unit (銖) for precise calculations.
2. **Price Calculation**: The total money is divided by the total weight in 銖 to get the price per 銖. This is then scaled up to get the price per 斤 and 鈞.
3. **Fraction Handling**: The `Fraction` class ensures that the calculations are exact and avoid floating-point inaccuracies.

### Answer:
The output will give the price per **斤** and per **鈞** in terms of 錢.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
