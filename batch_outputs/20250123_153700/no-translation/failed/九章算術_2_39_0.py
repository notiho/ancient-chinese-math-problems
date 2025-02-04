"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
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

# 計算每鈞的價格
每鈞價格 = 每銖價格 * (30 * 16 * 24)

# 計算每石的價格
每石價格 = 每鈞價格 * 4

# 結果
a = 每鈞價格.numerator  # 鈞的價格 (分子部分)
b = 每鈞價格.denominator  # 鈞的價格 (分母部分)
c = 每石價格.numerator  # 石的價格 (分子部分)
d = 每石價格.denominator  # 石的價格 (分母部分)

# 輸出結果
print(f"其 {a} 鈞，石 {b} 錢。其 {c} 石，石 {d} 錢。")


"""


### Explanation of the Code:
1. **Unit Conversion**: Convert all weights into the smallest unit (銖) to simplify calculations.
2. **Price per Unit**: Calculate the price per 銖 by dividing the total money by the total weight in 銖.
3. **Price for Larger Units**: Multiply the price per 銖 by the number of 銖 in a 鈞 or 石 to get their respective prices.
4. **Fraction Representation**: Use the `Fraction` class to ensure precise representation of prices in fractional form.

This code will output the price per 鈞 and per 石 in fractional form, as required.
"""


"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 160934400
Variable 'b' has wrong value. Expected: 8051, Actual: 79949
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 643737600
Variable 'd' has wrong value. Expected: 8052, Actual: 79949"""
