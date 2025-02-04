"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this problem, we need to calculate the rate per unit (鈞, 斤, 石) based on the total amount of money and the total weight of silk purchased. Let's break it down step by step according to the procedure provided.

---

### Definitions and Initial Values



---

### Calculate the Rate per 銖



---

### Calculate Rates for 鈞 and 石



---

### Results


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

# Convert everything to 銖 (smallest unit)
# 1 石 = 4 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總銖 = (石 * 4 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# Each 銖's rate in terms of money
銖率 = Fraction(錢數, 総銖)

# 1 鈞 = 30 斤 = 30 * 16 * 24 銖
鈞率 = 銖率 * (30 * 16 * 24)

# 1 石 = 4 鈞 = 4 * 30 * 16 * 24 銖
石率 = 銖率 * (4 * 30 * 16 * 24)

# 鈞率 and 石率 are the answers
a = Fraction(銖率, (16 * 24))  # Rate per 斤
b = 鈞率                       # Rate per 鈞
c = 石率                       # Rate per 石
d = 鈞率                       # Rate per 鈞 (repeated for clarity)
#----- content ends here -----


"""

"""


"""
Code error: name '総銖' is not defined"""
