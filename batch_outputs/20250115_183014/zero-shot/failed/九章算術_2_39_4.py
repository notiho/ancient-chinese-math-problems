"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight of silk in different units: per "鈞" (a unit of weight) and per "石" (another unit of weight). The problem specifies the total cost of the silk and its total weight in terms of "石", "鈞", "斤", "兩", and "銖". The solution involves converting the total weight into a single unit and dividing the total cost by the weight to find the price per unit.

Here is the Python code to compute the values of the unknowns `a`, `b`, `c`, and `d`:


"""


from fractions import Fraction

# Total cost in money
total_cost = 13970  # in 錢

# Total weight of silk
total_weight_stone = 1  # 石
total_weight_jun = 2  # 鈞
total_weight_jin = 28  # 斤
total_weight_liang = 3  # 兩
total_weight_zhu = 5  # 銖

# Conversion factors
jin_per_jun = 30  # 1 鈞 = 30 斤
liang_per_jin = 16  # 1 斤 = 16 兩
zhu_per_liang = 24  # 1 兩 = 24 銖
jin_per_stone = 300  # 1 石 = 300 斤

# Convert total weight to 鈞
total_weight_in_jun = (
    total_weight_stone * jin_per_stone / jin_per_jun
    + total_weight_jun
    + total_weight_jin / jin_per_jun
    + total_weight_liang / (jin_per_jun * liang_per_jin)
    + total_weight_zhu / (jin_per_jun * liang_per_jin * zhu_per_liang)
)

# Convert total weight to 石
total_weight_in_stone = (
    total_weight_stone
    + total_weight_jun / (jin_per_stone / jin_per_jun)
    + total_weight_jin / jin_per_stone
    + total_weight_liang / (jin_per_stone * liang_per_jin)
    + total_weight_zhu / (jin_per_stone * liang_per_jin * zhu_per_liang)
)

# Calculate rates
a = Fraction(total_cost, total_weight_in_jun)  # 錢 per 鈞
b = a  # 錢 per 鈞 (same as a, as per the problem statement)
c = Fraction(total_cost, total_weight_in_stone)  # 錢 per 石
d = c  # 錢 per 石 (same as c, as per the problem statement)

# Results
a, b, c, d


"""


This code calculates the price per "鈞" (`a` and `b`) and the price per "石" (`c` and `d`) using the given total cost and weight. The results are stored in the variables `a`, `b`, `c`, and `d` as fractions for precise representation.
"""


"""
Code error: both arguments should be Rational instances"""
