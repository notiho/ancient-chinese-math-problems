"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this problem, we need to break it down step by step according to the procedure described. Here's the Python code:


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
法 = (石 * 1200) + (鈞 * 100) + (斤 * 16) + (兩 * 1) + Fraction(銖, 24)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
斤率 = Fraction(實, 法)

# 計算每單位的價格
a = 斤率 * 16  # 每斤的價格
b = 斤率 * 100  # 每鈞的價格
c = 斤率 * 1200  # 每石的價格
d = b  # 每鈞的價格 (鈞率 already calculated)

# Output results
a, b, c, d


"""


Explanation:
1. The total amount of money (`錢數`) is divided by the total weight (`法`), which is calculated by converting all units (石, 鈞, 斤, 兩, 銖) into a common base (銖).
2. The resulting rate (`斤率`) is used to calculate the price per unit (斤, 鈞, 石).
3. The results `a`, `b`, `c`, and `d` represent the price per 斤, 鈞, and 石, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 487680/4039
Variable 'b' has wrong value. Expected: 2012, Actual: 3048000/4039
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 36576000/4039
Variable 'd' has wrong value. Expected: 2013, Actual: 3048000/4039"""
