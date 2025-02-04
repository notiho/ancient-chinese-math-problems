"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the price per unit (石, 鈞, 斤, 兩) for a given total cost and weight of silk. Here's the Python code:


"""


from fractions import Fraction

# Given data
total_money = 13970  # Total money spent
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

# Calculate price per 銖
price_per_zhu = Fraction(total_money, total_weight_in_zhu)

# Convert price per 銖 to price per 石, 鈞, 斤, and 兩
a = price_per_zhu * jin_per_jun * liang_per_jin * zhu_per_liang  # Price per 石
b = price_per_zhu * liang_per_jin * zhu_per_liang  # Price per 鈞
c = price_per_zhu * zhu_per_liang  # Price per 斤
d = price_per_zhu  # Price per 銖

# Results
a = a.limit_denominator()  # Simplify fractions
b = b.limit_denominator()
c = c.limit_denominator()
d = d.limit_denominator()

# Output variables
a, b, c, d


"""


This code calculates the price per unit (石, 鈞, 斤, 兩) based on the given total cost and weight. The results are stored in the variables `a`, `b`, `c`, and `d`.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 160934400/45389
Variable 'b' has wrong value. Expected: 4, Actual: 5364480/45389
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 335280/45389
Variable 'd' has wrong value. Expected: 5, Actual: 13970/45389"""
