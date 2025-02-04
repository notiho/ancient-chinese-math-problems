"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this problem, we need to calculate the price per "斤" (jin) and per "石" (shi) based on the total cost and the total weight of silk purchased. Here's the Python code to compute the values of the unknowns `a`, `b`, `c`, and `d`:


"""


from fractions import Fraction

# Total money spent
total_money = 13970  # in 錢

# Total weight purchased
total_shi = 1  # 石
total_jun = 2  # 鈞
total_jin = 28  # 斤
total_liang = 3  # 兩
total_zhu = 5  # 銖

# Convert the total weight into 鈞 (1 石 = 4 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖)
total_weight_in_jin = (
    total_shi * 4 * 30 +  # 石 to 鈞 to 斤
    total_jun * 30 +      # 鈞 to 斤
    total_jin +           # 斤
    Fraction(total_liang, 16) +  # 兩 to 斤
    Fraction(total_zhu, 16 * 24)  # 銖 to 斤
)

# Calculate the price per 斤 (a 錢 per 斤)
a = Fraction(total_money, total_weight_in_jin)

# Calculate the price per 鈞 (b 錢 per 鈞, 1 鈞 = 30 斤)
b = a * 30

# Calculate the price per 石 (c 錢 per 石, 1 石 = 4 鈞)
c = b * 4

# Calculate the price per 鈞 when considering 石 (d 錢 per 鈞)
d = c / 4

# Results
a  # Price per 斤 in 錢
b  # Price per 鈞 in 錢
c  # Price per 石 in 錢
d  # Price per 鈞 in 錢 when considering 石


"""


### Explanation:
1. **Weight Conversion**: The total weight is converted into a single unit (斤) using the relationships:
   - 1 石 = 4 鈞
   - 1 鈞 = 30 斤
   - 1 斤 = 16 兩
   - 1 兩 = 24 銖
2. **Price Calculation**:
   - The price per 斤 (`a`) is calculated by dividing the total money by the total weight in 斤.
   - The price per 鈞 (`b`) is derived by multiplying the price per 斤 by 30 (since 1 鈞 = 30 斤).
   - The price per 石 (`c`) is derived by multiplying the price per 鈞 by 4 (since 1 石 = 4 鈞).
   - The price per 鈞 when considering 石 (`d`) is derived by dividing the price per 石 by 4.

The variables `a`, `b`, `c`, and `d` now contain the respective prices in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 2013, Actual: 160934400/79949"""
