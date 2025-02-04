"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (斤) for the silk based on the total cost and the total weight. Here's the step-by-step Python code following the ancient Chinese procedure:


"""


from fractions import Fraction

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 各置所買石、鈞、斤以為法
石法 = 16 * 24  # 1 石 = 16 鈞, 1 鈞 = 24 斤
鈞法 = 24  # 1 鈞 = 24 斤
斤法 = 1  # 1 斤 = 1 斤

# 總重量 (斤)
總重量 = 石 * 石法 + 鈞 * 鈞法 + 斤 * 斤法

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
斤率 = Fraction(實, 總重量)

# 計算各單位的價格
a = 斤率 * 鈞法  # 每鈞的價格
b = 斤率  # 每斤的價格
c = 斤率 * 石法  # 每石的價格
d = b  # 每斤的價格 (同 b)

# Output results
a, b, c, d


"""


### Explanation:
1. **Weight Conversion**: Convert the total weight into 斤 (jin) using the relationships:
   - 1 石 = 16 鈞
   - 1 鈞 = 24 斤
2. **法 (denominator)**: The total weight in 斤 is used as the denominator.
3. **實 (numerator)**: The total cost (1120) is used as the numerator.
4. **Rate Calculation**: Divide the total cost by the total weight to get the price per 斤.
5. **Unit Prices**: Multiply the price per 斤 by the conversion factors to get the price per 鈞 and per 石.

### Final Answer:
- 每鈞的價格: `a` 錢
- 每斤的價格: `b` 錢
- 每石的價格: `c` 錢
- 每斤的價格 (again): `d` 錢
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 896/15
Variable 'b' has wrong value. Expected: 5, Actual: 112/45
Variable 'c' has wrong value. Expected: 13/12, Actual: 14336/15
Variable 'd' has wrong value. Expected: 6, Actual: 112/45"""
