"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit of silk (石, 鈞, 斤, 兩, 銖). Let's proceed step by step according to the procedure described.


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

# 各置所買石、鈞、斤、兩以為法
# Convert everything to 銖 (smallest unit) for calculation
銖_per_兩 = 24
銖_per_斤 = 16 * 銖_per_兩
銖_per_鈞 = 30 * 銖_per_斤
銖_per_石 = 4 * 銖_per_鈞

總銖 = (石 * 銖_per_石) + (鈞 * 銖_per_鈞) + (斤 * 銖_per_斤) + (兩 * 銖_per_兩) + 銖

# 以所率乘錢數為實
實 = 錢數 * 總銖

# 實如法而一
# Calculate the price per 銖
每銖價格 = Fraction(錢數, 總銖)

# Convert the price back to 石 and 鈞 rates
每石價格 = 每銖價格 * 銖_per_石
每鈞價格 = 每銖價格 * 銖_per_鈞

# Results
a = 每鈞價格.numerator  # 鈞的價格 (分子)
b = 每鈞價格.denominator  # 鈞的價格 (分母)
c = 每石價格.numerator  # 石的價格 (分子)
d = 每石價格.denominator  # 石的價格 (分母)


"""
 

### Explanation:
1. Convert all units (石, 鈞, 斤, 兩, 銖) into the smallest unit (銖) for accurate calculations.
2. Calculate the total number of 銖 in the purchased silk.
3. Use the total money spent (`錢數`) to calculate the price per 銖.
4. Convert the price per 銖 back into the price per 石 and 鈞 for the final answer.

This ensures the procedure is followed exactly as described.
"""


"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 160934400
Variable 'b' has wrong value. Expected: 8051, Actual: 79949
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 643737600
Variable 'd' has wrong value. Expected: 8052, Actual: 79949"""
