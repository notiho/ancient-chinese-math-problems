"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the rates for each unit of weight (石, 鈞, 斤, 兩, 銖). Here's the Python code following the procedure:


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
石法 = 石 * 1
鈞法 = 鈞 * 10
斤法 = 斤 * 100
兩法 = 兩 * 1000
銖法 = 銖 * 10000

# 以所率乘錢數為實
石實 = 錢數 * 石法
鈞實 = 錢數 * 鈞法

# 實如法而一
a = Fraction(石實, 石法)
b = Fraction(石實, 鈞法)

c = Fraction(鈞實, 石法)
d = Fraction(鈞實, 鈞法)

# Output results
print(f"其 {a} 石 ，兩 {b} 錢 。其 {c} 鈞 ，兩 {d} 錢 。")


"""


This code calculates the rates for 石 and 鈞 based on the given procedure. Each calculation adheres to the ancient Chinese method of dividing the total money by the respective unit's weight.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 13970
Variable 'b' has wrong value. Expected: 4, Actual: 1397/2
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 279400
Variable 'd' has wrong value. Expected: 5, Actual: 13970"""
