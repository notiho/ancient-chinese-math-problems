"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
To solve this problem, we need to calculate the price per unit weight (銖 rate) and then determine the values of `a`, `b`, `c`, and `d`. The problem involves converting the total weight into smaller units and dividing the total cost by the total weight.

Here is the Python code to compute the values:


"""


from fractions import Fraction

# Given data
total_money = 13970  # in 錢
total_weight_stone = 1  # 石
total_weight_jun = 2  # 鈞
total_weight_jin = 28  # 斤
total_weight_liang = 3  # 兩
total_weight_zhu = 5  # 銖

# Conversion factors
jin_to_liang = 16  # 1 斤 = 16 兩
liang_to_zhu = 24  # 1 兩 = 24 銖
jun_to_jin = 30  # 1 鈞 = 30 斤
stone_to_jun = 4  # 1 石 = 4 鈞

# Convert total weight to 銖
total_weight_zhu += (total_weight_liang * liang_to_zhu)  # 兩 to 銖
total_weight_zhu += (total_weight_jin * jin_to_liang * liang_to_zhu)  # 斤 to 銖
total_weight_zhu += (total_weight_jun * jun_to_jin * jin_to_liang * liang_to_zhu)  # 鈞 to 銖
total_weight_zhu += (total_weight_stone * stone_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu)  # 石 to 銖

# Calculate 銖 rate
zhu_rate = Fraction(total_money, total_weight_zhu)

# Convert 銖 rate to 鈞 and 銖
zhu_per_jun = jun_to_jin * jin_to_liang * liang_to_zhu  # 鈞 to 銖
a = zhu_rate // zhu_per_jun  # 鈞 part
b = zhu_rate % zhu_per_jun  # 銖 part

# Convert 銖 rate to 石 and 銖
zhu_per_stone = stone_to_jun * zhu_per_jun  # 石 to 銖
c = zhu_rate // zhu_per_stone  # 石 part
d = zhu_rate % zhu_per_stone  # 銖 part

# Results
a = int(a)  # 鈞
b = Fraction(b)  # 銖
c = int(c)  # 石
d = Fraction(d)  # 銖

# Output variables
a, b, c, d


"""


### Explanation:
1. **Conversion to 銖**: The total weight is converted into the smallest unit (銖) using the given conversion factors.
2. **銖 Rate Calculation**: The total money is divided by the total weight in 銖 to find the rate per 銖.
3. **鈞 and 銖 Calculation**: The rate is converted into 鈞 and 銖 using integer division and modulo.
4. **石 and 銖 Calculation**: Similarly, the rate is converted into 石 and 銖.

The final values of `a`, `b`, `c`, and `d` will contain the solution.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 0
Variable 'b' has wrong value. Expected: 5, Actual: 13970/79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 0
Variable 'd' has wrong value. Expected: 6, Actual: 13970/79949"""
