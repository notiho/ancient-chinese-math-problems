"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight of silk in different units: per "鈞" (a traditional Chinese unit of weight) and per "石" (another traditional Chinese unit of weight). The total weight and total cost are given, and we need to compute the price per unit.

The problem states:
- Total cost: 1120 錢
- Total weight: 1 石, 2 鈞, 18 斤

We are tasked to compute:
- `a` 錢 per 鈞
- `b` 錢 per 斤
- `c` 錢 per 石
- `d` 錢 per 斤

### Definitions of units:
1 石 = 4 鈞  
1 鈞 = 30 斤  

Thus:
1 石 = 4 鈞 = 4 × 30 斤 = 120 斤  

### Total weight in 斤:
1 石 = 120 斤  
2 鈞 = 2 × 30 斤 = 60 斤  
18 斤 = 18 斤  

Total weight = 120 + 60 + 18 = 198 斤  

### Price per unit:
- Price per 斤 (`b`) = Total cost / Total weight  
- Price per 鈞 (`a`) = Price per 斤 × 斤 per 鈞  
- Price per 石 (`c`) = Price per 斤 × 斤 per 石  
- Price per 斤 (`d`) = Same as `b` (redundant, but included for clarity)

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_cost = 1120  # in 錢
total_weight_in_jin = 120 + 60 + 18  # 1 石, 2 鈞, 18 斤

# Calculations
b = Fraction(total_cost, total_weight_in_jin)  # Price per 斤
a = b * 30  # Price per 鈞 (30 斤 per 鈞)
c = b * 120  # Price per 石 (120 斤 per 石)
d = b  # Price per 斤 (same as b)

# Results
a, b, c, d
#----- content ends here -----


"""


### Explanation of Results:
- `a` is the price per 鈞 in 錢.
- `b` is the price per 斤 in 錢.
- `c` is the price per 石 in 錢.
- `d` is the price per 斤 in 錢 (same as `b`).

This code calculates the values of `a`, `b`, `c`, and `d` using the given data and the relationships between the units.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 5600/33
Variable 'b' has wrong value. Expected: 5, Actual: 560/99
Variable 'c' has wrong value. Expected: 13/12, Actual: 22400/33
Variable 'd' has wrong value. Expected: 6, Actual: 560/99"""
