"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit of weight (石, 鈞, 斤, 兩, 銖) for the given amount of money and weight. Here's the step-by-step Python implementation:


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

# 各置所買石、鈞、斤、兩以為法
# Convert everything to 銖 (smallest unit)
銖_per_兩 = 24
銖_per_斤 = 16 * 銖_per_兩
銖_per_鈞 = 30 * 銖_per_斤
銖_per_石 = 4 * 銖_per_鈞

總銖 = (石 * 銖_per_石) + (鈞 * 銖_per_鈞) + (斤 * 銖_per_斤) + (兩 * 銖_per_兩) + 銖

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
每銖價格 = Fraction(實, 總銖)

# 不滿法者反以實減法，法賤實貴
# Calculate the price for each unit
每石價格 = 每銖價格 * 銖_per_石
每鈞價格 = 每銖價格 * 銖_per_鈞

# Output results
a = 每石價格.numerator
b = 每石價格.denominator
c = 每鈞價格.numerator
d = 每鈞價格.denominator

print(f"其 {a}石 ，兩 {b}錢 。其 {c}鈞 ，兩 {d}錢 。")
#----- content ends here -----


"""


### Explanation:
1. **Conversion to 銖**: Since 銖 is the smallest unit, we convert all weights to 銖 for consistent calculations.
2. **Calculate Total 銖**: Sum up the total weight in 銖.
3. **Price per 銖**: Divide the total money by the total 銖 to get the price per 銖.
4. **Price per 石 and 鈞**: Multiply the price per 銖 by the number of 銖 in a 石 or 鈞 to get their respective prices.
5. **Output**: The results are expressed as fractions to maintain precision.

This code calculates the price per 石 and 鈞 in terms of 錢.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600
Variable 'b' has wrong value. Expected: 4, Actual: 79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400
Variable 'd' has wrong value. Expected: 5, Actual: 79949"""
