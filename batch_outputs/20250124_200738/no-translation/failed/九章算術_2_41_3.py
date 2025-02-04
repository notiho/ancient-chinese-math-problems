"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (斤) based on the total amount of money spent and the total weight of silk purchased. Here's the step-by-step Python code:


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
# 1 石 = 120 斤, 1 鈞 = 30 斤, 1 兩 = 1/16 斤, 1 銖 = 1/384 斤
總斤 = 石 * 120 + 鈞 * 30 + 斤 + Fraction(兩, 16) + Fraction(銖, 384)

# 計算每斤的價格
每斤價格 = Fraction(錢數, 總斤)

# 結果
a = 石
b = 每斤價格
c = 總斤
d = 每斤價格

# Output
a, b, c, d
#----- content ends here -----


"""


### Explanation:
1. **Weight Conversion**:
   - Convert all units (石, 鈞, 斤, 兩, 銖) into a single unit (斤) for consistency.
   - Use the conversion rates: 1 石 = 120 斤, 1 鈞 = 30 斤, 1 兩 = 1/16 斤, 1 銖 = 1/384 斤.

2. **Price Calculation**:
   - Divide the total money spent (`錢數`) by the total weight in 斤 (`總斤`) to get the price per 斤.

3. **Output**:
   - The results are expressed in terms of the total weight and the price per 斤.

This code calculates the price per 斤 and provides the results as requested.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 1
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/79949
Variable 'c' has wrong value. Expected: 7897/384, Actual: 79949/384
Variable 'd' has wrong value. Expected: 68, Actual: 5364480/79949"""
