"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this ancient Chinese math problem, we will translate the problem into Python code. The problem involves calculating the price per "斤" (jin) and per "鈞" (jun), as well as the price per "石" (shi) and per "鈞" (jun). Here's the solution:


"""


from fractions import Fraction

# Given values
total_money = 13970  # in 錢
total_weight_shi = 1  # 石
total_weight_jun = 2  # 鈞
total_weight_jin = 28  # 斤
total_weight_liang = 3  # 兩
total_weight_zhu = 5  # 銖

# Convert all weights to 銖 (smallest unit)
shi_to_zhu = 120000  # 1 石 = 120000 銖
jun_to_zhu = 20000   # 1 鈞 = 20000 銖
jin_to_zhu = 1600    # 1 斤 = 1600 銖
liang_to_zhu = 100   # 1 兩 = 100 銖
zhu_to_zhu = 1       # 1 銖 = 1 銖

total_weight_in_zhu = (
    total_weight_shi * shi_to_zhu +
    total_weight_jun * jun_to_zhu +
    total_weight_jin * jin_to_zhu +
    total_weight_liang * liang_to_zhu +
    total_weight_zhu * zhu_to_zhu
)

# Calculate the price per 銖
price_per_zhu = Fraction(total_money, total_weight_in_zhu)

# Convert the price per 銖 to price per 斤 and price per 鈞
price_per_jin = price_per_zhu * jin_to_zhu  # Price per 斤 in 錢
price_per_jun = price_per_zhu * jun_to_zhu  # Price per 鈞 in 錢

# Convert the price per 鈞 to price per 石
price_per_shi = price_per_jun * (shi_to_zhu // jun_to_zhu)  # Price per 石 in 錢

# Assign the results to the variables
a = price_per_jin  # Price per 斤 in 錢
b = price_per_jun  # Price per 鈞 in 錢
c = price_per_shi  # Price per 石 in 錢
d = price_per_jun  # Price per 鈞 in 錢

# Print the results
print(f"a = {a} 錢 per 斤")
print(f"b = {b} 錢 per 鈞")
print(f"c = {c} 錢 per 石")
print(f"d = {d} 錢 per 鈞")


"""


This code calculates the price per unit weight (斤, 鈞, 石) based on the total money and total weight provided in the problem. The results are stored in variables `a`, `b`, `c`, and `d` as required.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 35200/323
Variable 'b' has wrong value. Expected: 2012, Actual: 440000/323
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 2640000/323
Variable 'd' has wrong value. Expected: 2013, Actual: 440000/323"""
