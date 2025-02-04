"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (jin) of silk based on the total money spent and the total weight of silk purchased. The procedure involves breaking down the weight into its components (shi, jun, jin, liang) and calculating the price per jin based on these components.

### Problem Breakdown:
- Total money spent: 1120 qian.
- Total weight of silk: 1 shi, 2 jun, 18 jin.
- 1 shi = 4 jun, 1 jun = 30 jin, and 1 jin = 16 liang.

### Procedure:
1. Convert the total weight into jin.
2. Use the total money and the total weight in jin to calculate the price per jin.
3. Break down the price per jin into its components (shi, jun, jin).

### Solution in Python Code:


"""


from fractions import Fraction

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 1石 = 4鈞, 1鈞 = 30斤
總斤 = 石 * 4 * 30 + 鈞 * 30 + 斤

# 計算每斤的價格
每斤價格 = Fraction(錢數, 總斤)

# 計算每鈞的價格 (1鈞 = 30斤)
每鈞價格 = 每斤價格 * 30

# 計算每石的價格 (1石 = 4鈞 = 120斤)
每石價格 = 每鈞價格 * 4

# 結果
a = 每鈞價格  # 每鈞的價格
b = 每斤價格  # 每斤的價格
c = 每石價格  # 每石的價格
d = 每斤價格  # 每斤的價格

# Output
a, b, c, d


"""


### Explanation of Variables:
- `總斤`: Total weight in jin.
- `每斤價格`: Price per jin.
- `每鈞價格`: Price per jun (30 jin).
- `每石價格`: Price per shi (120 jin).

### Final Answer:
- Price per jun: `a` qian.
- Price per jin: `b` qian.
- Price per shi: `c` qian.
- Price per jin: `d` qian.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 5600/33
Variable 'b' has wrong value. Expected: 5, Actual: 560/99
Variable 'c' has wrong value. Expected: 13/12, Actual: 22400/33
Variable 'd' has wrong value. Expected: 6, Actual: 560/99"""
