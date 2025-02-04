"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (in terms of 石, 鈞, 斤, etc.) for the given amount of money and silk. The procedure involves dividing the total money by the total weight, then calculating the price per unit for each weight category.

Here is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
# Convert the total weight into a single unit (銖) for easier calculation
# 1 石 = 4 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Total weight in 銖
總銖 = (
    石 * 4 * 30 * 16 * 24 +
    鈞 * 30 * 16 * 24 +
    斤 * 16 * 24 +
    兩 * 24 +
    銖
)

# Calculate the price per 銖
每銖價格 = Fraction(錢數, 總銖)

# Calculate the price for each unit
# 石
每石價格 = 每銖價格 * (4 * 30 * 16 * 24)

# 鈞
每鈞價格 = 每銖價格 * (30 * 16 * 24)

# 斤
每斤價格 = 每銖價格 * (16 * 24)

# 兩
每兩價格 = 每銖價格 * 24

# 銖
每銖價格 = 每銖價格

# Convert the results into human-readable form
a = 每石價格.numerator // 每石價格.denominator  # 石 price in whole numbers
b = 每石價格 - a  # Remaining fraction for 石

c = 每鈞價格.numerator // 每鈞價格.denominator  # 鈞 price in whole numbers
d = 每鈞價格 - c  # Remaining fraction for 鈞

print(f"其 {a} 石 ，兩 {b} 錢 。其 {c} 鈞 ，兩 {d} 錢 。")
#----- content ends here -----


"""


### Explanation:
1. **Convert all weights to the smallest unit (銖)**: This ensures consistent calculations.
2. **Calculate the price per 銖**: Divide the total money by the total weight in 銖.
3. **Calculate the price for each unit (石, 鈞, etc.)**: Multiply the price per 銖 by the number of 銖 in each unit.
4. **Output the results**: Convert the fractional results into a human-readable format.

### Example Output:
If you run the above code, it will calculate the price per 石 and 鈞, and provide the results in terms of whole numbers and remaining fractions.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 8051
Variable 'b' has wrong value. Expected: 4, Actual: 68201/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 2012
Variable 'd' has wrong value. Expected: 5, Actual: 77012/79949"""
