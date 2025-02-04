"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit for each weight unit (石, 鈞, 斤, 兩, 銖). Here's the Python code:


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
石法 = 石 * 1
鈞法 = 石 * 10 + 鈞
斤法 = 石 * 100 + 鈞 * 10 + 斤
兩法 = 石 * 1000 + 鈞 * 100 + 斤 * 10 + 兩

# 計算每單位的價格
# 石的價格
石實 = 錢數 * 石法
a = Fraction(石實, 石法)

# 鈞的價格
鈞實 = 錢數 * 鈞法
c = Fraction(鈞實, 鈞法)

# 兩的價格
兩實 = 錢數 * 兩法
b = Fraction(兩實, 兩法)
d = Fraction(兩實, 兩法)

# Output results
print(f"其 {a} 石 ，兩 {b} 錢 。其 {c} 鈞 ，兩 {d} 錢 。")
#----- content ends here -----


"""


This code calculates the price per 石 and 鈞, as well as the price per 兩. Each calculation follows the procedure described in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 13970
Variable 'b' has wrong value. Expected: 4, Actual: 13970
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 13970
Variable 'd' has wrong value. Expected: 5, Actual: 13970"""
