"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight of silk in terms of "鈞" (jins) and "石" (shihs). The total cost is 13,970 units of money, and the total weight is 1 石 (shih), 2 鈞 (jins), 28 斤 (jin), 3 兩 (liang), and 5 銖 (zhu). 

The conversion factors are:
- 1 石 = 4 鈞
- 1 鈞 = 30 斤
- 1 斤 = 16 兩
- 1 兩 = 24 銖

We first convert the total weight into 銖 (zhu), calculate the price per 銖, and then convert the price back into 鈞 and 石 units.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money
total_money = 13970

# Total weight in 石, 鈞, 斤, 兩, 銖
weight_shih = 1
weight_jin = 2
weight_jin_jin = 28
weight_liang = 3
weight_zhu = 5

# Conversion factors
shih_to_jin = 4
jin_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Convert total weight to 銖 (zhu)
total_weight_zhu = (
    (weight_shih * shih_to_jin * jin_to_jin * jin_to_liang * liang_to_zhu) +
    (weight_jin * jin_to_jin * jin_to_liang * liang_to_zhu) +
    (weight_jin_jin * jin_to_liang * liang_to_zhu) +
    (weight_liang * liang_to_zhu) +
    weight_zhu
)

# Calculate price per 銖 (zhu)
price_per_zhu = Fraction(total_money, total_weight_zhu)

# Convert price per 銖 to 鈞 (jin) and 石 (shih)
price_per_liang = price_per_zhu * liang_to_zhu
price_per_jin = price_per_liang * jin_to_liang
price_per_jin = Fraction(price_per_jin)
price_per_shih = price_per_jin * jin_to_jin

# Assign results to variables
a = price_per_jin  # Price per 鈞
b = price_per_shih  # Price per 石
c = price_per_shih  # Price per 石
d = price_per_shih  # Price per 石

# Results
a, b, c, d
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 8051, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 160934400/79949
Variable 'd' has wrong value. Expected: 8052, Actual: 160934400/79949"""
