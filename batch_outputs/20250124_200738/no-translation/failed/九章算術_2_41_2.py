"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (斤) based on the total amount of money and the total weight of silk purchased. Here's how we can translate the procedure into Python code:


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

# 將所有重量轉換為斤
# 1 石 = 120 斤, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總斤 = (石 * 120) + (鈞 * 30) + 斤 + Fraction(兩, 16) + Fraction(銖, 16 * 24)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
斤率 = Fraction(實, 總斤)

# 結果
a = 石
b = 斤率
c = 總斤
d = 斤率

# Output
print(f"其 {a}石 ，斤 {b}錢 。其 {c}斤 ，斤 {d}錢 。")
#----- content ends here -----


"""


### Explanation:
1. **Convert all weights to 斤**: Since the problem involves mixed units (石, 鈞, 斤, 兩, 銖), we first convert everything into a single unit (斤).
2. **Calculate the rate (斤率)**: Divide the total money by the total weight in 斤 to find the price per 斤.
3. **Output the results**: The results are expressed in terms of the price per 斤 for the given total weight.

This code adheres to the structure of the procedure ("術") provided in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 1
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/79949
Variable 'c' has wrong value. Expected: 7897/384, Actual: 79949/384
Variable 'd' has wrong value. Expected: 68, Actual: 5364480/79949"""
