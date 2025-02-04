"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (斤) for different units (鈞 and 石). Let's translate the problem into Python code.

The given data is:
- Total money spent: 1120 (錢)
- Total weight: 1 石, 2 鈞, 18 斤
- We need to calculate the price per 斤 for 鈞 and 石.

We will use the following relationships:
1 石 = 4 鈞  
1 鈞 = 30 斤  

Thus, 1 石 = 4 × 30 = 120 斤.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_money = 1120  # in 錢
total_weight_stone = 1  # 石
total_weight_jun = 2  # 鈞
total_weight_jin = 18  # 斤

# Conversion factors
stone_to_jin = 120  # 1 石 = 120 斤
jun_to_jin = 30  # 1 鈞 = 30 斤

# Total weight in 斤
total_weight_jin = (total_weight_stone * stone_to_jin) + (total_weight_jun * jun_to_jin) + total_weight_jin

# Price per 斤
price_per_jin = Fraction(total_money, total_weight_jin)

# Price per 鈞
a = price_per_jin * jun_to_jin

# Price per 石
c = price_per_jin * stone_to_jin

# Output results
b = price_per_jin  # Price per 斤 for 鈞
d = price_per_jin  # Price per 斤 for 石

# Results
a, b, c, d
#----- content ends here -----


"""


### Explanation of Variables:
- `a`: Price per 鈞 (斤 rate for 鈞)
- `b`: Price per 斤 for 鈞
- `c`: Price per 石 (斤 rate for 石)
- `d`: Price per 斤 for 石

### Final Results:
The code will compute the values of `a`, `b`, `c`, and `d` as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 5600/33
Variable 'b' has wrong value. Expected: 5, Actual: 560/99
Variable 'c' has wrong value. Expected: 13/12, Actual: 22400/33
Variable 'd' has wrong value. Expected: 6, Actual: 560/99"""
