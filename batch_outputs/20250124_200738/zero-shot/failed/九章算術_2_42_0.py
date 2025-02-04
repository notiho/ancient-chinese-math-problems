"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit of silk in terms of 石 (shi), 鈞 (jun), 斤 (jin), and 銖 (zhu). The total cost is 13,970 units of money, and the total weight of the silk is 1 石, 2 鈞, 28 斤, 3 兩, and 5 銖. 

We will calculate the price per unit for each of these measurements. Here's the Python code to compute the values of `a`, `b`, `c`, and `d`:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in money
total_money = 13970

# Total weight in terms of 石, 鈞, 斤, 兩, 銖
# 1 石 = 4 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
total_weight_in_zhu = (
    1 * 4 * 30 * 16 * 24 +  # 石 to 銖
    2 * 30 * 16 * 24 +      # 鈞 to 銖
    28 * 16 * 24 +          # 斤 to 銖
    3 * 24 +                # 兩 to 銖
    5                       # 銖
)

# Price per 銖
price_per_zhu = Fraction(total_money, total_weight_in_zhu)

# Convert price per 銖 to price per 石
price_per_shi = price_per_zhu * (4 * 30 * 16 * 24)
a = price_per_shi.numerator  # Price per 石 in whole units
b = price_per_shi - a        # Remaining fraction of the price per 石
b = b * (4 * 30 * 16 * 24)   # Convert remaining fraction to 錢
b = b.numerator

# Convert price per 銖 to price per 鈞
price_per_jun = price_per_zhu * (30 * 16 * 24)
c = price_per_jun.numerator  # Price per 鈞 in whole units
d = price_per_jun - c        # Remaining fraction of the price per 鈞
d = d * (30 * 16 * 24)       # Convert remaining fraction to 錢
d = d.numerator

# Output the results
print("其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")
#----- content ends here -----


"""


This code calculates the values of `a`, `b`, `c`, and `d` based on the given problem. The results are stored in the variables `a`, `b`, `c`, and `d`.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600
Variable 'b' has wrong value. Expected: 4, Actual: -2371531790352384000
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400
Variable 'd' has wrong value. Expected: 5, Actual: -148220736897024000"""
