"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This problem involves calculating the price per unit weight (斤, 鈞, 石) based on the total cost and the total weight. Let's translate the procedure into Python code step by step.


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
# Convert everything to 銖 (smallest unit for calculation)
銖_per_兩 = 24
銖_per_斤 = 16 * 銖_per_兩
銖_per_鈞 = 30 * 銖_per_斤
銖_per_石 = 4 * 銖_per_鈞

# Total weight in 銖
總銖 = (
    石 * 銖_per_石 +
    鈞 * 銖_per_鈞 +
    斤 * 銖_per_斤 +
    兩 * 銖_per_兩 +
    銖
)

# 以所率乘錢數為實
實 = 錢數 * 總銖

# 實如法而一
# Calculate the price per 銖
每銖價格 = Fraction(錢數, 總銖)

# Convert the price per 銖 to the price per 斤 and per 鈞
每斤價格 = 每銖價格 * 銖_per_斤
每鈞價格 = 每銖價格 * 銖_per_鈞
每石價格 = 每銖價格 * 銖_per_石

# Results
a = 每斤價格  # Price per 斤
b = 每鈞價格  # Price per 鈞
c = 每石價格  # Price per 石
d = 每鈞價格  # Price per 鈞 (repeated for clarity)
#----- content ends here -----


"""


### Explanation of Variables:
- `總銖`: Total weight in 銖 (smallest unit).
- `每銖價格`: Price per 銖, calculated by dividing the total money by the total weight in 銖.
- `每斤價格`, `每鈞價格`, `每石價格`: Prices per 斤, 鈞, and 石, respectively, derived from the price per 銖.

### Final Answer:
- `a`: Price per 斤.
- `b`: Price per 鈞.
- `c`: Price per 石.
- `d`: Price per 鈞 (same as `b` for clarity).
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 2013, Actual: 160934400/79949"""
