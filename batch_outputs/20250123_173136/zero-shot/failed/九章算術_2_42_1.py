"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this ancient Chinese math problem, we will translate it into Python code. The problem involves calculating the price per unit weight of silk in different units (石, 鈞, 斤, 兩). Here's the Python code:


"""


from fractions import Fraction

# Total money spent
total_money = 13970  # in 錢

# Total weight of silk purchased
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

# Calculate the price per 銖
price_per_zhu = Fraction(total_money, total_weight_in_zhu)

# Convert the price per 銖 to other units
price_per_liang = price_per_zhu * zhu_per_liang
price_per_jin = price_per_liang * liang_per_jin
price_per_jun = price_per_jin * jin_per_jun
price_per_stone = price_per_jun * jin_per_jun

# Assign the answers to variables
a = price_per_stone  # Price per 石
b = price_per_liang  # Price per 兩
c = price_per_jun    # Price per 鈞
d = price_per_liang  # Price per 兩 (same as b)

# Print the results
print(f"a (price per 石): {a} 錢")
print(f"b (price per 兩): {b} 錢")
print(f"c (price per 鈞): {c} 錢")
print(f"d (price per 兩): {d} 錢")


"""


This code calculates the price per unit weight in various units (石, 鈞, 斤, 兩) based on the total money spent and the total weight of silk purchased. The results are stored in variables `a`, `b`, `c`, and `d` as required.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 4828032000/45389
Variable 'b' has wrong value. Expected: 4, Actual: 335280/45389
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400/45389
Variable 'd' has wrong value. Expected: 5, Actual: 335280/45389"""
