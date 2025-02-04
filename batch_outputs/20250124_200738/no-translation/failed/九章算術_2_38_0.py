"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (斤) for the given amount of money and weight. Here's the Python code following the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 各置所買石、鈞、斤以為法
法 = 石 * 120 + 鈞 * 20 + 斤  # 1石 = 120斤, 1鈞 = 20斤

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
斤率 = Fraction(實, 法)

# 計算每鈞和每石的價格
a = 20 * 斤率  # 每鈞的價格 (1鈞 = 20斤)
b = 斤率  # 每斤的價格
c = 120 * 斤率  # 每石的價格 (1石 = 120斤)
d = 斤率  # 每斤的價格

# Output results
a, b, c, d
#----- content ends here -----


"""


### Explanation:
1. **法**: The total weight in 斤 is calculated by converting 石 and 鈞 into 斤 and adding them to the given 斤.
   - 1 石 = 120 斤
   - 1 鈞 = 20 斤
2. **斤率**: The price per 斤 is calculated by dividing the total money (錢數) by the total weight (法).
3. **a, b, c, d**: Using the 斤 rate, we calculate the price per 鈞 and 石, as well as the price per 斤 for both cases.

This code calculates the required values for the problem.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 11200/89
Variable 'b' has wrong value. Expected: 5, Actual: 560/89
Variable 'c' has wrong value. Expected: 13/12, Actual: 67200/89
Variable 'd' has wrong value. Expected: 6, Actual: 560/89"""
