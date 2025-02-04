"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (石, 鈞, 斤, etc.) based on the total cost and the total weight. Here's the step-by-step procedure encoded in Python:


"""


from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 將所有單位轉換為銖 (最小單位)
# 1 石 = 4 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總銖 = (石 * 4 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 計算每銖的價格
每銖價格 = Fraction(錢數, 總銖)

# 計算每單位的價格
# 每石的價格
每石價格 = 每銖價格 * (4 * 30 * 16 * 24)

# 每鈞的價格
每鈞價格 = 每銖價格 * (30 * 16 * 24)

# 每斤的價格
每斤價格 = 每銖價格 * (16 * 24)

# 每兩的價格
每兩價格 = 每銖價格 * 24

# 結果
a = 每石價格
b = 每兩價格
c = 每鈞價格
d = 每兩價格

# Output the results
print(f"其 {a} 石 ，兩 {b} 錢 。其 {c} 鈞 ，兩 {d} 錢 。")


"""


This code follows the procedure described in the problem, converting all units to the smallest unit (銖), calculating the price per unit, and then determining the price for each larger unit (石, 鈞, etc.).
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 4, Actual: 335280/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400/79949
Variable 'd' has wrong value. Expected: 5, Actual: 335280/79949"""
