"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this problem, we need to break it down step by step according to the procedure described. Here's the Python implementation:


"""

#----- content starts here -----

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
法 = (石 * 1200) + (鈞 * 100) + (斤 * 16) + (兩 * 1) + (銖 * Fraction(1, 24))

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
斤率 = Fraction(實, 法)

# 計算各部分的錢數
石錢 = 斤率 * 1200
鈞錢 = 斤率 * 100
斤錢 = 斤率 * 16
兩錢 = 斤率 * 1
銖錢 = 斤率 * Fraction(1, 24)

# 結果
a = 斤錢
b = 鈞錢
c = 石錢
d = 鈞錢
#----- content ends here -----


"""


### Explanation:
1. **法**: The total weight in terms of a unified unit (銖). Each unit is converted to銖 and summed up.
2. **斤率**: The rate per unit weight is calculated by dividing the total money by the total weight (`法`).
3. **各部分的錢數**: The money corresponding to each unit (石, 鈞, 斤, 兩, 銖) is calculated by multiplying the rate by the respective weight.

Let me know if you need further clarification!
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 487680/4039
Variable 'b' has wrong value. Expected: 2012, Actual: 3048000/4039
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 36576000/4039
Variable 'd' has wrong value. Expected: 2013, Actual: 3048000/4039"""
