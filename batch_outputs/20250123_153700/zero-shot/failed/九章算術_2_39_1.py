"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
To solve this ancient Chinese math problem, we need to compute the values of the unknowns `a`, `b`, `c`, and `d`. Here's the Python code to compute these values:


"""


from fractions import Fraction

# Given values
total_money = 13970  # in 錢
total_weight_stone = 1  # 石
total_weight_jun = 2  # 鈞
total_weight_jin = 28  # 斤
total_weight_liang = 3  # 兩
total_weight_zhu = 5  # 銖

# Conversion factors
jin_per_jun = 30  # 1 鈞 = 30 斤
liang_per_jin = 16  # 1 斤 = 16 兩
zhu_per_liang = 24  # 1 兩 = 24 銖

# Convert total weight to 銖 (smallest unit)
total_weight_in_zhu = (
    total_weight_stone * jin_per_jun * liang_per_jin * zhu_per_liang +
    total_weight_jun * jin_per_jun * liang_per_jin * zhu_per_liang +
    total_weight_jin * liang_per_jin * zhu_per_liang +
    total_weight_liang * zhu_per_liang +
    total_weight_zhu
)

# Calculate the rate per 銖
rate_per_zhu = Fraction(total_money, total_weight_in_zhu)

# Convert the rate back to 石, 鈞, 斤, 兩, 銖
rate_per_stone = rate_per_zhu * jin_per_jun * liang_per_jin * zhu_per_liang
rate_per_jun = rate_per_zhu * liang_per_jin * zhu_per_liang
rate_per_jin = rate_per_zhu * zhu_per_liang
rate_per_liang = rate_per_zhu

# Assign the answers
a = rate_per_jun  # 鈞 rate
b = rate_per_stone  # 石 rate
c = rate_per_stone  # 石 rate (same as b)
d = rate_per_stone  # 石 rate (same as b)

# Print the results
print(f"a = {a} 鈞")
print(f"b = {b} 錢")
print(f"c = {c} 石")
print(f"d = {d} 錢")


"""


This code calculates the rates for the given problem and assigns the values to the variables `a`, `b`, `c`, and `d`. Note that the units are preserved in the comments for clarity.
"""


"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 5364480/45389
Variable 'b' has wrong value. Expected: 8051, Actual: 160934400/45389
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 160934400/45389
Variable 'd' has wrong value. Expected: 8052, Actual: 160934400/45389"""
