"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight of silk in terms of "石" (shi), "鈞" (jun), "斤" (jin), and "兩" (liang). The total cost is 13,970 units of money, and the total weight is 1石2鈞28斤3兩5銖. We will compute the price per unit weight step by step.

Here is the Python code:


"""


from fractions import Fraction

# Total cost in money
total_money = 13970

# Total weight in terms of 石, 鈞, 斤, 兩, 銖
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
jin_per_shi = 120  # 1石 = 120斤
jin_per_jun = 30   # 1鈞 = 30斤
liang_per_jin = 16 # 1斤 = 16兩
zhu_per_liang = 24 # 1兩 = 24銖

# Convert total weight to 銖 (smallest unit)
total_zhu = (shi * jin_per_shi + jun * jin_per_jun + jin) * liang_per_jin * zhu_per_liang + liang * zhu_per_liang + zhu

# Calculate price per 銖
price_per_zhu = Fraction(total_money, total_zhu)

# Convert price per 銖 to price per larger units
price_per_liang = price_per_zhu * zhu_per_liang
price_per_jin = price_per_liang * liang_per_jin
price_per_jun = price_per_jin * jin_per_jun
price_per_shi = price_per_jin * jin_per_shi

# Assign results to variables
a = price_per_shi  # Price per 石
b = price_per_liang  # Price per 兩
c = price_per_jun  # Price per 鈞
d = price_per_liang  # Price per 兩 (same as b)

# Output results
a, b, c, d


"""


### Explanation:
1. **Weight Conversion**: Convert the total weight into the smallest unit (銖) using the given conversion factors.
2. **Price Calculation**: Compute the price per 銖 by dividing the total money by the total weight in 銖.
3. **Unit Conversion**: Convert the price per 銖 to prices per larger units (兩, 斤, 鈞, 石).
4. **Results**: Assign the computed prices to the variables `a`, `b`, `c`, and `d`.

The variables `a`, `b`, `c`, and `d` now hold the prices per 石, 兩, 鈞, and 兩, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 4, Actual: 335280/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400/79949
Variable 'd' has wrong value. Expected: 5, Actual: 335280/79949"""
