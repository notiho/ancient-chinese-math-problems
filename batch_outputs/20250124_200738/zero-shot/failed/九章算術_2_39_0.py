"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight of silk in terms of "鈞" (jun) and "石" (shi). The total cost is 13,970, and the total weight is 1石 2鈞 28斤 3兩 5銖. The problem asks for the price per "鈞" (a鈞) and the price per "石" (b錢), as well as the price per "石" (c石) and the price per "石" (d錢).

Here is the Python code to compute the values of the unknowns:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in 錢
total_cost = 13970

# Total weight in 錢 (convert to a single unit for calculation)
# 1石 = 4鈞, 1鈞 = 30斤, 1斤 = 16兩, 1兩 = 24銖
total_weight_in_zhu = (
    1 * 4 * 30 * 16 * 24 +  # 1石
    2 * 30 * 16 * 24 +      # 2鈞
    28 * 16 * 24 +          # 28斤
    3 * 24 +                # 3兩
    5                       # 5銖
)

# Price per 銖 (smallest unit)
price_per_zhu = Fraction(total_cost, total_weight_in_zhu)

# Convert price per 銖 to price per 鈞 and price per 石
price_per_jun = price_per_zhu * (30 * 16 * 24)  # 1鈞 = 30斤 * 16兩 * 24銖
price_per_shi = price_per_zhu * (4 * 30 * 16 * 24)  # 1石 = 4鈞 * 30斤 * 16兩 * 24銖

# Extract integer and fractional parts for price per 石
price_per_shi_integer = price_per_shi.numerator // price_per_shi.denominator
price_per_shi_fraction = Fraction(price_per_shi.numerator % price_per_shi.denominator, price_per_shi.denominator)

# Assign the results to variables
a = price_per_jun  # Price per 鈞
b = price_per_shi_integer  # Integer part of price per 石
c = price_per_shi_fraction.numerator  # Numerator of fractional part of price per 石
d = price_per_shi_fraction.denominator  # Denominator of fractional part of price per 石

# Results
a, b, c, d
#----- content ends here -----


"""


This code calculates the price per "鈞" (`a`), the integer part of the price per "石" (`b`), and the fractional part of the price per "石" (`c` and `d`). The results are stored in the variables `a`, `b`, `c`, and `d`.
"""


"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 68201
Variable 'd' has wrong value. Expected: 8052, Actual: 79949"""
